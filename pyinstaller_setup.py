import sys
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = [
        'Transactions_generator.py',
        '--name', 'TransactionProcessor',
        '--onefile',
        '--windowed',
        '--hidden-import', 'tkinter',        # Ensure tkinter is included
        '--hidden-import', 'numpy',          # Ensure pandas is included        
        '--hidden-import', 'pandas',         # Ensure pandas is included
        '--hidden-import', 'pytesseract',    # Ensure pytesseract is included
        '--hidden-import', 'PIL',            # Ensure PIL (Pillow) is included
        '--hidden-import', 'openpyxl',       # Ensure openpyxl is included
        '--add-data', 'sv_ttk:sv_ttk',
        '--icon', './tools.ico'
    ]

    sys.exit(run(opts))
