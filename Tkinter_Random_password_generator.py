import random
import tkinter as tk
def generate_passwords():
    try:
        pwd_count = int(entry_pwd_count.get())
        pwd_chars = int(entry_pwd_chars.get())
        if pwd_count <= 0 or pwd_chars <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive numbers.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return
    
    password_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&"
    passwords = []

    for _ in range(pwd_count):
        pwd = ''.join(random.choice(password_characters) for _ in range(pwd_chars))
        passwords.append(pwd)
    
    # Clear previous results
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END,"Passwords:\n")

    # Insert new passwords and calculate size
    max_line_length = 0
    for i, pwd in enumerate(passwords, start=1):
        line = f" {i}. {pwd}\n"
        result_text.insert(tk.END, line)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x600")
root.config(bg="lightblue")

# Labels and entry fields
label_pwd_count = tk.Label(root, text="Number of passwords:",bg="lightyellow")
label_pwd_count.pack(pady=10)
entry_pwd_count = tk.Entry(root)
entry_pwd_count.pack(pady=5)

label_pwd_chars = tk.Label(root, text="Number of characters:",bg="lightyellow")
label_pwd_chars.pack(pady=5)
entry_pwd_chars = tk.Entry(root)
entry_pwd_chars.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords,bg="lightgreen")
generate_button.pack(pady=10)

# Text box to display generated passwords
result_text = tk.Text(root,height=20,width=50,bg="lightyellow", fg="black")  
result_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

