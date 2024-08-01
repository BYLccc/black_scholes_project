import tkinter as tk
from tkinter import ttk

def minimal_example():
    print("Creating root window")
    root = tk.Tk()
    root.title("Minimal Tkinter Example")
    root.geometry("400x300")
    print("Root window created")

    label = ttk.Label(root, text="This is a test label")
    label.pack(pady=20)
    print("Label packed")

    root.mainloop()
    print("Main loop running")

if __name__ == "__main__":
    print("Starting minimal example")
    minimal_example()
    print("Minimal example started")
