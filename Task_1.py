import tkinter as tk

root = tk.Tk()
root.title("Моя программа")
root.geometry("800x500")
label = tk.Label(root, text="Hello world!", font=("Times New Roman", 18))
label.pack(padx=20, pady=20)
textbox = tk.Entry(root, font=("Comic Sans MS", 16))
textbox.pack(padx=20, pady=20)
root.mainloop()

