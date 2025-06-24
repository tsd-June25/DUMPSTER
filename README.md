# DUMPSTER

This repository contains a small Windows-friendly application for scanning your
`Documents`, `Desktop`, and `Downloads` folders for `.txt` files. It displays
results sorted by modification time in either ascending or descending order.

## Requirements

- Python 3.8 or newer.
- No additional packages are required; the application uses Python's built-in
  `tkinter` GUI library.

## Usage

1. Ensure Python is installed on your machine.
2. Run the application from a command prompt:

   ```bash
   python scan_txt_files.py
   ```

3. Choose the sort order (Ascending or Descending) and click **Scan**. The list
   will populate with timestamped entries for every `.txt` file found in the
   specified folders and their subfolders.

This script should work on Windows out of the box, but it can also run on other
platforms where the `Documents`, `Desktop`, and `Downloads` directories exist in
the user's home folder.
