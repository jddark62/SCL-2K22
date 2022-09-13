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


n = 5
y = [[0 for i in range(10)]
		for j in range(10)];
x = [45,50,55,60,65]

y[0][0] = 114.84
y[1][0] = 96.16
y[2][0] = 83.32
y[3][0] = 74.48
y[4][0] = 68.48

y=dividedDiffTable(x, y, n);

printDiffTable(y, n);
value = 63

print("\nValue at", value, "is",
		round(applyFormula(value, x, y, n), 2))
