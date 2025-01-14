# Create window using Tkinter with two buttons with process control
import tkinter as tk

def write_text():
    print("Tkinter is easy to create GUI!")

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

text_disp = tk.Button(frame, text="Hello", command=write_text)
text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame, text="Exit", fg="green", command=parent.quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()                               

