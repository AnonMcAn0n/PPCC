import argparse

def caesar_encrypt_with_password(text, password):
    reversed_password = password[::-1]
    password_shifts = [(ord(char) - 96) + len(password) for char in reversed_password]
    
    encrypted_text = ""
    password_index = 0
    
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift = password_shifts[password_index % len(password_shifts)]
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
            password_index += 1
        else:
            encrypted_text += char
    
    return encrypted_text


def caesar_decrypt_with_password(encrypted_text, password):
    reversed_password = password[::-1]
    password_shifts = [(ord(char) - 96) + len(password) for char in reversed_password]
    
    decrypted_text = ""
    password_index = 0
    
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift = password_shifts[password_index % len(password_shifts)]
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
            password_index += 1
        else:
            decrypted_text += char
    
    return decrypted_text


def encrypt_text(text, password):
    encrypted_text = caesar_encrypt_with_password(text, password)
    print("Encrypted text:", encrypted_text)


def decrypt_text(text, password):
    decrypted_text = caesar_decrypt_with_password(text, password)
    print("Decrypted text:", decrypted_text)


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encrypt", help="Encrypt a text")
group.add_argument("-d", "--decrypt", help="Decrypt an encrypted text")
args = parser.parse_args()

if args.encrypt:
    password = input("Enter the password: ")
    encrypt_text(args.encrypt, password)
elif args.decrypt:
    password = input("Enter the password: ")
    decrypt_text(args.decrypt, password)
else:
    print("No argument was provided. use -e to encrypt a text or -d to decrypt a text.")
