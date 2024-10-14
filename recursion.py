# recursive function
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
show(5)
###factorial of n
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
# write a code to find 1st n numbers of sum
def calc_sum(n):
    if n < 0:
        return 0
    else:
        return (n * (n+1)) / 2

print(calc_sum(5))