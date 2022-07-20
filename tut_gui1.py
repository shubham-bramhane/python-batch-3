# # # #  gui stands for graphical user interface 


# # # import tkinter

# # # # window=tkinter.Tk()

# # # # window.title("Demo")

# # # # label=tkinter.Label(text="shubham")

# # # # menu=tkinter.Menu(window)

# # # # window.config(menu=menu)

# # # # filemenu=tkinter.Menu(menu)
# # # # editmenu=tkinter.Menu(menu)

# # # # menu.add_cascade(label="File",menu=filemenu)
# # # # menu.add_cascade(label="Edit",menu=editmenu)
# # # # menu.add_cascade(label="Selection")
# # # # menu.add_cascade(label="View")
# # # # menu.add_cascade(label="Go")
# # # # menu.add_cascade(label="Run")
# # # # menu.add_cascade(label="Terminal")
# # # # menu.add_cascade(label="Help")

# # # # filemenu.add_command(label="New",command=window.quit)
# # # # filemenu.add_command(label="Open..")
# # # # filemenu.add_separator()
# # # # # menu.add_cascade('Exit',command=window.quit)
# # # # filemenu.add_command(label="Exit",command=window.quit)




# # # # editmenu.add_command(label="Undo")
# # # # editmenu.add_command(label="Redo")
# # # # editmenu.add_separator()
# # # # editmenu.add_command(label="cut")
# # # # editmenu.add_command(label="copy")
# # # # editmenu.add_command(label="paste")



# # # window=tkinter.Tk()
# # # tkinter.Label(window,text="first name").grid(row=0)
# # # tkinter.Label(window,text="last name").grid(row=1)
# # # e1=tkinter.Entry(window)
# # # e2=tkinter.Entry(window)

# # # e1.grid(row=0,column=1)
# # # e2.grid(row=1,column=1)



# # # # label.pack()
# # # window.mainloop()





# # from tkinter import *
# # from tkinter import ttk
# # root = Tk()
# # frm = ttk.Frame(root, padding=10)
# # frm.grid()
# # ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# # root.mainloop()




# import tkinter as tk

# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()

#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()

#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("hello i am shubham")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents

#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)

#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())

# root = tk.Tk()
# myapp = App(root)
# myapp.mainloop()




from tkinter import *


window=Tk()


window.mainloop()