# Transaction Processor

<img src="https://github.com/mohankumarpaluru/transactions-extractor/raw/refs/heads/main/assets/ai-image.jpg" alt="Transaction Processor Logo" height="300">

## Overview
Transaction Processor is a Python-based tool designed to simplify and automate the extraction of transaction data from payment screenshots, specifically tailored for platforms like PhonePe. The tool uses Optical Character Recognition (OCR) to extract transaction details and saves them in a well-organized table within an Excel (.xlsx) and Word (.docx) document.

This application can be bundled as an executable file (.exe) to run without requiring Python or dependencies installed on the user's system.

---

## Features
- Extract transaction details from screenshots using OCR (powered by Tesseract).
- Supports common image formats (.jpeg, .jpg, .png).
- Outputs organized transaction data to Excel and Word files.
- User-friendly graphical interface built with Tkinter.
- Fully standalone executable with dependencies bundled using PyInstaller.
- Sorts transactions by timestamp and computes total transaction amounts.
- Dark mode interface with modern design using `sv_ttk`.

---

## Requirements

### Python Dependencies
If running from source, the following dependencies are required:
- Python 3.8+
- `pytesseract`
- `pandas`
- `pillow` (PIL)
- `python-docx`
- `openpyxl`
- `tkinter`
- `sv_ttk`

Ensure Tesseract OCR is installed and its path is correctly configured in the script.

### Tesseract Installation
Download Tesseract OCR from: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

---

## Installation and Usage

### Running the Executable
1. Download the pre-built executable file (`TransactionProcessor.exe`).
2. Double-click the executable to launch the application.
3. Follow the GUI instructions to select the screenshot directory and specify the output file.
4. Click "Process Transactions" to generate the results.

### Running from Source
1. Clone this repository:
   ```
   git clone <repository-url>
   cd transactions-extractor
   ```
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python Transactions_generator.py
   ```

---

## Building the Executable

### Using PyInstaller
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Build the executable:
   ```
   python pyinstaller_setup.py
   ```
3. The executable will be available in the `dist` folder.

---

## GUI Features
1. **Input Directory Selection:** Browse and select the directory containing screenshots.
2. **Output File Selection:** Specify the location to save the Excel and Word files.
3. **Process Button:** Automatically extracts and organizes transaction data.
4. **Error Notifications:** Alerts for missing dependencies or unsupported files.

---

## Logo and Cover
A professional logo and cover have been designed to enhance the project's identity. They reflect the theme of digital transactions and innovation.

---

## Contribution
Feel free to fork the repository and submit pull requests. Suggestions and bug reports are welcome!

---
