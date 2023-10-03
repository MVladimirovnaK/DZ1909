'''#Task 22

def newset(num):
    new_set = set()
    for i in range(num):
        new_set.add(int(input("Введите число для множества: ")))
    return new_set

n = int(input("Введите кол-во элементов первого множества: "))
n_set = newset(n)

m = int(input("Введите кол-во элементов второго множества: "))
m_set = newset(m)

print(*n_set)
print(*m_set)

s_set = sorted(n_set.intersection(m_set))
print(*s_set)'''

#Task 24. 

n = int(input("Введите кол-во кустов: "))
count = [int(i) for i in input("Введите через пробел кол-во ягод на " "каждом кусте: ").split()[:n]]
print(max([count[i - 2] + count[i - 1] + count[i] for i in range(n)]))