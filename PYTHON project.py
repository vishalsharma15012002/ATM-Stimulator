import tkinter as tk
from tkinter import messagebox

# ----- Account Data -----
stored_pin = "1234"
balance = 10000.0  # Starting balance


# ----- ATM Functions -----
def check_balance():
    """Show the current balance."""
    messagebox.showinfo("Balance", f"Your current balance is ₹{balance:.2f}")
    balance_label.config(text=f"💰 Balance: ₹{balance:.2f}")


def deposit_money():
    """Add money to the current balance."""
    global balance
    amount = amount_entry.get()

    if not amount:
        messagebox.showwarning("Input Error", "Please enter an amount!")
        return

    try:
        amt = float(amount)
        if amt <= 0:
            messagebox.showwarning("Invalid", "Enter a positive amount!")
        else:
            balance += amt   # <--- Updates the global balance
            messagebox.showinfo("Success",
                                f"₹{amt:.2f} deposited successfully!\nNew Balance: ₹{balance:.2f}")
            balance_label.config(text=f"💰 Balance: ₹{balance:.2f}")  # Update label
            amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter a numeric amount!")


def withdraw_money():
    """Withdraw money from the balance."""
    global balance
    amount = amount_entry.get()

    if not amount:
        messagebox.showwarning("Input Error", "Please enter an amount!")
        return

    try:
        amt = float(amount)
        if amt <= 0:
            messagebox.showwarning("Invalid", "Enter a positive amount!")
        elif amt > balance:
            messagebox.showerror("Insufficient Funds", "You don't have enough balance!")
        else:
            balance -= amt   # <--- Updates the global balance
            messagebox.showinfo("Success",
                                f"₹{amt:.2f} withdrawn successfully!\nRemaining Balance: ₹{balance:.2f}")
            balance_label.config(text=f"💰 Balance: ₹{balance:.2f}")  # Update label
            amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Enter a numeric amount!")


def logout():
    messagebox.showinfo("Goodbye", "Thank you for using Python ATM 💳")
    atm_window.destroy()
    login_screen()


# ----- Login Screen -----
def login_screen():
    def verify_login():
        pin = pin_entry.get()
        if pin == stored_pin:
            messagebox.showinfo("Welcome", "Login Successful ✅")
            login.destroy()
            main_atm_window()
        else:
            messagebox.showerror("Wrong PIN", "Incorrect PIN. Try again!")

    global login, pin_entry
    login = tk.Tk()
    login.title("Python Bank - ATM Login")
    login.geometry("300x200")
    login.config(bg="#e6f2ff")

    tk.Label(login, text="Welcome to Python Bank ATM 🏦",
             bg="#e6f2ff", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(login, text="Enter your 4-digit PIN:", bg="#e6f2ff").pack()

    pin_entry = tk.Entry(login, show="*", width=10, font=("Arial", 12))
    pin_entry.pack(pady=5)

    tk.Button(login, text="Login", width=10, bg="#4CAF50", fg="white",
              command=verify_login).pack(pady=10)

    login.mainloop()


# ----- Main ATM Menu Screen -----
def main_atm_window():
    global atm_window, amount_entry, balance_label

    atm_window = tk.Tk()
    atm_window.title("Python Bank ATM")
    atm_window.geometry("400x400")
    atm_window.config(bg="#f2ffe6")

    tk.Label(atm_window, text="ATM Main Menu",
             font=("Arial", 14, "bold"), bg="#f2ffe6").pack(pady=10)

    # Current balance label (updates live)
    balance_label = tk.Label(atm_window,
                             text=f"💰 Balance: ₹{balance:.2f}",
                             font=("Arial", 12, "bold"),
                             bg="#f2ffe6", fg="#333333")
    balance_label.pack(pady=8)

    tk.Label(atm_window, text="Enter amount:", bg="#f2ffe6").pack(pady=5)
    amount_entry = tk.Entry(atm_window, width=15, font=("Arial", 12))
    amount_entry.pack(pady=5)

    tk.Button(atm_window, text="Check Balance",
              command=check_balance, width=20,
              bg="#2196F3", fg="white").pack(pady=8)
    tk.Button(atm_window, text="Deposit Money",
              command=deposit_money, width=20,
              bg="#4CAF50", fg="white").pack(pady=8)
    tk.Button(atm_window, text="Withdraw Money",
              command=withdraw_money, width=20,
              bg="#FF9800", fg="white").pack(pady=8)

    tk.Button(atm_window, text="Exit", command=logout,
              width=10, bg="#f44336", fg="white").pack(pady=10)

    atm_window.mainloop()


# ----- Run the Program -----
login_screen()