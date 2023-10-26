#1.1 Implement a recursve function to calculate factor

def fact_rec(n):
   if n==0 or n==1:
      return 1
   else:
    return n*fact_rec (n-1)

number = 2
res = fact_rec (number)

print("The factoiral of {} is {}.".format (number, res))
