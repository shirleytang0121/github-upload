import math
mins = 42
second = 42
TotalSecond = mins*60+second
print("The total seconds is ", TotalSecond)

GivenRadius1 = 4
GivenRadius2 = 6
Volume1 = (4/3)*math.pi*GivenRadius1**3
Volume2 = (4/3)*math.pi*GivenRadius2**3
print("The volume of the sphere with radius 4 is", Volume1, "\nthe volume of the sphere with radius 6 is", Volume2)

TempFa = -40
TempCe = (TempFa-32)*5/9
print("If the temperature is -40 in Fahrenheit, then the temperature in Celsius is", TempCe)

a = 1
length = 1*a
width = 2*a
height = 3*a
VolumeOfRP = length*width*height
VolumeOfCube = a*a*a
NumFit = VolumeOfRP//VolumeOfCube
print(NumFit, "cubes can fit in the rectangular prism")
