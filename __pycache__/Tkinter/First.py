import tkinter as tk
# m = tk.Tk()
# label = tk.Label(m,text="Hello My Lable").pack()
# m.mainloop()

text1 = tk.Tk()
text1.geometry('200x200')
label = tk.Label(text1,text="Email").grid(row=0,column=1)
i1 = tk.Entry(text1,)