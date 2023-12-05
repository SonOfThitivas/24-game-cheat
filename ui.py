from tkinter import Tk, Label, Frame, Entry, Button, Text, Scrollbar
from new import Possibility

class Gui:
    def __init__(self):
        self.wn = Tk()
        self.wn.title("24 Game Cheat")
        self.create_widget()
        
    def create_widget(self):
        self.left_frame = Frame(self.wn, height=500, width=500)
        Label(self.left_frame, text="Enter the numbers in the blanks", font=("Calibri", 36)).pack(pady=5)
        self.entry_frame = Frame(self.left_frame)
        self.ent1 = Entry(self.entry_frame, font=("Calibri", 36), width=3, justify="center")
        self.ent2 = Entry(self.entry_frame, font=("Calibri", 36), width=3, justify="center")
        self.ent3 = Entry(self.entry_frame, font=("Calibri", 36), width=3, justify="center")
        self.ent4 = Entry(self.entry_frame, font=("Calibri", 36), width=3, justify="center")
        self.ent1.grid(row=0, column=0, padx=5)
        self.ent2.grid(row=0, column=1, padx=5)
        self.ent3.grid(row=0, column=2, padx=5)
        self.ent4.grid(row=0, column=3, padx=5)
        self.entry_frame.pack(padx=10, pady=10)
        Button(self.left_frame, text="Submit", font=("Calibri", 24), background="light green").pack(pady=5)
        Button(self.left_frame, text="Reset", font=("Calibri", 24), background="yellow").pack(pady=5)
        
        self.mid_frame = Frame(self.wn, height=500, width=500)
        
        
        self.right_frame = Frame(self.wn, height=500, width=500)
        text_frame = Frame(self.right_frame)
        scroll_bar = Scrollbar(text_frame)
        scroll_bar.pack(side="right", fill='y')
        self.text_area = Text(text_frame, font=("Calibri", 16), state="disabled", padx=10, pady=10, yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.text_area.yview) 
        self.text_area.pack()
        text_frame.pack()
        
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)
        self.mid_frame.grid(row=0, column=1, padx=10, pady=10)
        self.right_frame.grid(row=0, column=2, padx=10, pady=10)
    
    def mainloop(self):
        self.wn.mainloop()
        
if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()