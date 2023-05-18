import tkinter as tk
from tkinter.filedialog import askopenfile
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root_tk = customtkinter.CTk()
root_tk.geometry("400x240")

label1 = tk.Label(root_tk, text="Uploaded Successfully!").place(
    relx=0.5, rely=0.9, anchor=tk.CENTER)
label2 = tk.Label(root_tk, text="Faild!").place(
    relx=0.5, rely=0.9, anchor=tk.CENTER)


def open_csv():
    file = askopenfile(
        parent=root_tk,
        mode='rb',
        title="Choose a file",
        filetypes=[("CSV file", "*.csv")])

    if file:
        label1
    else:
        label2


button = customtkinter.CTkButton(
    master=root_tk,
    text="Upload",
    command=open_csv)

button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root_tk.mainloop()


#  brew install python-tk
# pip install customtkinter
