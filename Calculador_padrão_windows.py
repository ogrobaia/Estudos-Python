import tkinter as tk


def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")


def button_click(symbol):
    entry.insert(tk.END, symbol)


def clear_entry():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (symbol, row, column) in buttons:
    btn = tk.Button(root, text=symbol, padx=20, pady=10,
                    command=lambda sym=symbol: button_click(sym))
    btn.grid(row=row, column=column)

clear_btn = tk.Button(root, text='C', padx=20, pady=10, command=clear_entry)
clear_btn.grid(row=5, column=0, columnspan=2)

equal_btn = tk.Button(root, text='=', padx=20, pady=10,
                      command=evaluate_expression)
equal_btn.grid(row=5, column=2, columnspan=2)

root.mainloop()
