def arb_args(*args):
    # iterate over any length of args and print each specific arg on its own line
    for arg in args:
        print(arg)

# Takes in two integers. Two nested functions should perform separate, 
# distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed.
def inner_func(a,b):
    def subtract():
        return a - b
    def add():
        return a + b
    print(subtract()+add())


# lunch_lady - Takes in two strings: a student's 
# name and their lunch preference. The function should print both strings. 
# If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady( name, lunch = "Mystery Meat"):
    print(f"Hi my name is {name} and I like to eat {lunch}.")

# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(a,b):
    sum = a + b
    multiply = a * b
    return sum, multiply

# alias_arb_args - Should be arb_args but assigned an alias. 
# Remember, variables can hold functions in Python just like they can in JS. 
# Alternatively, you can call a function from inside another function
alias_arb_args = arb_args

# arb_mean - Accepts any number of integers and prints their average
def arb_mean(*integers):
    total = 0
    for int in integers:
        total += int
    print(total/len(integers))

# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*strings):
    length = 0
    longest_string = ""
    for string in strings:
        if(len(string) > length ):
            length = len(string)
            longest_string = string
    return longest_string

        

#output
arb_args(1,2,3,"john",8,9,"fred")
inner_func(5,4)
lunch_lady("Bob","Pizza")
lunch_lady("Bob")
print(sum_n_product(2,3))
arb_mean(1,2,3,4,5,6)
print(arb_longest_string("Bob", "Fred", "Cynthia"))
