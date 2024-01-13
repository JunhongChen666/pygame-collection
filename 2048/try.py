a = [1,2,3]

def add(lst):
    lst.append(4)

print(a)
add(a)
print(a)

a = 1

def sum(a):
    a = a+1

print(a)
sum(a)
print(a)


def a():
    for i in range(3):
        for j in range(4):
            if i+j==3:
                return 3
            else:
                return 4


b = a()
print(b)