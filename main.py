import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
import pyperclip

# Function to generate password
def generate_password():
    length = length_var.get()
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()
    exclude_chars = exclude_var.get()

    if length < 4:
        messagebox.showerror("Error", "Password length must be at least 4 characters.")
        return

    # Define character pools
    char_pool = ""
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation

    # Exclude unwanted characters
    if exclude_chars:
        char_pool = ''.join(c for c in char_pool if c not in exclude_chars)

    if not char_pool:
        messagebox.showerror("Error", "No characters available for password generation.")
        return

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))

    # Ensure password contains at least one character from each selected category
    if include_upper:
        password = replace_random_char(password, random.choice(string.ascii_uppercase))
    if include_lower:
        password = replace_random_char(password, random.choice(string.ascii_lowercase))
    if include_digits:
        password = replace_random_char(password, random.choice(string.digits))
    if include_symbols:
        password = replace_random_char(password, random.choice(string.punctuation))

    # Display password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Replace a random character in the password
def replace_random_char(password, char):
    password_list = list(password)
    index = random.randint(0, len(password_list) - 1)
    password_list[index] = char
    return ''.join(password_list)

# Copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x500")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Advanced Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password length
length_label = tk.Label(root, text="Password Length:", font=("Arial", 12))
length_label.pack()
length_var = tk.IntVar(value=12)
length_spinbox = tk.Spinbox(root, from_=4, to=100, textvariable=length_var, font=("Arial", 12))
length_spinbox.pack(pady=5)

# Options for character inclusion
options_frame = tk.Frame(root)
options_frame.pack(pady=10)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

upper_check = tk.Checkbutton(options_frame, text="Include Uppercase", variable=upper_var, font=("Arial", 10))
lower_check = tk.Checkbutton(options_frame, text="Include Lowercase", variable=lower_var, font=("Arial", 10))
digits_check = tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var, font=("Arial", 10))
symbols_check = tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var, font=("Arial", 10))

upper_check.grid(row=0, column=0, padx=5, pady=5, sticky="w")
lower_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
digits_check.grid(row=0, column=1, padx=5, pady=5, sticky="w")
symbols_check.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Exclude characters
exclude_label = tk.Label(root, text="Exclude Characters:", font=("Arial", 12))
exclude_label.pack()
exclude_var = tk.StringVar()
exclude_entry = tk.Entry(root, textvariable=exclude_var, font=("Arial", 12))
exclude_entry.pack(pady=5)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white")
generate_button.pack(pady=10)

# Password display
password_label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
password_label.pack()
password_entry = tk.Entry(root, font=("Arial", 12), justify="center")
password_entry.pack(pady=5)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="blue", fg="white")
copy_button.pack(pady=10)

# Run the application
root.mainloop()
