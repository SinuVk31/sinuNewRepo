def factoarial(n):
 if n == 0:
   return 1
 else:
   return n * factoarial(n-1)
number =5
result = factorial(number)
print(f"The factoarial of {number} is {result}.")
