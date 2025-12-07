from pypdf import PdfReader, PdfWriter
from datetime import datetime
import sys
from concurrent.futures import ThreadPoolExecutor

def is_valid_date(date_str):
    """Check if the given date string in YYMMDD format is a valid date."""
    try:
        datetime.strptime(date_str, "%y%m%d")
        return True
    except ValueError:
        return False

def decrypt_pdf(input_path, output_path, password):
    """Decrypt the PDF file with the given password."""
    reader = PdfReader(input_path)
    if reader.is_encrypted:
        reader.decrypt(password)

    writer = PdfWriter(clone_from=reader)

    writer.write(output_path)

def attempt_decrypt_with_password(args):
    """Try to decrypt the PDF using the provided password."""
    password, filename = args
    formatted_password = f"{password}"
    if is_valid_date(formatted_password):  # Check if the password is a valid date
        try:
            decrypt_pdf(filename, f'decrypted_{filename}', formatted_password)
            print("Success!")
            print(f"{formatted_password} - OK")
            exit(0)
            return True  # Indicate success
        except Exception as e:  # Catch the exception and assign it to e
            print(f"Error with password {formatted_password}: {e}", end="\r")
    return False

def generate_passwords():
    """Generate all valid YYMMDD combinations."""
    for yy in range(00, 100):  # YY 
        for mm in range(1, 13):  # Months from 01 to 12
            for dd in range(1, 32):  # Days from 01 to 31
                yield f"{yy:02d}{mm:02d}{dd:02d}"  # Format as YYMMDD

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    start_time = datetime.now()
    found = False

    print(f">> {filename}")

    # Generate passwords
    passwords = list(generate_passwords())

    with ThreadPoolExecutor(max_workers=16) as executor:
        for result in executor.map(attempt_decrypt_with_password, [(pwd, filename) for pwd in passwords]):
            if result:
                found = True
                break

    end_time = datetime.now()
    duration = end_time - start_time

    print("\r\n")
    print("     >> DONE!")
    print(f"     >> Script execution duration: {duration} found: {found}")
