def hello():
    print("hello user, welcome!")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch( list ):
    # check if list length is = 0
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        # for element (i) in the range of the length of the given list
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat my {list[0]}")
            else:
                print(f"Next I eat my {list[i]}")



#output
hello()
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["pizza", "yogurt", "ice-cream", "chocolate"])