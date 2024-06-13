# TODO: Change this all to be a class which is ran by the main.py file.


import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



root = ctk.CTk()
root.geometry("800x400")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

frame1 = ctk.CTkFrame(root, )
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame2 = ctk.CTkFrame(root)
frame2.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

frame3 = ctk.CTkFrame(root)
frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


root.mainloop()