import tkinter as tk

btn_content = ['1', '2', '3', '-', '4', '5', '6', '+', '7', '8', '9', '*', 'Clear', '0', '=', '/']
root = tk.Tk()
root.title("Моя программа")
root.geometry("800x500")

label = tk.Label(root, text="Калькулятор", font=("Comic Sans MS", 18))
label.pack(padx=20, pady=20)
textbox = tk.Text(root, height=3, font=("Comic Sans MS", 16))
textbox.pack(padx=0, pady=2)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

for y in range(4):
    for x in range(4):
        btn = tk.Button(buttonFrame, text=btn_content[x+y*4], font=("Comic Sans MS", 18))
        btn.grid(row=f'{y}', column=f'{x}', sticky="we")

buttonFrame.pack(fill="x")
root.mainloop()