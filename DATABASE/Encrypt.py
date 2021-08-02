from cryptography.fernet import Fernet

# this generates a key and opens a file 'key.key' and writes the key there
key = Fernet.generate_key()
file = open('DATABASE/Assets/key.key', 'wb')
file.write(key)
file.close()

# this just opens your 'key.key' and assings the key stored there as 'key'
file = open('DATABASE/Assets/key.key', 'rb')
key = file.read()
file.close()

   # this opens your json and reads its data into a new variable called 'data'
with open('DATABASE/Assets/User_Log.json', 'rb') as f:
        data = f.read()

    # this encrypts the data read from your json and stores it in 'encrypted'
fernet = Fernet(key)
encrypted = fernet.encrypt(data)
decrypted = fernet.decrypt(encrypted)
    # this writes your new, encrypted data into a new JSON file
with open('DATABASE/Assets/User_Log.json', 'wb') as f:
        f.write(encrypted)
