import itertools # for permutation

################### functions  #############################
def sum_(a,b):
    if a == None or b == None:
        return None
    else:
        return a+b
    
def minus(a,b):
    # aware negative
    if a == None or b == None:
        return None
    else:
        return a-b

def multi(a,b):
    if a == None or b == None:
        return None
    else:
        return a*b

def divided(a,b):
    if (b == 0 and a == 0) or a == None or b == None:
        return None
    elif a == 0:
        return a/b
    elif b == 0:
        return b/a
    else:
        return a/b

def aware_negative(num1, sign, num2):
    global text
    if num1 == None:
        return None
    elif num1 >= num2:
        text = f"({text}{sign}{num2})"
    else:
        text = f"({num2}{sign}{text})"
        
def loop_func():
    #  looping user list number
    global result, user
    global text
    user_permutations = list(itertools.permutations(user,4))
    for li in range(24): # permutaions possability 4*4*4*4
        user_permu_list = list(user_permutations[li])

        # operator loop
        for i in range(4):
            for j in range(4):
                for k in range(4):

                    firstResult = func_list[i](user_permu_list[0], user_permu_list[1]) # first pair operand
                    text = f"({user_permu_list[0]}{func_sign[i]}{user_permu_list[1]})" # display solution 
                    secondResult = func_list[j](firstResult, user_permu_list[2])   # second pair operand 
                    # aware negative and None
                    aware_negative(firstResult, func_sign[j], user_permu_list[2])    
                    thirdResult = func_list[k](secondResult, user_permu_list[3]) # third pair operand
                    # aware negative
                    aware_negative(secondResult, func_sign[k], user_permu_list[3])
                        
                    result = thirdResult # final result from solution
                    print(text, "", result)
                    if result == 24:
                        return text
################################################################

text = ""
func_list = [sum_, minus, multi, divided] # list of function names
func_sign = ["+","-","*","/"]   # list of operator signs
# To display the solutions

# Start the program
while (True) : # user input awaring
    try:
        user = [int(n) for n in input("Enter 4 numbers with space: ").split()]
    except ValueError:
        print("Not a Number.")
    else:
        if len(user) != 4:
            print("Enter only 4 numbers.")
        else:
            break 

prove = loop_func() # calling function

# checking the result returning
if prove == None:
    print("There is no answer.")
else:
    print(f"The prove is {prove} = {result}.")
    
# program end