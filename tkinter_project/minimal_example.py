import tkinter as tk

def basic_example():
    print("Creating root window")
    root = tk.Tk()
    root.title("Basic Tkinter Example")
    root.geometry("400x300")
    print("Root window created")

    label = tk.Label(root, text="This is a test label", bg="yellow", fg="black")
    label.pack(pady=20)
    print("Label packed")

    root.mainloop()
    print("Main loop running")

if __name__ == "__main__":
    print("Starting basic example")
    basic_example()
    print("Basic example started")
