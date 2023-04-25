A = int(input())
B = int(input())

DivA = 0
DivB = 0

for i in range(1, A):
    if A % i == 0:
        DivA = DivA + i

for i in range(1, B):
    if B % i == 0:
        DivB = DivB + i

if DivA == B and DivB == A:
    print("ok")
else:
    print("nok")