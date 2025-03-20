output = ""
sifer = int

def decode(text, sifer):
    output = ""
    for i in range(len(text)):
        tmp = ord(text[i])
        tmp -= sifer
        tmp = chr(tmp)
        output += tmp
    print(output)

def encode(text):
    output = ""
    for i in range(len(text)):
        tmp = ord(text[i])
        tmp += sifer
        tmp = chr(tmp)
        output += tmp
    output += chr(sifer)
    print(output)

while True:
    print ("-------------")
    text = str(input())
    ed = input()
    sifer = input()
    sifer = int(sifer)
    if sifer < 0:
        sifer *= -1
    if ed == "e":
        encode(text)
    elif ed == "d":
        decode(text, sifer)
    elif ed == "b":
        break

