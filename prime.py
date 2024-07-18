upper_limit = int(input("Enter the upper limit: "))

print("Prime numbers up to", upper_limit, ":")

for num in range(2, upper_limit + 1):
    is_prime = True  
 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
   
    if is_prime:
        print(num, end=" ")
