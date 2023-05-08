import tkinter as tk
import base64


def encrypt_decrypt():
    message = message_entry.get()
    key = key_entry.get()

    encrypted = ""
    decrypted = ""
    for i in range(len(message)):
        char = chr(ord(message[i]) ^ ord(key[i % len(key)]))
        encrypted += char

        decrypted_char = chr(ord(char) ^ ord(key[i % len(key)]))
        decrypted += decrypted_char

    encoded_message = base64.b64encode(encrypted.encode("utf-8"))
    decoded_message = base64.b64decode(encoded_message).decode("utf-8")

    encrypted_message_label.config(
        text="Encrypted message: " + encoded_message.decode("utf-8"), fg="#0C4B05")
    decrypted_message_label.config(
        text="Decrypted message: " + decrypted, fg="#BF0103")


# Create a tkinter window
window = tk.Tk()
window.title("Encryption and Decryption")
window.geometry("550x450")
window.config(bg="#E9F7EF")

# Create a message label and entry
message_label = tk.Label(window, text="Enter a message:", font=(
    "Arial", 14), bg="#E9F7EF", fg="#0C4B05")
message_label.pack(pady=10)
message_entry = tk.Entry(window, font=("Arial", 14), bd=2, relief="groove")
message_entry.pack()

# Create a key label and entry
key_label = tk.Label(window, text="Enter a key:", font=(
    "Arial", 14), bg="#E9F7EF", fg="#0C4B05")
key_label.pack(pady=10)
key_entry = tk.Entry(window, font=("Arial", 14), bd=2, relief="groove")
key_entry.pack()

# Create a button to encrypt and decrypt the message
encrypt_decrypt_button = tk.Button(window, text="Encrypt and Decrypt", font=(
    "Arial", 14), bg="#0C4B05", fg="white", bd=2, relief="groove", command=encrypt_decrypt)
encrypt_decrypt_button.pack(pady=20)

# Create labels to display the encrypted and decrypted messages
encrypted_message_label = tk.Label(
    window, text="", font=("Arial", 14), bg="#E9F7EF")
encrypted_message_label.pack(pady=10)
decrypted_message_label = tk.Label(
    window, text="", font=("Arial", 14), bg="#E9F7EF")
decrypted_message_label.pack()

# Run the tkinter window
window.mainloop()
