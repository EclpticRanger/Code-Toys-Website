I = int
P = int(input("Enter initial amount: "))
R = float(input("Enter rate: "))
T = int(input("Enter time: "))

I = (P * R * T) / 100
print("Simple interest: ", I)