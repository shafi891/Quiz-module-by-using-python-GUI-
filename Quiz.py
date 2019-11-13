from tkinter import *
import tkinter as tk
#from tkinter import messagebox


def save_info():
    name_info = name.get()
    reg_info = reg.get()
    reg_info = str(reg_info)
    sec_info = sec.get()
    print(name_info , reg_info , sec_info)

    file = open("project.txt", "w")
    file.write(name_info +" ")
    file.write(reg_info+ " ")
    file.write(sec_info+" ")
    file.close()
    print("Thankyou", name_info, "Your submittion is done successfully")
    master.destroy()


#f = open("Save.py", "w")
#f.write("Name = " + str() + "\n")
#f.write("Registration no:" + str() + "\n")
#f.close()

master = Tk()
master.title('Registration')
tk = LabelFrame(master, bg='teal', height=400, width=500)
tk.propagate(0)
tk.pack()
name = StringVar()
reg = IntVar()
sec = StringVar()

name_text = Label(text='Enter your name', width=19)
reg_text = Label(text='Enter your Registration no', width=19)
sec_text = Label(text='Enter your section', width=19)

e1 = Entry(tk, textvariable=name, width=25, fg='blue', bg='yellow', font=('Arial', 12))
e2 = Entry(tk, textvariable=reg, width=25, fg='blue', bg='yellow', font=('Arial', 14))
e3 = Entry(tk, textvariable=sec, width=25, fg='blue', bg='yellow', font=('Arial', 14))
e4 = Entry(tk, width=25, fg='blue', bg='yellow', font=('Arial', 14))

name_text.place(x=2, y=10)
reg_text.place(x=2, y=50)
sec_text.place(x=2, y=90)

e1.place(x=190, y=10)
e2.place(x=190, y=50)
e3.place(x=190, y=90)
tk.propagate(0)
tk.pack()
#def showMsg():
 #  messagebox.showinfo('hey !! your submittion is done')
  # f=Frame(master,bg='teal', height=600, width=500)
   #f.propagate(0)
   #f.pack()
submit = Button(text="Submit", width=25, fg='blue', font=('Arial', 18), command= save_info)
submit.place(x=150, y=250)
submit.place()
master.resizable(0, 0)

master.mainloop()

import numpy as np

# keep the question in a separate json file
q = [
    "What is the output of the following?print('my_string'.isidentifier()",
    "What is the output of following statement : 'a''+'bc'",
    "What is the output of the following? print(''' \tfoo'''.lstrip())",
    "Given a string example=”hello” what is the output of example.count(‘l’)",

]

options = [
    ["True", "False", "None", "Error"],
    ["a", "bc", "bca", "abc"],
    ["/tfoo", "foo", "/foo", "none of the mentioned"],
    ["2", "1", "none", 0]
]

a = [1, 4, 2, 1]



class Quiz:
    def __init__(self, master):
        self.count=0
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
       #self.button = Button(master, text="Back", width=20, command=self.back_btn)
        #self.button.pack(side=BOTTOM)
        self.button = Button(master, bg='yellow',text="Next",width=20, command=self.next_btn)
        self.button1 = Button(master, text='End', width=20,command= root.destroy)
        self.button1.pack()
        self.button1.place(x= 170, y= 250)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val + 1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(q))

    def next_btn(self):
        if self.check_q(self.qn):
            self.count= self.count+1
            print("Correct, your points is {}".format(self.count))
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
        else:
            self.display_q(self.qn)


root = Tk()
root.geometry("500x300")
root.title("Question")
app = Quiz(root)
root.mainloop()
