# function
def sum_(a,b):
    return a+b
def minus(a,b):
    if (a-b) < 0:
        return b-a
    else:
        return a-b
def multi(a,b):
    return a*b
def divided(a,b):
    if (a%b) == 0:
        return a//b
    elif (b%a) == 0:
        return b//a
    else:
        return 0

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
# cloneUser_list = user_list

# aware same num
same_dict = {}
sawTheSame = 0
# mostSame = 0
class IfSameNum:

    def __init__ (self, user_list):
        self.user_list = user_list
        self.sawPair = 0
        for num in self.user_list:
            if self.user_list.count(num) == 2: # see a pair
                self.sawPair += 1 # when see some pair
                if (self.user_list[3] == num) and (self.sawPair == 1): # last number and see one pair
                    return self.OnePair(self)
                elif (self.user_list[3] == num) and (self.sawPair == 2): # last number and see two pair
                    return self.TwoPair(self)
            elif (self.user_list.count(num) == 3) and (self.sawPair == 1): # see kind of three
                return self.KindOfThree(self);
            elif (self.user_list.count(num) == 4): # forth 
                return num
            else: # nothing
                return []
            
    
    def OnePair(self: user_list):
        for i in range(9):
            count = user_list.count(i)
            if count == 2:
                return [i]
    
    def TwoPair(self: user_list):
        firstPair = None
        secondPair = None
        for i in range(9):
            count = user_list.count(i)
            if firstPair == None:
                if count == 2:
                    firstPair = i
            elif secondPair == None:
                if count == 2:
                    secondPair = i
        return [firstPair,secondPair]
    
    def KindOfThree(self: user_list):
        for i in range(9):
            count = user_list.count(i)
            if count == 3:
                return [i]
        
# for n in range(4):
#     num = user_list[n]
#     count = user_list.count(num)
#     if count > 1:
#         same_dict["num{0}".format(n)] = SameNum(num, count)
#         sawTheSame += 1

# for v in same_dict.values:
#     if v > mostSame :
#         mostSame = v

# # condition the same number
# def isSameNum(p, q):
#     if user_list[p] == user_list[q]:
#         return True

#loop calculate        
# def loop_func():
#     # choosing operator
#     result = 0
#     text = ""
#     for i in range(4):
#         for j in range(4):
#             for k in range(4):
#                 # choosing number
#                 for a in range(4):
#                     for b in range(3):
#                         for c in range(2):
#                            for d in range(1):
#                                     #1
#                                     firstResult = func_list[i](cloneUser_list[a], cloneUser_list[b])
#                                     text += f"{cloneUser_list[a]}{func_sign[i]}{cloneUser_list[b]}"
#                                     cloneUser_list.pop(a)
#                                     cloneUser_list.pop(b)
#                                     #2
#                                     secondResult = func_list[j](firstResult,cloneUser_list[c])
#                                     text += f"{func_sign[j]}{cloneUser_list[c]}"
#                                     cloneUser_list.pop(c)
#                                     #3
#                                     thirdResult = func_list[k](secondResult, cloneUser_list[d])
#                                     text += f"{func_sign[k]}{cloneUser_list[d]}"
#                                     cloneUser_list.pop(d)
#                                     result = thirdResult
#                                     if result == 24:
#                                         return text
#                                     print(text)
#                                     text = ""
#                                     cloneUser_list = user_list
                                    
def loop_func():
    # choosing operator
    result = 0
    text = ""
    for i in range(4):
        for j in range(4):
            for k in range(4):
                # choosing number
                for a in range(4):
                    for b in range(3):
                        for c in range(2):
                           for d in range(1): 
                                    firstResult = func_list[i](user_list[a], user_list[b])
                                    text += f"{user_list[a]}{func_sign[i]}{user_list[b]}"
                                    secondResult = func_list[j](firstResult, user_list[c])
                                    text += f"{func_sign[j]}{user_list[c]}"
                                    thirdResult = func_list[k](secondResult, user_list[d])
                                    text += f"{func_sign[k]}{user_list[d]}"
                                    result = thirdResult
                                    if result == 24:
                                        return text
                                    print(text)
                                    text = ""

result = loop_func()
    
print(f"The prove is {result}")