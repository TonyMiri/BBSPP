#Brute force Caesar Cypher decryptor
msg = input('Enter the message you want to decrypt:\n>').upper()
for x in range(26):
    output = ""
    for y in msg:
        if y == " ":
            output += " "
            continue
        output += chr((ord(y)-97+x)%26+97)
    print(f'{x+1}: {output}')
