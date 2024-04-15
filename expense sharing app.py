import tkinter as tk
from tkinter import messagebox

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Sharing App")
        
        self.expenses = []
        
        # Entry widgets
        tk.Label(root, text="Amount: ", font="helvetica", bg="palevioletred").grid(row=1, column=0, rowspan=2)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, rowspan=2)
        
        tk.Label(root, text="Description: ", font="helvetica", bg="palevioletred").grid(row=4, column=0, rowspan=2)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=4, column=1, rowspan=2)
        
        tk.Label(root, text="Participants (comma-separated): ", font="helvetica", bg="palevioletred").grid(row=7, column=0, rowspan=2)
        self.participants_entry = tk.Entry(root)
        self.participants_entry.grid(row=7, column=1, rowspan=2)
        
        # Buttons
        tk.Button(root, text="Add Expense", command=self.add_expense, font=('verdana', 13)).grid(row=9, column=0, columnspan=2, rowspan=2)
        tk.Button(root, text="Calculate Share", command=self.calculate_share, font=('verdana', 13)).grid(row=13, column=0, columnspan=2, rowspan=2)
        
        # Text widget to display balances
        self.balance_text = tk.Text(root, height=10, width=50)
        self.balance_text.grid(row=16, column=0, columnspan=2, rowspan=2)

    def add_expense(self):
        desc = self.desc_entry.get()
        amount = float(self.amount_entry.get())
        participants = [p.strip() for p in self.participants_entry.get().split(',')]
        expense = {"description": desc, "amount": amount, "participants": participants}
        self.expenses.append(expense)
        messagebox.showinfo("Expense Added", "Expense added successfully!")

    def calculate_share(self):
        balances = {}
        for expense in self.expenses:
            share = expense["amount"] / len(expense["participants"])
            for participant in expense["participants"]:
                balances[participant] = balances.get(participant, 0) - share
            balances[expense["participants"][0]] += expense["amount"]
        
        self.balance_text.delete("1.0", tk.END)
        self.balance_text.insert(tk.END, "Balances:\n")
        for person, balance in balances.items():
            self.balance_text.insert(tk.END, f"{person}: ${balance:.2f}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseApp(root)
    root.mainloop()