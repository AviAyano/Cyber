import string
alphabet =string.ascii_lowercase

def encrypt(plaintext, k):
    chipertext = []
    end = len(plaintext)
    for index in range(0,end) :
        number = int((index+k)%26)
        chipertext.append(alphabet[number])
    return ', '.join( map( lambda x: str(x)  ,  chipertext ) )

if __name__ == '__main__':
    k = int(input('Enter a integer number please: '))
    plaintext = input('Enter a text please: ')
    print(encrypt(plaintext, k))
