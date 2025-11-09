def main():
    base = int(input("base = "))
    exp = int(input("exponent = "))
    res = exponent(base, exp)
    print(f"{base} raises to the power of {exp}: {res}")

def exponent(base, exp):
    if exp <=0:
        return 1
    else: return base * exponent(base, exp-1)

main()