import tkinter as tk
from tkinter import simpledialog
import numpy as np


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x700')
        self.title('Calculator By Yash Bajaj')

    def statusbar(self):
        self.status = tk.StringVar()
        self.status.set('Ready...')
        self.sbar = tk.Label(self, textvariable=self.status, relief=tk.SUNKEN)
        self.sbar.pack(fill=tk.X, side=tk.BOTTOM, anchor='w')

    def InstructionsBar(self):
        self.status = tk.StringVar()
        self.status.set('** is for square, *** is for cube, // is for square root, /// is for cube root')
        self.sbar = tk.Label(self, textvariable=self.status, relief=tk.SUNKEN)
        self.sbar.pack(fill=tk.X, side=tk.BOTTOM, anchor='w')

    def entrybox(self):
        self.scvalue = tk.StringVar()
        self.scvalue.set('')
        self.screeen = tk.Entry(self, textvariable=self.scvalue, font='oswald 30')
        self.screeen.pack()

    def buttons(self):
        def cilck(event):
            text = event.widget.cget('text')
            
            if text == '=':
                if self.scvalue.get().isdigit():
                    self.value = int(self.scvalue.get())
                else:
                    try:
                        self.value = eval(self.screeen.get())

                    except Exception as e:
                        print(e)
                        self.value = "Error"


                self.scvalue.set(self.value)
                self.screeen.update()
            elif text == 'C':
                self.scvalue.set('')
                self.screeen.update()

            elif text == '//':
                self.sqrtval = float(np.sqrt(self.scvalue.get()))
                self.scvalue.set(self.sqrtval)
                self.screeen.update()

            elif text == '///':
                self.cbrtval = float(np.cbrt(self.scvalue.get()))
                self.scvalue.set(self.cbrtval)
                self.screeen.update()
            
            elif text == '**':
                self.sbval = float(self.scvalue.get())**2
                self.scvalue.set(self.sbval)
                self.screeen.update()
            
            elif text == '***':
                self.cbval = float(self.scvalue.get())**3
                self.scvalue.set(self.cbval)
                self.screeen.update()
            
            elif text == '^':
                self.poww = simpledialog.askfloat(title='Enter he value', prompt='Enter the value which you want to put in power')
                if self.poww == None:
                    pass
                else:
                    self.powval = float(float(self.scvalue.get())**self.poww)
                    self.scvalue.set(self.powval)
                    self.screeen.update()

            else:
                self.scvalue.set(f'{self.scvalue.get()}{text}')
                self.screeen.update()
            

        self.f1 = tk.Frame(self)

        self.b1 = tk.Button(self.f1, text='C')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='1')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='6')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='9')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        
        self.f1.pack(side=tk.LEFT, anchor='n')

        self.f1 = tk.Frame(self)

        self.b1 = tk.Button(self.f1, text='0')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='2')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='5')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='8')
        self.b1.pack(side=tk.BOTTOM)
        self.b1.bind('<1>', cilck)

        self.f1.pack(side=tk.LEFT, anchor='n')

        self.f1 = tk.Frame(self)
        self.b1 = tk.Button(self.f1, text='7')
        self.b1.pack(side=tk.TOP, anchor='n')
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='4')
        self.b1.pack(side=tk.TOP, anchor='n')
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='3')
        self.b1.pack(side=tk.TOP, anchor='n')
        self.b1.bind('<1>', cilck)
        self.b1 = tk.Button(self.f1, text='=')
        self.b1.pack(side=tk.TOP, anchor='n')
        self.b1.bind('<1>', cilck)

        self.f1.pack(side=tk.LEFT, anchor='n')

        self.f4 = tk.Frame(self)
        self.f5 = tk.Frame(self)
        self.f6 = tk.Frame(self)

        b1 = tk.Button(self.f4, text='+')
        b1.pack(side=tk.LEFT, ipadx=3)
        b1.bind('<1>', cilck)
        b1 = tk.Button(self.f4, text='/')
        b1.pack(side=tk.LEFT, ipadx=3)
        b1.bind('<1>', cilck)
        b1 = tk.Button(self.f4, text='*')
        b1.pack(side=tk.LEFT, ipadx=3.5)
        b1.bind('<1>', cilck)

        b2 = tk.Button(self.f5, text='-')
        b2.pack(side=tk.LEFT, ipadx=2)
        b2.bind('<1>', cilck)
        b2 = tk.Button(self.f5, text='//')
        b2.pack(side=tk.LEFT, ipadx=2.5)
        b2.bind('<1>', cilck)
        b2 = tk.Button(self.f5, text='**')
        b2.pack(side=tk.LEFT, ipadx=2.5)
        b2.bind('<1>', cilck)

        b3 = tk.Button(self.f6, text='^')
        b3.pack(side=tk.LEFT)
        b3.bind('<1>', cilck)
        b3 = tk.Button(self.f6, text='///')
        b3.pack(side=tk.LEFT)
        b3.bind('<1>', cilck)
        b3 = tk.Button(self.f6, text='***')
        b3.pack(side=tk.LEFT)
        b3.bind('<1>', cilck)

        self.f4.pack(side=tk.TOP, anchor='e')
        self.f5.pack(side=tk.TOP, anchor='e')
        self.f6.pack(side=tk.TOP, anchor='e')

    
if __name__ == '__main__':
    window = GUI()
    window.statusbar()
    window.InstructionsBar()
    window.entrybox()
    window.buttons()
    window.mainloop()