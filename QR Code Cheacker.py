code = str(input())
string1 = 0
string2 = 0
end = int(code[-1])

for i in range(len(code)-1):
    if (i % 2) == 0:
        string1 += int(code[i])
    else:
        string2 += int(code[i])

string1 = str(string1)
string2 = str(string2)
string2 = int(string2[0]) * 3
string2 = str(string2)
tmp = int(string2[0]) * int(string1[0])
tmp = str(tmp)
tmp = int(tmp[0]) + end
print(tmp)
if (tmp % 10) == 0:
    print("Valid")
else:
    print("Not Valid")
