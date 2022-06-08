# Accepts any number of named arguments and prints them in the pattern key : value one at a time.
def name_args(**kwargs):
    for arg in kwargs:
        print(f"{arg}:{kwargs[arg]}")

# Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
def all_true(*args):
    #all() function returns True if all items in an iterable are true, otherwise it returns False.
    return all(args)

#Returns True if one of the elements in an iterable is true.
def one_true(*args):
    return any(args)

#Uses recursion to find the factorial of an integer.
def factorial(n):

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


#Recursively removes all adjacent duplicate letters from a string.
def recursive_deduplicate(my_str,i=0):
  # if our string is empty or only has 1 thing, it's got no duplicates
  # if i is at the end of the string, no duplicates are left
  if len(my_str) <= 1 or i == len(my_str)-1:
    return my_str
  else:
    # str at current position is same as next position
    if my_str[i] == my_str[i+1]:
      #my_str[0:i] = slice string from indeces 0 up to current value of i(not included)
      print(f"{i}th run first print {my_str[0:i],i}")
      #my_str[i+1:] = slice string at i+1 and include everything to end of string
      print(f"{i}th run second print {my_str[i+1:],i}")
      print(f"{i}th run third print {my_str[0:i]+my_str[i+1:],i}")
      return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
    else:
      #no duplicate at current position, check next
      return recursive_deduplicate(my_str,i+1)

#Uses recursion to reverse a string
def recursive_reverse(string):
    if (len(string) == 0):
        return ""
    elif (len(string) == 1):
        return string
    else:
        return string[::-1]



#output
name_args(a="vehicles", b="motorcycles", c="cats")
#true all_true
print(all_true(3==3,2==2,"a"=="a"))
#false all true
print(all_true(3==3,2==2,4==5))
#one iterable is true
print(one_true(3==5,2==3,4==4))
print(factorial(4))
print(factorial(1))
print(f"{factorial(-1)}\n")
print(f"This is your string deduplicated {recursive_deduplicate('AABBCCDD')}.\n")
print(f"This is a your string reversed {recursive_reverse('reversed')}.")
print(f"This is an empty reversed string {recursive_reverse('')}.")
print(f"This is a single letter string reversed {recursive_reverse('r')}.")