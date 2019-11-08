alphabet = '=>?@[\\]678hiVWlmABCDEpqrsjkJKL01234RюБжэяЩРтшЦМйu&UмоПtлС5хКцvЧёgчwSещFTвНZ#ОькТЖЯЁфбГъуЗиргШЪ$ЮХыЫIXHЕ!ВДG"Фа%АYсЙЬИздЛoxyz<MNOPQnУЭпн9abcdef^_`{|}~ \'()*+,-./:;'

def encrypt():
    enc = ''
    
    msg = input('Type message for encrypting: ')
    key = input('Enter key for encrypting: ')
    
    for c in msg:
        if c in alphabet:
            s1 = alphabet.find(c)
            s1 = (s1 + int(key)) % len(alphabet)
            enc += alphabet[s1]
        else:
            enc += c
    print('Encrypted message: ' + enc)
    print('Key, what used for encrypting: ' + key)
    print('Goodbye!')

def decrypt():
    dec = ''
    
    msg = input('Type message for decrypting: ')
    key = input('Enter key for decrypting: ')
    
    for c in msg:
        if c in alphabet:
            s1 = alphabet.find(c)
            s1 = (s1 - int(key)) % len(alphabet)
            dec += alphabet[s1]
        else:
            dec += c
    print('Decrypted message: ' + dec)
    print('Key, what used for decrypting: ' + key)
    print('Goodbye!')

def main():
    print('''
    <====== UCrypt v1.0 ======>
         What do you want?
            0 - Encrypt
            1 - Decrypt''')
    k = input('\nYou choice (0/1): ')
    try:
        int(k)
    except ValueError:
        print('Error #0. Entered choice not a number.')
        exit()
    if k == '0':
        encrypt()
    elif k == '1':
        decrypt()
    else:
        print('Error #1. Enter 0 or 1 for choosing.')
        exit()

try:
    main()
except KeyboardInterrupt:
    print('Good bye!')
    exit()


