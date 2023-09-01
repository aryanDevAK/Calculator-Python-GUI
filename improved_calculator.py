import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.math_operation = None
        self.current_number = ""
        self.result = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.result_display = tk.Entry(self.root, width=50, border=5, bg="#fff", fg="#000")
        self.result_display.grid(row=0, column=0, columnspan=4)
        
        button_texts = [
            ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('/', 2, 3, 1),
            ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('*', 3, 3, 1),
            ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('-', 4, 3, 1),
            ('0', 5, 0, 1), ('.', 5, 1, 1), ('=', 5, 2, 2), ('+', 5, 3, 1)
        ]
        
        for button_text, row, col, rowspan in button_texts:
            button = tk.Button(self.root, text=button_text, padx=30, pady=30, border=5, command=lambda t=button_text, rs=rowspan: self.on_button_click(t, rs))
            button.grid(row=row, column=col, rowspan=rowspan)
        
    def on_button_click(self, button_text, rowspan=1):
        if button_text.isdigit() or button_text == '.':
            self.current_number += button_text
            self.update_display(self.current_number)
        elif button_text in ('+', '-', '*', '/'):
            self.result = float(self.current_number)
            self.math_operation = button_text
            self.current_number = ""
        elif button_text == '=':
            if self.math_operation and self.current_number:
                second_number = float(self.current_number)
                if self.math_operation == '+':
                    self.result += second_number
                elif self.math_operation == '-':
                    self.result -= second_number
                elif self.math_operation == '*':
                    self.result *= second_number
                elif self.math_operation == '/':
                    if second_number != 0:
                        self.result /= second_number
                    else:
                        self.update_display("Error")
                        return
                self.update_display(self.result)
                self.math_operation = None
                self.current_number = str(self.result)
        
    def update_display(self, value):
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
