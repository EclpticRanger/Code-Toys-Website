A = int()
P = float(input("Enter initial amount: "))
R = float(input("Enter rate: "))
T = int(input("Enter time in years: "))
N = int(input("Enter number of compunds per year: "))

A = P * (1+ ( R/ (N*100))) ** (N*T)
print("Compound interest: ", A)