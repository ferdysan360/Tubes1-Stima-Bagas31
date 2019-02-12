def evaluate(x, y, opr):
	if (opr == '+'):
		return (x + y)
	elif (opr == '-'):
		return (x - y)
	elif (opr == '*'):
		return (x * y)
	elif (opr == '/'):
		if (y != 0):
			return (x / y)
		else:
			return -999

def solve24(arr):
	arr.sort()
	opr = ['+', '-', '*', '/']
	opr_val = [5, 4, 3, 2]

	c_result = -999
	c_point = -999
	chosen_opr = ['.','.','.']

	for i in range(4):
		t_result = evaluate(arr[0], arr[3], opr[i])
		t_point = opr_val[i] - abs(t_result - 12)
		if (t_point > c_point):
			c_result = t_result
			c_point = t_point
			chosen_opr[0] = opr[i]

	result = c_result
	point = c_point
	c_result = -999
	c_point = -999

	for i in range(4):
		t_result = evaluate(result, arr[1], opr[i])
		t_point = point + opr_val[i] - abs(t_result - 18) + abs(result - 12)
		# untuk tanda kurung
		if (chosen_opr[0] == '+' or chosen_opr[0] == '-') and (opr[i] == '*' or opr[i] == '/'):
			t_point -= 1
		if (t_point > c_point):
			c_result = t_result
			c_point = t_point
			chosen_opr[1] = opr[i]

	result = c_result
	point = c_point
	c_result = -999
	c_point = -999

	for i in range(4):
		t_result = evaluate(result, arr[2], opr[i])
		t_point = point + opr_val[i] - abs(t_result - 24) + abs(result - 18)
		# untuk tanda kurung
		if (chosen_opr[1] == '+' or chosen_opr[1] == '-') and (opr[i] == '*' or opr[i] == '/'):
			t_point -= 1
		if (t_point > c_point):
			c_result = t_result
			c_point = t_point
			chosen_opr[2] = opr[i]

	result = c_result
	point = c_point

	exp = str(arr[0]) + chosen_opr[0] + str(arr[3])
	if (chosen_opr[0] == '+' or chosen_opr[0] == '-') and (chosen_opr[1] == '*' or chosen_opr[1] == '/'):
		exp = "(" + exp + ")" + chosen_opr[1] + str(arr[1])
	else:
		exp = exp + chosen_opr[1] + str(arr[1])

	if (chosen_opr[1] == '+' or chosen_opr[1] == '-') and (chosen_opr[2] == '*' or chosen_opr[2] == '/'):
		exp = "(" + exp + ")" + chosen_opr[2] + str(arr[2])
	else:
		exp = exp + chosen_opr[2] + str(arr[2])

	# print(str(arr[0]) + chosen_opr[0] + str(arr[3]) + chosen_opr[1] + str(arr[1]) + chosen_opr[2] + str(arr[2]) + " = " + str(result))
	print(exp + " = " + str(result))
	print("Point: " + str(point))

# Contoh Main Program

# arr = [-1 for i in range(4)]

# for i in range(4):
# 	arr[i] = int(input())

# solve24(arr)