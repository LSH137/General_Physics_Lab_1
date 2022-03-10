import math

a = 150.0
R = list()
R_average = 0.0
R_sigma = 0.0

for i in range(3):
    h = float(input("enter h: "))
    R.append(a**2/(6*h) + h/2)
    print(f"R = {R[i]}")

#get everage
for i in range(3):
    R_average = R_average + R[i]
R_average = R_average / 3
print(f"average = {R_average}")

#ger sigma
for i in range(3):
    R_sigma = R_sigma + (R[i] - R_average)**2
R_sigma = math.sqrt(R_sigma/2)
print(f"sigma = {R_sigma}")
