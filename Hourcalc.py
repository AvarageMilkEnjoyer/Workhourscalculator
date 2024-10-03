import tkinter as tk
from tkinter import messagebox

def calculate_pay():
    try:
        # Get inputs from the user
        starthour = int(starthour_entry.get())
        startminutes = int(startminutes_entry.get())
        endhour = int(endhour_entry.get())
        endminutes = int(endminutes_entry.get())
        pause = int(pause_entry.get())

        # Calculate the total
        hour = endhour - starthour
        minute1 = endminutes - startminutes
        minute2 = minute1 - pause

        pay = hour * 12.5
        taxes = pay / 2

        # Prepare result message
        if minute2 < 10:
            result = f"You worked (hh:mm): {hour}:0{minute2}\n"
        else:
            result = f"You worked (hh:mm): {hour}:{minute2}\n"
        
        result += f"You earned a cool ~€{pay:.2f}, but with uncle Sam's cut you still have €{taxes:.2f} left!"
        
        # Show result in a message box
        messagebox.showinfo("Calculation Result", result)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers.")

# Create the main window
root = tk.Tk()
root.title("Work Hours Calculator")

# Create input fields
tk.Label(root, text="Start Hour:").grid(row=0, column=0)
starthour_entry = tk.Entry(root)
starthour_entry.grid(row=0, column=1)

tk.Label(root, text="Start Minutes:").grid(row=1, column=0)
startminutes_entry = tk.Entry(root)
startminutes_entry.grid(row=1, column=1)

tk.Label(root, text="End Hour:").grid(row=2, column=0)
endhour_entry = tk.Entry(root)
endhour_entry.grid(row=2, column=1)

tk.Label(root, text="End Minutes:").grid(row=3, column=0)
endminutes_entry = tk.Entry(root)
endminutes_entry.grid(row=3, column=1)

tk.Label(root, text="Pause Minutes:").grid(row=4, column=0)
pause_entry = tk.Entry(root)
pause_entry.grid(row=4, column=1)

# Create Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_pay)
calculate_button.grid(row=5, columnspan=2)

# Run the application
root.mainloop()
