import tkinter as tk
from tkinter import messagebox
import csv

def register_user():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    country = country_var.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password, gender, country])

    messagebox.showinfo("Success", "Registration successful!")
    clear_form()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    gender_var.set(None)
    country_var.set("Select Country")

# Create main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x400")

# Name
tk.Label(root, text="Full Name").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()

# Email
tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()

# Password
tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, width=40, show="*")
entry_password.pack()

# Gender
tk.Label(root, text="Gender").pack(pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Country dropdown
tk.Label(root, text="Country").pack(pady=5)
country_var = tk.StringVar()
country_var.set("Select Country")
countries = ["India", "USA", "UK", "Canada", "Australia"]
tk.OptionMenu(root, country_var, *countries).pack()

# Register button
tk.Button(root, text="Register", command=register_user).pack(pady=20)

# Run the app
root.mainloop()
