import itertools

class Possibility:
    def __init__(self, user_num):
        self.user_num = user_num
        self.text = str()
        self.op_list = [self._sum, self.minus, self.multi, self.divide]
        self.op_sign = ['+', '-', '*', '/']
        self.result = None
        self.count = 0   
    
    def compute(self):
        user_permu = list(itertools.permutations(self.user_num, 4))
        
        for pos in range(24):
            num_list = list(user_permu[pos])
            
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        self.count += 1
                        
                        self.result = self.op_list[i](num_list[0], num_list[1])
                        self.text = f"({num_list[0]}{self.op_sign[i]}{num_list[1]})"
                        
                        self.result = self.op_list[j](self.result, num_list[2])
                        self.text = f"({self.text}{self.op_sign[j]}{num_list[2]})"
                        
                        self.result = self.op_list[k](self.result, num_list[3])
                        self.text = f"({self.text}{self.op_sign[k]}{num_list[3]})"
                        
                        print(self.count, self.text, '=', self.result)
                        
                        if self.result == 24:
                            return self.text
    
    def _sum(self, n1, n2):
        try:
            result = n1 + n2
        except:
            return None
        else:
            return result
        
    def minus(self, n1, n2):
        try:
            result = n1 - n2
        except:
            return None
        else:
            return result
        
    def multi(self, n1, n2):
        try:
            result = n1 * n2
        except:
            return None
        else:
            return result
        
    def divide(self, n1, n2):
        try:
            result = n1 / n2
        except:
            return None
        else:
            return result
            
if __name__ == "__main__":
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
    
    program = Possibility(user)
    program.compute()
    print(program.count, program.text)