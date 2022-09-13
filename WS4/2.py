n = int(input("enter the number of datapoints :"))
x = []
y = []
print("enter the datapoints")
for i in range(n):
    x.append(int(input("x coordinate:")))
    y.append(int(input("y coordinate:")))

X = int(input("Enter the point to find y value:"))

Y = ((X - x[1])*(X - x[2]))/((x[0] - x[1])*(x[0] - x[2])) +((X - x[0])*(X - x[2]))/((x[1] - x[0])*(x[1] - x[2])) +((X - x[0])*(X - x[1]))/((x[2] - x[0])*(x[2] - x[1]))

print("the y coordinate of the given x is :",Y)