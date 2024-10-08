def PrimeFactors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    if n > 2:
        factors.append(n)
    
    return factors

n = int(input("Enter the number: "))
print(f"Prime factors of {n} = {PrimeFactors(n)}")
