max_number = 100

prime_numbers = []

# prime num is always greater than 1
for num in range(2, max_number):
    for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            prime_numbers.append(num)
print(prime_numbers)
