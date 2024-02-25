import itertools

class CalculatePossiblity:
    """
    Idea:
    1) 4 numbers as input.
    2) Create a list that contains the different position of the numbers with permutation.
    3) Take them to operate as possible (addition, subtraction, multiplication and division)
    """
    def __init__(self, list_of_num:list) -> None:
        self.ListOfNum = list_of_num
        self.ListOfEquation, self.ListOfIndex = [], []                 # contain equations and index of equations that be 24
        self.index = 0                                                   # follow the index

        for i in range(len(self.ListOfNum)):                            # convert the strings to the integers
            try:                                                        # input have to be the numbers
                self.ListOfNum[i] = int(self.ListOfNum[i])
            except:
                return "Only the integer numbers are valid."            # stop the function
            
        self.ListOfPermutation = list(set(itertools.permutations(self.ListOfNum, 4)))   # different position with the same numbers, duplicates will be taken once
        self.EncoderOperator = {                                        # convert index to the operating function                       
            0:lambda x,y: x+y,
            1:lambda x,y: x-y,
            2:lambda x,y: x*y,
            3:lambda x,y: x/y,
            4:lambda x,y: y+x,
            5:lambda x,y: y-x,
            6:lambda x,y: y*x,
            7:lambda x,y: y/x
            }
        self.EncoderOperatorToText = {                                  # convert index to the operator strings
            0:lambda x,y: f"({x}+{y})",
            1:lambda x,y: f"({x}-{y})",
            2:lambda x,y: f"({x}*{y})",
            3:lambda x,y: f"({x}/{y})",
            4:lambda x,y: f"({y}+{x})",
            5:lambda x,y: f"({y}-{x})",
            6:lambda x,y: f"({y}*{x})",
            7:lambda x,y: f"({y}/{x})"
        }
        
    def Finding24Possibility(self):
        for p in range(len(self.ListOfPermutation)):
            TextResult = ""                                             # contain the equation
            
            for i in range(8):                                          # first operating
                for j in range(8):                                      # second operating
                    for k in range(8):                                  # third operating
                        operator1, operator2, operator3 = self.EncoderOperator[i], \
                                                        self.EncoderOperator[j], \
                                                        self.EncoderOperator[k]
                        operator1Text, operator2Text, operator3Text = self.EncoderOperatorToText[i], \
                                                        self.EncoderOperatorToText[j], \
                                                        self.EncoderOperatorToText[k]
                                                        
                        try:                                            # beware the error of the mathematical
                            result = float(operator3(operator2(operator1( \
                                self.ListOfPermutation[p][0],self.ListOfPermutation[p][1]), \
                                self.ListOfPermutation[p][2]), \
                                self.ListOfPermutation[p][3]))
                        except:
                            TextResult = operator3Text(\
                                    operator2Text(\
                                    operator1Text(self.ListOfPermutation[p][0], self.ListOfPermutation[p][1]),\
                                    self.ListOfPermutation[p][2]),\
                                    self.ListOfPermutation[p][3])\
                                    + " = invalid"
                        else:
                            TextResult = operator3Text(\
                                    operator2Text(\
                                    operator1Text(self.ListOfPermutation[p][0], self.ListOfPermutation[p][1]),\
                                    self.ListOfPermutation[p][2]),\
                                    self.ListOfPermutation[p][3])\
                                    + f" = {result}"
                        
                        if TextResult not in self.ListOfEquation:               # not the duplicate equation
                            self.ListOfEquation.append(TextResult)              # take the equation to a list
                            
                            if result == 24:
                                self.ListOfIndex.append(self.index)             # collect the index of the equation that the result is 24
                        
                            self.index += 1
    
        return self.ListOfEquation, self.ListOfIndex