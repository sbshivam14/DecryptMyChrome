# DecryptMyChrome
# Chrome Password Decryption Automation

This project automates the **decryption of passwords saved in the Chrome Password Manager** on outdated versions of Chrome.  
It uses a combination of **Python** and **VBScript** to perform the process without requiring any manual interaction.  

The project is inspired by [decrypt-chrome-passwords](https://github.com) but extends its functionality by fully automating the execution.

⚠️ **Disclaimer**: This tool is provided for **educational and research purposes only**. Do not use it on systems you do not own or have explicit permission to test. The author assumes no responsibility for any misuse.

---

## Features
- Fully automated Chrome password decryption.
- Works with **outdated versions of Chrome** where the vulnerability exists.
- Automatically installs required dependencies if they are missing.
- Saves the results in a clean **CSV file** for easy access.

---

## Supported Operating Systems
- **Windows**

---

## Dependencies
The script requires the following Python modules:
- `sqlite3` (built-in with Python)
- `pycryptodomex`
- `pywin32`

If these dependencies are not installed, the script will automatically attempt to install them.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/sbshivam14/DecryptMyChrome.git
   cd DecryptMyChrome
   
2. Execute the script:
   ```bash
   ./DecryptMyChrome.vbs

3. Execute the Python Script Directly: (Optional)
   ```bash
   python DecryptMyChrome.py
