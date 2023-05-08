from cryptography.fernet import Fernet
import os


def encrypt_decrypt(message, key):
    # Generate a random salt and add it to the key
    salt = os.urandom(16)
    salted_key = key + salt

    # Derive a 256-bit key from the salted key using PBKDF2
    kdf = Fernet.generate_key()
    f = Fernet(kdf)

    # Encrypt the message using the derived key and salt
    encrypted_message = f.encrypt(salted_key + message.encode())

    # Decrypt the message using the derived key and salt
    decrypted_message = f.decrypt(encrypted_message)
    decrypted_message = decrypted_message[len(salted_key):].decode()

    # Print the encrypted message and decrypted message
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")


# Ask the user for a message and a password
message = input("Enter a message to encrypt: ")
password = input("Enter a password: ").encode()

# Encrypt and decrypt the message using the password
encrypt_decrypt(message, password)
