import tkinter as tk

root = tk.Tk()
root.resizable(0, 0)
root.title('Text Widget Example')
root.config(bg='#d9d9d9')

text = tk.Text(root, height=8, bg='white', fg='black')
text.insert('1.0', 'This is a Text widget demo.')
text.pack(padx=5, pady=5)

root.mainloop()