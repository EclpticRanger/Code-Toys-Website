output = ""
sifer = int

def decode(text, sifer):
    output = ""
    sifer *= -1
    for i in range(len(text)):
        tmp = ord(text[i])
        tmp += sifer
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
    print(output)

def fix_sifer_numer(shift):
    while shift > 26 or shift < -26:
        if shift > 26:
            shift -= 26
        else:
            shift += 26

while True:
    print ("-------------")
    text = str(input())
    ed = input()
    sifer = int(input())
    fix_sifer_numer(sifer)
    if ed == "e":
        encode(text)
    elif ed == "d":
        decode(text, sifer)
    elif ed == "b":
        break

