cake = 1.0
percent = 0.01
x = 0
largest = []
place = []
for i in range(100):
    x = cake * percent
    cake -= x
    percent += 0.01

    largest.append(x)
    place.append(i)

a = max(largest)
print(a)
b = largest.index(a)
print(b + 1)



    




