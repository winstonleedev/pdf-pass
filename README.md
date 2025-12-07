# pdf-pass

Small Python utility to attempt decrypting a PDF protected with a password in YYMMDD format (two-digit year, month, day).

## Requirements
- Python 3.8+
- pypdf (install with `pip install pypdf`)

## What it does
- Generates all YYMMDD combinations (00-99 for year, 01-12 for month, 01-31 for day).
- Validates each combination as a real date before attempting decryption.
- Uses ThreadPoolExecutor to attempt decryption concurrently.
- On success writes `decrypted_<original_filename>` and exits.

## Usage
Run from the command line:
```
python searchpw.py <protected.pdf>
```

Example:
```
python searchpw.py secret.pdf
```

## Configuration & tuning
- Thread count is currently set to 16 in the script. Reduce or increase depending on your CPU and I/O capabilities.
- Output file name is `decrypted_<input_filename>`.

## Notes & legal
- This script brute-forces passwords; use only on files you own or have explicit permission to test.
- Be aware of legal restrictions in your jurisdiction.

## Troubleshooting
- If decryption fails with an exception, the script prints the error and continues.
- Ensure `pypdf` is the installed library (not PyPDF2 or others) or adapt imports accordingly.

## License
GPL

Use at your own risk. No warranty provided.
