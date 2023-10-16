


def __encrypt(text: str, shift: int) -> [str, str]:
    text = text.upper()
    max_ascii_threshold = 90
    encrypted_text = ''
    encrypted_ascii = ''

    for character in text:
        ascii_val = ord(character)
        ascii_val += shift

        if ascii_val > max_ascii_threshold:
            ascii_val -= 26

        if ascii_val == 32 + shift:
            ascii_val = 32
        
        encrypted_ascii += str(ascii_val)
        encrypted_text += chr(ascii_val) 

    return [encrypted_ascii, encrypted_text]


def __decrypt(encrypted_ascii: str, shift: int) -> str:
    min_ascii_threshold = 65
    decrypted_text = ''

    for i in range(0, len(encrypted_ascii), +2):
        ascii_str = encrypted_ascii[i] + encrypted_ascii[i+1]
        ascii_int = int(ascii_str)
        ascii_int -= shift

        if ascii_int == 32 - shift:
            ascii_int = 32
        elif ascii_int < min_ascii_threshold:
            ascii_int += 26

        decrypted_text += chr(ascii_int)

    return decrypted_text


def run() -> None:
    while True:
        text = input("Enter text to encrypt and decrypt: ") 

        if text.lower() == 'x':
            break

        shift = int(input("Enter shift count: "))

        encrypted_ascii, encrypted_text = __encrypt(text, shift)
        decrypted_text = __decrypt(encrypted_ascii, shift)

        print(f'\nEncrypted ASCII: {encrypted_ascii}')
        print(f'Encrypted text: {encrypted_text}')
        print(f'Decrypted text: {decrypted_text}')

        print("\nPress X to quit...")
