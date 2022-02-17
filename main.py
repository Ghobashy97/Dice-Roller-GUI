import tkinter as tk
import numpy as np


def create_gui():
    root = tk.Tk()
    root.title("Roll the Bones!")
    # root.geometry("200x150")

    panel1 = tk.PanedWindow(root)
    panel1.pack(side='top')
    label1 = tk.Label(panel1, font=('Comic Sans', 48))

    # label1.grid(column=1, row=2)
    # label1.pack()

    def roll_da_bonez():
        label1.config(text=f'{np.random.randint(1,6)} | {np.random.randint(1,6)}')
        label1.pack(side='top')

    button1 = tk.Button(panel1, text="ROLL THE BONES!", command=roll_da_bonez)
    button1.pack()
    # button1.grid(column=1, row=1)

    root.mainloop()


create_gui()
