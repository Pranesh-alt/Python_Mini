import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def initialize_db():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT DEFAULT (DATE('now'))
        )
     """)
    connection.commit()
    return connection

connection = initialize_db()


def add_expense():
    def save_expense():
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO expenses (amount, category, description) 
            VALUES (?, ?, ?)
        """, (amount, category, description))
        # connection.commit()
        messagebox.showinfo("Success", "Expense added successfully!")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Expense")
    tk.Label(add_window, text="Amount:").grid(row=0, column=0)
    amount_entry = tk.Entry(add_window)
    amount_entry.grid(row=0, column=1)
    tk.Label(add_window, text="Category:").grid(row=1, column=0)
    category_entry = tk.Entry(add_window)
    category_entry.grid(row=1, column=1)
    tk.Label(add_window, text="Description:").grid(row=2, column=0)
    description_entry = tk.Entry(add_window)
    description_entry.grid(row=2, column=1)
    tk.Button(add_window, text="Save", command=save_expense).grid(row=3, columnspan=2)

def view_expenses():
    view_window = tk.Toplevel(root) 
    view_window.title("View Expenses")

    tree = ttk.Treeview(view_window, columns=("ID", "Amount", "Category", "Description", "Date"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Amount", text="Amount")
    tree.heading("Category", text="Category")
    tree.heading("Description", text="Description")
    tree.heading("Date", text="Date")
    tree.pack(fill="both", expand=True)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

    tk.Button(view_window, text="Close", command=view_window.destroy).pack(pady=10)


def delete_expense():
    def confirm_delete():
        expense_id = expense_id_entry.get()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        connection.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Expense deleted successfully!")
        else:
            messagebox.showwarning("Not Found", "Expense ID not found.")
        delete_window.destroy()

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Expense")

    tk.Label(delete_window, text="Enter Expense ID to delete:").grid(row=0, column=0)
    expense_id_entry = tk.Entry(delete_window)
    expense_id_entry.grid(row=0, column=1)

    tk.Button(delete_window, text="Delete", command=confirm_delete).grid(row=1, columnspan=2)

def edit_expense():
    def load_expense():
        expense_id = expense_id_entry.get()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
        expense = cursor.fetchone()

        if expense:
            amount_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            description_entry.delete(0, tk.END)

            amount_entry.insert(0, expense[1])  
            category_entry.insert(0, expense[2])  
            description_entry.insert(0, expense[3]) 
        else:
            messagebox.showwarning("Not Found", "Expense ID not found.")

    def save_changes():
        expense_id = expense_id_entry.get()
        new_amount = float(amount_entry.get())
        new_category = category_entry.get()
        new_description = description_entry.get()

        cursor = connection.cursor()
        cursor.execute("""
            UPDATE expenses
            SET amount = ?, category = ?, description = ?
            WHERE id = ?
        """, (new_amount, new_category, new_description, expense_id))
        connection.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Expense updated successfully!")
            edit_window.destroy()
        else:
            messagebox.showwarning("Error", "Failed to update expense.")

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Expense")

    tk.Label(edit_window, text="Expense ID:").grid(row=0, column=0)
    expense_id_entry = tk.Entry(edit_window)
    expense_id_entry.grid(row=0, column=1)

    tk.Button(edit_window, text="Load Expense", command=load_expense).grid(row=0, column=2)

    tk.Label(edit_window, text="New Amount:").grid(row=1, column=0)
    amount_entry = tk.Entry(edit_window)
    amount_entry.grid(row=1, column=1)

    tk.Label(edit_window, text="New Category:").grid(row=2, column=0)
    category_entry = tk.Entry(edit_window)
    category_entry.grid(row=2, column=1)

    tk.Label(edit_window, text="New Description:").grid(row=3, column=0)
    description_entry = tk.Entry(edit_window)
    description_entry.grid(row=3, column=1)

    tk.Button(edit_window, text="Save Changes", command=save_changes).grid(row=4, columnspan=3)


root = tk.Tk()
root.title("Expense Tracker")


tk.Label(root, text="Expense Tracker", font=("Arial", 20)).pack(pady=10)
tk.Button(root, text="Add Expense", command=add_expense, width=20).pack(pady=5)
tk.Button(root, text="View Expenses", command=view_expenses, width=20).pack(pady=5)
tk.Button(root, text="Edit Expense", command=edit_expense, width=20).pack(pady=5)
tk.Button(root, text="Delete Expense", command=delete_expense, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

root.mainloop()