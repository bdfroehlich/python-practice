# recursive functions - sum of numbers 1 through n
def sum(n):
    # base case - when recursion ends
    if n < 0:
        return 0
    # recursive case - everytime we call this we should get closer and closer to base case
    else:
        print(n)
        return(n + sum(n - 1))

# factorial recursion
def find_fact(num):

    # base case
    if num == 1:
        return 1
    
    # recursive case
    else:
        return(num * find_fact(num - 1))

#factorial iterative
def find_fact_iterative(num):
    factorial = 1

    for i in range(1, num+1):
        factorial = factorial * i
    
    return factorial



#output
print(sum(3))
print(find_fact(4))
print(find_fact_iterative(4))