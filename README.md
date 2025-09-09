# DecryptMyChrome
# Chrome Password Decryption Automation

This project automates the **decryption of passwords saved in the Chrome Password Manager** on outdated versions of Chrome.  
It uses a combination of **Python** and **VBScript** to perform the process without requiring any manual interaction.  

The project is inspired by [decrypt-chrome-passwords](https://github.com/ohyicong/decrypt-chrome-passwords) but extends its functionality by fully automating the execution.

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
1. Execute the VBScript file:
   ```bash
   ./DecryptMyChrome.vbs

2. Execute the Python Script Directly: (Optional)
   ```bash
   python DecryptMyChrome.py

   # Project Workflow

## How It Works 
## VBScript Automation ('DecryptMyChrome.vbs'

The **VBScript file** ensures the environment is ready to run the decryption script:

- ✅ Checks if Python is installed.  
- ✅ If missing, downloads and installs Python silently via PowerShell.  
- ✅ Installs the required **requests** Python module.  
- ✅ Executes the `DecryptMyChrome.py` script automatically.  

This guarantees the Python script will run seamlessly even on systems without prior setup.

---

## Python Script (`DecryptMyChrome.py`)

The Python script performs **Chrome password decryption** in four main steps:

### 🔹 Step 1: Retrieve the Encryption Key
- Reads the **Local State** file from Chrome’s user directory.  
- Extracts and Base64-decodes the `encrypted_key`.  
- Uses **Windows DPAPI** (`win32crypt.CryptUnprotectData`) to decrypt the key.  

### 🔹 Step 2: Extract Credentials from Database
- Copies Chrome’s **Login Data** SQLite file to avoid file locks.  
- Reads `action_url`, `username_value`, and `password_value` fields.  

### 🔹 Step 3: AES-GCM Decryption
- Splits the encrypted password into **Initialization Vector (IV)** and **ciphertext**.  
- Decrypts using the recovered **AES key** in GCM mode.  
- Converts the result into a readable **plaintext password**.  

### 🔹 Step 4: Output Results
Prints or saves the decrypted data in the format:  
- `URL: www.website.com'
- `Username: admin@admin.com'
- `Password: securepassword'

