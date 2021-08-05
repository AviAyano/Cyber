alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


def brute_force(ciphertext):
    hacklist = ['from', 'no','to', 'me', 'at', 'am', 'is', 'are','the','in','and','will','The' ]
    ciphertextemp = ciphertext
    flag = True
    key = 0
    while(flag):
        ciphertextemp = decrypt(ciphertextemp, key)
        print('The key is ' + str(key), 'and the text is ' + ciphertextemp)
        for letter in hacklist:
            if (letter in ciphertextemp):
                print("Pay attention !")

        qinput = input('Does the text readable ? Y or N ' + "\n")
        if (qinput == 'Y'):
            flag = False
            break
        else:
            key += 1
    return ciphertextemp , key






if __name__ == '__main__':

    print(brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe"))