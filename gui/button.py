import tkinter as tk


def change_button_text(button):
    if button.cget("text") == "Click me!":
        button.config(text="Clicked!")
    else:
        button.config(text="Click me!")


def run_gui():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Button Text Changer")

    # Create a button widget
    button = tk.Button(root, text="Click me!", command=lambda: change_button_text(button))
    button.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()
