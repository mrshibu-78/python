import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store user data
USER_FILE = "users.csv"

# Create file if it doesn't exist
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Password"])  # header

# Register user function
def register_user():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Check if email already exists
    with open(USER_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if email == row[1]:
                messagebox.showerror("Error", "Email already registered!")
                return

    with open(USER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password])
    
    messagebox.showinfo("Success", "Registration successful!")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Login user function
def login_user():
    email = entry_login_email.get()
    password = entry_login_password.get()

    with open(USER_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            if email == row[1] and password == row[2]:
                messagebox.showinfo("Success", f"Welcome, {row[0]}!")
                return

    messagebox.showerror("Failed", "Invalid email or password")

# Main window
root = tk.Tk()
root.title("Login & Registration Form")
root.geometry("400x500")

# Registration Section
tk.Label(root, text="Register", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Full Name").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=30)
entry_email.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

tk.Button(root, text="Register", command=register_user, bg="green", fg="white").pack(pady=10)

# Separator
tk.Label(root, text="").pack()
tk.Label(root, text="----------------------------").pack()
tk.Label(root, text="").pack()

# Login Section
tk.Label(root, text="Login", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Email").pack()
entry_login_email = tk.Entry(root, width=30)
entry_login_email.pack()

tk.Label(root, text="Password").pack()
entry_login_password = tk.Entry(root, width=30, show="*")
entry_login_password.pack()

tk.Button(root, text="Login", command=login_user, bg="blue", fg="white").pack(pady=10)

root.mainloop()
