from cx_Freeze import setup, Executable
import sys
import os

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "tkinter", "pandas", "pytesseract", "PIL", "sv_ttk", "openpyxl"],
    "excludes": [] # Adjust this based on additional data files
}


base = None
if sys.platform == "win32":
    base = "Win32GUI"  # For Windows GUI application

executables = [
    Executable("Transactions_generator.py", base=base, target_name="TransactionProcessor.exe")
]

setup(
    name="TransactionProcessor",
    version="1.0",
    description="Transaction Processor Application",
    options={"build_exe": build_exe_options},
    executables=executables
)
