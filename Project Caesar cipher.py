def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # check if the character is a letter
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += shifted_char
        else:
            ciphertext += char  # if the character is not a letter, append it unchanged
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)  # decryption is just shifting in the opposite direction

def main():
    print("Welcome to the Caesar Cipher encryption/decryption tool!")
    while True:
        choice = input("Do you want to encrypt (e) or decrypt (d) a message? (e/d): ").strip().lower()
        
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        message = input("Enter your message: ").strip()
        shift = int(input("Enter the shift value (a positive integer): "))
        
        if choice == 'e':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Do you want to encrypt/decrypt another message? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
