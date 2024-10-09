def count_divisors(n):
    divisors_count = 1
    count = 0
    
    while n % 2 == 0:
        n = n // 2
        count += 1
    divisors_count *= (count + 1)
    
    for i in range(3, int(n**0.5) + 1, 2):
        count = 0
        while n % i == 0:
            n = n // i
            count += 1
        divisors_count *= (count + 1)
    
    if n > 2:
        divisors_count *= 2
    
    return divisors_count

n = int(input("Enter the number: "))
print(f"Number of Divisors of {n} = {count_divisors(n)}")