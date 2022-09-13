def proterm(i, value, x):
	pro = 1;
	for j in range(i):
		pro = pro * (value - x[j]);
	return pro;

def dividedDiffTable(x, y, n):

	for i in range(1, n):
		for j in range(n -1, i):
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
									(x[j] - x[i + j]));
	return y;

def fact(n):
    fact = 1

    for i in range(1,n):
        fact = fact*i
    return fact

def applyFormula(value, x, y, n):

	sum = y[n-1][0];

	for i in range(1, n):
		sum = sum + ((proterm(i, value, x) * y[n-1][i])/fact(i));

	return sum;

def printDiffTable(y, n):

	for i in range(n):
		for j in range(n - i):
			print(round(y[i][j], 4), "\t",
							end = " ");

		print("");


n = int(input("enter the number of data points:"));
y = [[0 for i in range(10)]
		for j in range(10)];
x = []
print("enter the data :")
for i in range(n):
    x.append(int(input("x coordinate:")))
    y[i][0].append(int(input("y coordinate:")))

y=dividedDiffTable(x, y, n);

printDiffTable(y, n);
value = int(input("enter the value to be interpolated:"))

print("\nValue at", value, "is",
		round(applyFormula(value, x, y, n), 2))
