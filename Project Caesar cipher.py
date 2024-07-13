def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Type 'encrypt' to encrypt a message, 'decrypt' to decrypt a message, or 'quit' to exit: ").lower()
        if choice == 'quit':
            break
        elif choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please try again.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'encrypt':
            result = caesar_cipher_encrypt(message, shift)
        else:
            result = caesar_cipher_decrypt(message, shift)
        
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
