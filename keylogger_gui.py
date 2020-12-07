from tkinter import *

root = Tk()

root.title("Hack points boutiques")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
e.insert(0, "Ton nom de compte : ")

p = Entry(root, width = 35, borderwidth = 5)
p.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)
p.insert(0, "Ton mot de passe : ")

s = Entry(root, width = 35, borderwidth = 5)
s.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 10)
s.insert(0, "Ta réponse secrète : ")

def openNewWindow():
    newWindow = Toplevel(root)

    Label(newWindow, text ="Ton compte a été crédité en points boutiques !").pack()

    label = Label(root, text ="Ton compte a été crédité en points boutiques !") 
    label.pack

    def click_ok():
        label_ok = Label(root, text ="Ok")
        root.destroy()

    button_ok = Button(newWindow, text="Ok", command = click_ok, padx = 25, pady = 10)
    button_ok.pack()

button_1 = Button(root, text="100 PB", padx = 50, pady = 20, fg = "#ffffff", bg = "#123456", command = openNewWindow)
button_2 = Button(root, text="1000 PB", padx = 50, pady = 20, fg = "#ffffff", bg = "#123456", command = openNewWindow)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)

root.mainloop()