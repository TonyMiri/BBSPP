import pyperclip

e_or_d = input("Do you want to (E)ncrypt or (D)ecrypt a message?\n>").lower()
key = int(input("Please enter the encryption key (0-25):\n>"))

abc = [chr(x+97) for x in range(26)]
message = input('Enter the message:\n>').lower()
answer = ""
for x in message:
    if x == " ":
        answer += " "
        continue
    idx = abc.index(x)
    if e_or_d in ['E', 'e']:
        new_idx = idx + key 
        if new_idx > len(abc) - 1:
            temp = abs((len(abc) - 1) - new_idx) - 1
            answer += abc[temp]
        else:
            answer += abc[new_idx]
    elif e_or_d in ['D','d']:
        new_idx = idx - key
        if new_idx < 0:
            temp = new_idx + len(abc)
            answer += abc[temp]
        else:
            answer += abc[new_idx]
pyperclip.copy(answer)
print(answer)
print('Output copied to clipboard.')