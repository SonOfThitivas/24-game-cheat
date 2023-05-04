import itertools

# function
def sum_(a,b):
    return a+b
def minus(a,b):
    # aware negative
    if (a-b) < 0:
        return b-a
    else:
        return a-b
    #return a-b
def multi(a,b):
    return a*b
def divided(a,b):
    return a/b

func_list = [sum_, minus, multi, divided]
func_sign = ["+","-","*","/"]

# Start     
while (True) :   
    try:
        user = int(input("Enter 4 numbers >> "))
        # user = 3737
        len(str(user)) == 4
    except Exception:
        print("Not a Number")
    else:
        break

# num variable
firstnum = user // 1000
secondnum = (user // 100) - (firstnum * 10)
thirdnum = (user // 10) - (firstnum * 100) - (secondnum * 10)
forthnum = user - (firstnum * 1000) - (secondnum * 100) - (thirdnum * 10)

user_list = [firstnum, secondnum, thirdnum, forthnum]

def loop_func():
    #  looping user list number
    global result
    text = ""
    user_permutations = list(itertools.permutations(user_list,4))
    for li in range(24): # permutaions possability
        user_permu_list = list(user_permutations[li])
        for n in range(4): #  pushing number
            # operator loop
            for i in range(4):
                for j in range(4):
                    for k in range(4):

                        firstResult = func_list[i](user_permu_list[0], user_permu_list[1])
                        text = f"({user_permu_list[0]}{func_sign[i]}{user_permu_list[1]})"
                        secondResult = func_list[j](firstResult, user_permu_list[2])
                        # aware negative
                        if firstResult >= user_permu_list[2]:
                            text = f"({text}{func_sign[j]}{user_permu_list[2]})"
                        else:
                            text = f"({user_permu_list[2]}{func_sign[j]}{text})"     

                        thirdResult = func_list[k](secondResult, user_permu_list[3])
                        # aware negative
                        if secondResult >= user_permu_list[3]:
                            text = f"{text}{func_sign[k]}{user_permu_list[3]}"
                        else:
                            text = f"{user_permu_list[3]}{func_sign[k]}{text}"   
                            
                        result = thirdResult
                        print(text, "", result)
                        if result == 24:
                            return text
            #  pushing number front-back
            user_permu_list.append(user_permu_list[0])
            user_permu_list.pop(0)
    

prove = loop_func()

if prove == None:
    print("There is no answer.")
else:
    print(f"The prove is {prove} = {result}.")