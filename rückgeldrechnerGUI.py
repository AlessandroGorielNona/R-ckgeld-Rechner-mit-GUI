import tkinter as tk

def calculate_change():
    try:
        amount_due = float(amount_due_entry.get())
        cash_received = float(cash_received_entry.get())
        change = cash_received - amount_due
        if change < 0:
            change_label.config(text="Warning: Insufficient payment", fg="red")
        else:
            change_label.config(text=f"Change: {change}", fg="black")
    except ValueError:
        change_label.config(text="Invalid input", fg="red")

root = tk.Tk()
root.title("Change Calculator")

amount_due_label = tk.Label(root, text="Amount Due:")
amount_due_label.grid(row=0, column=0)
amount_due_entry = tk.Entry(root)
amount_due_entry.grid(row=0, column=1)

cash_received_label = tk.Label(root, text="Cash Received:")
cash_received_label.grid(row=1, column=0)
cash_received_entry = tk.Entry(root)
cash_received_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_change)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

change_label = tk.Label(root, text="Change:")
change_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
