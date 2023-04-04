#Testing how progress bars are made with tkinter
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=10)

progress_bar = tk.Canvas(root, width=20, height=200, bg='white')
progress_bar.create_rectangle(0, 0, 20, 0, fill='green', width=0)
progress_bar.pack(pady=10)

scale = tk.Scale(root, from_=0, to=100, orient=tk.VERTICAL, length=200)
scale.pack(pady=10)


def update_progress_bar(val):
    progress_bar_height = int(float(val) / 100 * 200)
    progress_bar.coords(1, 0, 200 - progress_bar_height, 20, 200)


scale.set(50)

scale.config(command=update_progress_bar)

root.mainloop()
