string = str(input("Enter string to be converted: "))
hexa = str()
binary = str()
ascii = str()
for i in range(len(string)):
    tmp = ord(string[i])
    ascii += (str(tmp) + " ")
    tmp = bin(ord(string[i]))
    binary += (str(tmp) + " ")
    tmp = hex(ord(string[i]))
    hexa +=(str(tmp) + " ")

print("ASCII: ", ascii)
print("Binary: ", binary)
print("Hexadecimal: ", hexa)

inta = int(input("Enter interger to be converted: "))

ascii = ord(str(inta))
tmp = bin(inta)
binary = str(tmp) + " "
tmp = hex(inta)
hexa = str(tmp) + " "

print("Binary: ", binary)
print("Hexadecimal: ", hexa)