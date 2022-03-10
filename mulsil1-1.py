import math

PI = math.pi
volume_stack = 0.0
volume = list()
volume_mean = float()
volume_sigma = float()
temp = 0.0

for i in range(3):
    outerDiameter = float(input("enter outer diameter: "))
    innerDiameter = float(input("enter inner diameter: "))
    length = float(input("enter length: "))
    
    volume.append(((outerDiameter/2.0)**2 - (innerDiameter/2.0)**2) * PI * length)
    print(f"volume = {volume[i]}")
    print("=============================================")
    volume_stack = volume_stack + volume[i]

# get mean volume
volume_mean = volume_stack / 3.0

# get sigma
for i in range(3):
    temp = temp + (volume[i] - volume_mean)**2
temp = temp / 2
volume_sigma = math.sqrt(temp)

print(f"mean = {volume_mean}")
print(f"sigma = {volume_sigma}")
