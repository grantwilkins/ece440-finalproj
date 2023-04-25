import tkinter as tk
import lights_client

def button_click(button_num):
    lights_client.toggle_lights("gfwilki", button_num)

# create the main window
root = tk.Tk()
root.title("Button GUI")

# set window size and background color
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# create a label at the top of the window
title_label = tk.Label(root, text="Button GUI", font=("Arial", 24), bg="#f2f2f2")
title_label.pack(pady=20)

# create the buttons
button1 = tk.Button(root, text="Lights 1", font=("Arial", 16), command=lambda: button_click(1))
button2 = tk.Button(root, text="Lights 2", font=("Arial", 16), command=lambda: button_click(2))
button3 = tk.Button(root, text="Lights 3", font=("Arial", 16), command=lambda: button_click(3))


# add the buttons to the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# start the main event loop
root.mainloop()
