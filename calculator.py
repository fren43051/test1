import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self.buttons_frame, text=button, width=10, height=3, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, item):
        if item == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
            self.input_text.set(self.expression)
        elif item == 'C':
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
