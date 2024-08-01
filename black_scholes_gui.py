import tkinter as tk
from tkinter import ttk
from black_scholes import black_scholes_call, black_scholes_put

print("Starting GUI application...")

# Create the main application window
root = tk.Tk()
root.title("Black-Scholes Option Pricing Model")
root.geometry("400x300")  # Set a fixed window size

# Define and place input fields and labels using pack
frame = ttk.Frame(root, padding="10")
frame.pack(fill='both', expand=True)

ttk.Label(frame, text="Stock Price (S)").pack(pady=5)
entry_S = ttk.Entry(frame)
entry_S.pack(pady=5)

ttk.Label(frame, text="Strike Price (X)").pack(pady=5)
entry_X = ttk.Entry(frame)
entry_X.pack(pady=5)

ttk.Label(frame, text="Time to Maturity (T)").pack(pady=5)
entry_T = ttk.Entry(frame)
entry_T.pack(pady=5)

ttk.Label(frame, text="Risk-Free Rate (r)").pack(pady=5)
entry_r = ttk.Entry(frame)
entry_r.pack(pady=5)

ttk.Label(frame, text="Volatility (σ)").pack(pady=5)
entry_sigma = ttk.Entry(frame)
entry_sigma.pack(pady=5)

# Function to calculate and display option prices
def calculate_option_price():
    try:
        S = float(entry_S.get())
        X = float(entry_X.get())
        T = float(entry_T.get())
        r = float(entry_r.get())
        sigma = float(entry_sigma.get())

        call_price = black_scholes_call(S, X, T, r, sigma)
        put_price = black_scholes_put(S, X, T, r, sigma)

        label_result.config(text=f"Call Option Price: {call_price:.2f}\nPut Option Price: {put_price:.2f}")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

# Add a button to trigger the calculation
calculate_button = ttk.Button(frame, text="Calculate", command=calculate_option_price)
calculate_button.pack(pady=10)

# Label to display the results
label_result = ttk.Label(frame, text="")
label_result.pack(pady=10)

# Run the main event loop
root.mainloop()
