from GUI import *

class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        MainFrame(self.root).pack(expand=True)
        self.root.mainloop()

if __name__ == "__main__":
    MainApplication()