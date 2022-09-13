n = int(input("enter the number of datapoints :"))
x = []
y = []
print("enter the datapoints")
for i in range(n):
    x.append(int(input("x coordinate:")))
    y.append(int(input("y coordinate:")))

X = int(input("Enter the point to find y value:"))
Y = y[0] + (X - x[0])*((x[1] - x[0])/(y[1] - y[0]))

print("the y coordinate of given x is:",Y)
