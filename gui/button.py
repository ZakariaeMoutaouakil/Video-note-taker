import tkinter as tk

ON = "Stop recording"
OFF = "Start recording"
BUTTON_COLORS = {
    ON: ("#FF6347", "#FFFFFF"),  # Red when ON
    OFF: ("#32CD32", "#000000")  # Green when OFF
}


def change_button_text(button):
    if button.cget("text") == OFF:
        button.config(text=ON, bg=BUTTON_COLORS[ON][0], fg=BUTTON_COLORS[ON][1])
    else:
        button.config(text=OFF, bg=BUTTON_COLORS[OFF][0], fg=BUTTON_COLORS[OFF][1])


def run_gui():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Record Audio")

    # Create a button widget
    button = tk.Button(root, text=OFF, command=lambda: change_button_text(button))
    button.config(
        font=("Helvetica", 14),  # Set font size and family
        relief=tk.RAISED,  # Button relief style
        padx=20, pady=10  # Add padding
    )
    button.pack(pady=20)

    # Set initial button colors
    button.config(bg=BUTTON_COLORS[OFF][0], fg=BUTTON_COLORS[OFF][1])

    # Run the Tkinter event loop
    root.mainloop()
