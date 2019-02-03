def hitung(x,op,y):
    "Menghitung int 1 dengan int 2 dengan operator char"
    if (op == 1):
        return x + y
    elif (op == 2):
        return x - y
    elif (op == 3):
        return x * y
    elif (op == 4):
        return x / y

def IntToOp(x,op,y):
    if (op == 1):
        return x+'+'+y
    elif (op == 2):
        return x+'-'+y
    elif (op == 3):
        return x+'*'+y
    elif (op == 4):
        return x+'/'+y

def point(op):
    if (op == 1):
        return 5
    elif (op == 2):
        return 4
    elif (op == 3):
        return 3
    elif (op == 4):
        return 2

operation = ""
points = 0
hasil = 0;
maxx = 0
maxy = 0
maxop = 0

a = int(input("Input angka pertama : "))
b = int(input("Input angka kedua : "))
c = int(input("Input angka ketiga : "))
d = int(input("Input angka keempat : "))
