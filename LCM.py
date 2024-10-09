def LCM(a,b):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    return abs(a * b) // gcd(a, b)

a,b = map(int, input("Enter the numbers: ").split())
print(f"LCM of {a} and {b} = {LCM(a,b)}")