def porta_cipher(text, key, mode='encrypt'):
    porta_table = {
        'AB': 'NOPQRSTUVWXYZABCDEFGHIJKLM',
        'CD': 'OPQRSTUVWXYZNMABCDEFGHIJKL',
        'EF': 'PQRSTUVWXYZNOMABCDEFGHIJK',
        'GH': 'QRSTUVWXYZNOPABCDEFGHIJKLM',
        'IJ': 'RSTUVWXYZNOPQABCDEFGHIJKLM',
        'KL': 'STUVWXYZNOPQRABCDEFGHIJKLM',
        'MN': 'TUVWXYZNOPQRSABCDEFGHIJKLM',
        'OP': 'UVWXYZNOPQRSTABCDEFGHIJKLM',
        'QR': 'VWXYZNOPQRSTUABCDEFGHIJKLM',
        'ST': 'WXYZNOPQRSTUVABCDEFGHIJKLM',
        'UV': 'XYZNOPQRSTUVWABCDEFGHIJKLM',
        'WX': 'YZNOPQRSTUVWXABCDEFGHIJKLM',
        'YZ': 'ZNOPQRSTUVWXYABCDEFGHIJKLM',
    }

    result = []
    key_index = 0

    for char in text.upper():  # iterez peste fiecare poziție din plain text
        if char.isalpha():  # verific daca poziția char este un caracter alfabetic
            key_char = key[key_index % len(key)].upper()  # mapez litera din cheie peste litera curentă a textului
            for pair, alphabet in porta_table.items():  # iterez tabloul porta definit mai sus
                if key_char in pair:  # verific daca litera key_char se afla in perechea tabloului
                    if mode == 'encrypt':  # criptare
                        result.append(alphabet[ord(char) - ord('A')])
                        # normalizez indicele folosind codul ascii al literei
                        # caut litera din textul plain in linia tabloului corespunzator
                        # si adaug litera criptata la rezultat
                    else:  # decriptare
                        result.append(chr(alphabet.find(char) + ord('A')))  # inversul operatiei de criptare
                    break  # la incheierea criptarii/decriptarii literei, intrerup loopul curent
            key_index += 1
        else:
            result.append(char)  # adaug la rezultat si caracterele non-alfabetice (spatiile)
    return ''.join(result)  # concatenez lista de caractere si o returnez



with open('input.txt', 'r') as input_file, open('key.txt', 'r') as key_file:
    input_text = input_file.read()
    key = key_file.read().strip()

encrypted_text = porta_cipher(input_text, key, 'encrypt')

with open('encrypted.txt', 'w') as encrypted_file:
    encrypted_file.write(encrypted_text)

decrypted_text = porta_cipher(encrypted_text, key, 'decrypt')

with open('decrypted.txt', 'w') as decrypted_file:
    decrypted_file.write(decrypted_text)
