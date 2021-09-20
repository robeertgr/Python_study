A = '1234567'
print(A[1::2])

print(int(3.2))

name = "Michael Jackson"
print(name.find('el'))

a = '1'
b = '2'
print(a + b)

F = "You are wrong"
print(F.upper())

tuple1 = ("A", "B", "C")
print(tuple1[-1])

A = ((11, 12), [21, 22])
print(A[1])

A = ((11, 12), [21, 22])
print(A[0][1])

print('1, 2, 3,4'.split(','))

A = [1, 'a']
B = [2, 1, 'd']
print(A + B)

v = {'A', 'B'}
v.add('C')
print(v)

v = {'A', 'B', 'C'}
v.add('C')
print(v)

x = 'Go'
if x != 'Go':
    print('Stop')
else:
    print('Go')
print('Mike')

x = 'Go'
if x == 'Go':
    print('Stop')
else:
    print('Go')
print('Mike')

for n in range(3):
    print(n)

for n in range(3):
    print(n + 1)

A = ['1', '2', '3']
for a in A:
    print(2 * a)


def Add(x, y):
    z = y + x
    return y


print(Add(1, 1))


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x = ', self.x, 'y = ', self.y)


p1 = Points(1, 2)
p1.x = 2
p1.print_point()
