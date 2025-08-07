n = int(input("enter the number  : "))

def factorial():
    product = 1
    for i in range(1, n+1):
        product = product * i
    print(f"thee factorial of {n} is : ", product)


factorial()