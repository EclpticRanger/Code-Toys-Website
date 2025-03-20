code = str(input())
string1 = 0
string2 = 0

for i in range(len(code)-1):
    if (i % 2) == 0:
        string1 += int(code[i])
    else:
        string2 += int(code[i])

string2 = str(string2)
string2 = int(code[0]) * 3


end = int(code[-1])
print(string1)
print(string2)
print(end)
