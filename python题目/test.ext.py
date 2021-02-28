def is_prime():
    for i in range(2, 100):
        count = 0
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
        if count == 2:
            print(i, end='-')
print(is_prime, type(is_prime))
if is_prime:
    print('ojkjgjif')
    print('888888')