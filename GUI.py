import tkinter as tk
from Calculate_Possiblity import CalculatePossiblity
# ref: https://stackoverflow.com/a/17470842

class LeftFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.Frame_Input = tk.Frame(self)
        # collect entry widgets in a list
        self.Input_Num = [tk.Entry(self.Frame_Input, font=("Angsana New", 25), width=5, justify="center") for _ in range(4)]
        # define them to be the entry widgets
        for i in range(len(self.Input_Num)):
            self.Input_Num[i].grid(row=0, column=i, padx=2, pady=2)
        
        tk.Label(self, text="Enter the integers to find possibilty of equations.", font=("Angsana New", 25)).pack()
        self.Frame_Input.pack()
        tk.Button(self, text="Calculate", font=("Angsana New", 25), command=self.parent.CheckInputValue).pack(pady=20)

class RightFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        tk.Label(self, text="The Results", font=("Angsana New", 25)).pack()
        self.Result_Frame = tk.Frame(self)
        self.Scroll_Bar = tk.Scrollbar(self.Result_Frame) # ref: https://www.askpython.com/python-modules/tkinter/tkinter-text-widget-tkintscrollbar
        self.Scroll_Bar.pack(side="right", fill='y') # ref: https://www.geeksforgeeks.org/scrollable-frames-in-tkinter/
        self.Text_Box = tk.Text(self.Result_Frame, font=("Angsana New", 18), width=40, height=20, state="disabled", padx=5, pady=5, yscrollcommand=self.Scroll_Bar.set)
        self.Scroll_Bar.config(command=self.Text_Box.yview)
        self.Text_Box.pack()
        self.Result_Frame.pack()

class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.Left_Frame = LeftFrame(self)
        self.Right_Frame = RightFrame(self)
        
        self.Left_Frame.grid(row=0, column=0, padx=10, pady=10)
        self.Right_Frame.grid(row=0, column=1, padx=10, pady=10)
        
    def CheckInputValue(self):
        self.Right_Frame.Text_Box.configure(state="normal")
        self.Right_Frame.Text_Box.delete("1.0","end")
        self.Right_Frame.Text_Box.configure(state="disabled")
        
        ListOfNum = []
        for i in range(4):
            if isinstance(self.Left_Frame.Input_Num[i].get(), float):
                self.Right_Frame.Text_Box.configure(state="normal")
                self.Right_Frame.Text_Box.insert("end", "Please, enter only the integers.\n")
                self.Right_Frame.Text_Box.configure(state="disabled")
                self.Right_Frame.Text_Box.see("end")
                return
            
            try:
                ListOfNum.append(  \
                    int(self.Left_Frame.Input_Num[i].get())
                    )
            except:
                self.Right_Frame.Text_Box.configure(state="normal")
                self.Right_Frame.Text_Box.insert("end", "Please, enter only the integers.\n")
                self.Right_Frame.Text_Box.configure(state="disabled")
                self.Right_Frame.Text_Box.see("end")
                return
            
        self.Calculate(ListOfNum)
        
    def Calculate(self, ListOfNum):
        obj = CalculatePossiblity(ListOfNum)
        ListOfEquation, ListOfIndex24 = obj.Finding24Possibility()
        
        self.Right_Frame.Text_Box.configure(state="normal")
        
        self.Right_Frame.Text_Box.insert("end", f"Results: {len(ListOfIndex24):,}\nEquations: {len(ListOfEquation):,}\n")   
        self.Right_Frame.Text_Box.insert("end", "--------------------------------------------\n")             
        self.Right_Frame.Text_Box.insert("end", "\nThe results:\n")
        
        for i in ListOfIndex24:
            self.Right_Frame.Text_Box.insert("end", f"{i+1:,}) {ListOfEquation[i]}\n")
        
        self.Right_Frame.Text_Box.insert("end", "--------------------------------------------\n")             
        self.Right_Frame.Text_Box.insert("end", "\nAll of equations:\n")
        
        for e in range(len(ListOfEquation)):
            self.Right_Frame.Text_Box.insert("end", f"{e+1:,}) {ListOfEquation[e]}\n")
    
        self.Right_Frame.Text_Box.configure(state="disabled")
        