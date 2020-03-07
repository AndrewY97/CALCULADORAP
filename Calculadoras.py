import tkinter as tk
import math

class Calculadoras:
    def __init__(self):
        self.op3=""
        self.valor=False
        self.op=""
        self.op2=""
        self.sim=""
        self.res=0.0

    def C1(self):
        self.vp=tk.Tk()
        self.vp.title("Calculadora")
        self.vp.geometry("216x270")
        self.vp.config(bg='#5E5654')
        self.variable=tk.StringVar()
        self.caja1 = tk.Entry(self.vp,bg='#5E5654',fg='white',textvariable=self.variable,).place(x=5,y=5,width=204,height=40)
        btn1 = tk.Button(self.vp, text="MC",bg='#5E5654',fg='white').place(x=5,y=50,width=30)
        btn2 = tk.Button(self.vp, text="MR",bg='#5E5654',fg='white').place(x=40,y=50,width=30)
        btn3 = tk.Button(self.vp, text="M+",bg='#5E5654',fg='white').place(x=75,y=50,width=30)
        btn4 = tk.Button(self.vp, text="M-",bg='#5E5654',fg='white').place(x=110,y=50,width=30)
        btn5 = tk.Button(self.vp, text="MS",bg='#5E5654',fg='white').place(x=145,y=50,width=30)
        btn6 = tk.Button(self.vp, text="MV",bg='#5E5654',fg='white').place(x=180,y=50,width=30)
        btnpor = tk.Button(self.vp, text="%",bg='#5E5654',fg='white').place(x=5,y=80,width=50)
        btnce = tk.Button(self.vp, text="CE",bg='#5E5654',fg='white',command=self.c).place(x=57,y=80,width=50)
        btnc = tk.Button(self.vp, text="C",bg='#5E5654',fg='white',command=self.c).place(x=109,y=80,width=50)
        btndel = tk.Button(self.vp, text="DEL",bg='#5E5654',fg='white').place(x=161,y=80,width=50)
        btnxx = tk.Button(self.vp, text="1/X",bg='#5E5654',fg='white',command=self.log).place(x=5,y=110,width=50)
        btnx2 = tk.Button(self.vp, text="x2",bg='#5E5654',fg='white',command=self.cuad).place(x=57,y=110,width=50)
        btnraiz = tk.Button(self.vp, text="√",bg='#5E5654',fg='white',command=self.raiz).place(x=109,y=110,width=50)
        btndiv = tk.Button(self.vp, text="÷",bg='#5E5654',fg='white',command=self.entre).place(x=161,y=110,width=50)
        btnsie = tk.Button(self.vp, text="7",bg='#423C3B',fg='white',command=self.siete).place(x=5,y=140,width=50)
        btnocho = tk.Button(self.vp, text="8",bg='#423C3B',fg='white',command=self.ocho).place(x=57,y=140,width=50)
        btnnue = tk.Button(self.vp, text="9",bg='#423C3B',fg='white',command=self.nueve).place(x=109,y=140,width=50)
        btnmult = tk.Button(self.vp, text="x",bg='#5E5654',fg='white',command=self.por).place(x=161,y=140,width=50)
        btnpor = tk.Button(self.vp, text="4",bg='#423C3B',fg='white',command=self.cuatro).place(x=5,y=170,width=50)
        btnpor = tk.Button(self.vp, text="5",bg='#423C3B',fg='white',command=self.cinco).place(x=57,y=170,width=50)
        btnpor = tk.Button(self.vp, text="6",bg='#423C3B',fg='white',command=self.seis).place(x=109,y=170,width=50)
        btnpor = tk.Button(self.vp, text="-",bg='#5E5654',fg='white',command=self.menos).place(x=161,y=170,width=50)
        btnpor = tk.Button(self.vp, text="1",bg='#423C3B',fg='white',command=self.uno).place(x=5,y=200,width=50)
        btnpor = tk.Button(self.vp, text="2",bg='#423C3B',fg='white',command=self.dos).place(x=57,y=200,width=50)
        btnpor = tk.Button(self.vp, text="3",bg='#423C3B',fg='white',command=self.tres).place(x=109,y=200,width=50)
        btnpor = tk.Button(self.vp, text="+",bg='#5E5654',fg='white',command=self.mas).place(x=161,y=200,width=50)
        btnpor = tk.Button(self.vp, text="±",bg='#423C3B',fg='white',command=self.dos).place(x=5,y=230,width=50)
        btnpor = tk.Button(self.vp, text="0",bg='#423C3B',fg='white',command=self.cero).place(x=57,y=230,width=50)
        btnpor = tk.Button(self.vp, text=".",bg='#423C3B',fg='white',command=self.punto).place(x=109,y=230,width=50)
        btnpor = tk.Button(self.vp, text="=",bg='#CD2672',fg='white',command=self.igual).place(x=161,y=230,width=50)
        self.vp.mainloop()

    def uno(self):
        self.op3 = "1"
        if self.valor==False:
            self.op=self.op+"1"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"1"
            self.variable.set(self.op2)
    def dos(self):
        self.op3 = "2"
        if self.valor==False:
            self.op=self.op+"2"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"2"
            self.variable.set(self.op2)
    def tres(self):
        self.op3 = "3"
        if self.valor==False:
            self.op=self.op+"3"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"3"
            self.variable.set(self.op2)
    def cuatro(self):
        self.op3 = "4"
        if self.valor==False:
            self.op=self.op+"4"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"4"
            self.variable.set(self.op2)
    def cinco(self):
        self.op3 = "5"
        if self.valor==False:
            self.op=self.op+"5"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"5"
            self.variable.set(self.op2)
    def seis(self):
        self.op3 = "6"
        if self.valor==False:
            self.op=self.op+"6"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"6"
            self.variable.set(self.op2)
    def siete(self):
        self.op3 = "7"
        if self.valor==False:
            self.op=self.op+"7"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"7"
            self.variable.set(self.op2)
    def ocho(self):
        self.op3 = "8"
        if self.valor==False:
            self.op=self.op+"8"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"8"
            self.variable.set(self.op2)
    def nueve(self):
        self.op3 = "9"
        if self.valor==False:
            self.op=self.op+"9"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"9"
            self.variable.set(self.op2)
    def cero(self):
        self.op3 = "0"
        if self.valor==False:
            self.op=self.op+"0"
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"0"
            self.variable.set(self.op2)
    def punto(self):
        self.op3 = "."
        if self.valor==False:
            self.op=self.op+"."
            self.variable.set(self.op)
        else:
            self.op2=self.op2+"."
            self.variable.set(self.op2)
    def mas(self):
        self.variable.set("+")
        self.op3="+"
        self.sim="+"
        self.valor=True
    def menos(self):
        self.variable.set("-")
        self.op3="-"
        self.sim="-"
        self.valor=True
    def por(self):
        self.variable.set("x")
        self.op3 = "x"
        self.sim = "x"
        self.valor = True
    def cuad(self):
        self.variable.set("x2")
        self.op3 = "x2"
        self.sim = "x2"
        self.valor=True
    def raiz(self):
        self.variable.set("√")
        self.op3 = "√"
        self.sim = "√"
        self.valor = True
    def entre(self):
        self.variable.set("/")
        self.op3 = "/"
        self.sim = "/"
        self.valor = True

    def c(self):
        self.variable.set("")
        self.op=""
        self.op2=""
        self.sim=""
        self.res=0.0
        self.valor=False

    def log(self):
        self.variable.set("1/x")
        self.op3 = "1/x"
        self.sim = "1/x"
        self.valor = True

    def igual(self):
        if self.sim=="+":
            self.res=float(self.op)+float(self.op2)
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            #self.sim = ""
            self.res = 0.0
            self.valor = False
        if self.sim=="-":
            self.res=float(self.op)-float(self.op2)
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            # self.sim = ""
            self.res = 0.0
            self.valor = False
        if self.sim=="x":
            self.res = float(self.op) * float(self.op2)
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            # self.sim = ""
            self.res = 0.0
            self.valor = False
        if self.sim=="/":
            self.res = float(self.op) / float(self.op2)
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            # self.sim = ""
            self.res = 0.0
            self.valor = False
        if self.sim=="x2":
            self.res =pow(float(self.op),2)
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            # self.sim = ""
            self.res = 0.0
            self.valor = False
        if self.sim=="√":
            self.res =math.sqrt(float(self.op))
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            # self.sim = ""
            self.res = 0.0
            self.valor = False
        if self.sim=="1/x":
            self.res =math.log(1,float(self.op))
            self.variable.set(str(self.res))
            self.sim = ""
            self.op = ""
            self.op2 = ""
            # self.sim = ""
            self.res = 0.0
            self.valor = False


    """def c2(self):
        self.vp=tk.Tk()
        self.vp.title("Calculadora")
        self.vp.geometry("216x270")
        self.vp.config(bg='#5E5654')
        self.panel1=tk.Frame(self.vp,bg='#5E5654',width=350,height=50)
        self.panel1.pack()
        caja1 = tk.Entry(self.panel1,bg='#5E5654',fg='white').pack(ipadx=204,ipady=15)
        self.panel2 = tk.Frame(self.vp,bg='#5E5654',width=350,height=50)
        self.panel2.pack()
        btn1 = tk.Button(self.panel2, text="MC",bg='#5E5654',fg='white',width=3).pack(side=tk.LEFT, ipadx=2,ipady=2)
        btn2 = tk.Button(self.panel2, text="MR",bg='#5E5654',fg='white',width=3).pack(side=tk.LEFT, ipadx=2,ipady=2)
        btn3 = tk.Button(self.panel2, text="M+",bg='#5E5654',fg='white',width=3).pack(side=tk.LEFT, ipadx=2,ipady=2)
        btn4 = tk.Button(self.panel2, text="M-",bg='#5E5654',fg='white',width=3).pack(side=tk.LEFT, ipadx=2,ipady=2)
        btn5 = tk.Button(self.panel2, text="MS",bg='#5E5654',fg='white',width=3).pack(side=tk.LEFT, ipadx=2,ipady=2)
        btn6 = tk.Button(self.panel2, text="MV",bg='#5E5654',fg='white',width=3).pack(side=tk.LEFT, ipadx=2,ipady=2)
        self.panel3= tk.Frame(self.vp,bg='#5E5654',width=350,height=50)
        self.panel3.pack()
        btnpor = tk.Button(self.panel3, text="%",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnce = tk.Button(self.panel3, text="CE",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnc = tk.Button(self.panel3, text="C",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btndel = tk.Button(self.panel3, text="DEL",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        self.panel4 = tk.Frame(self.vp, bg='#5E5654', width=350, height=50)
        self.panel4.pack()
        btnxx = tk.Button(self.panel4, text="1/x",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnx2 = tk.Button(self.panel4, text="x2",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnraiz = tk.Button(self.panel4, text="√",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btndiv = tk.Button(self.panel4, text="÷",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        self.panel5 = tk.Frame(self.vp, bg='#5E5654', width=350, height=50)
        self.panel5.pack()
        btnsie = tk.Button(self.panel5, text="7",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnocho = tk.Button(self.panel5, text="8",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnnue = tk.Button(self.panel5, text="9",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnmult = tk.Button(self.panel5, text="x",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        self.panel6 = tk.Frame(self.vp, bg='#5E5654', width=350, height=50)
        self.panel6.pack()
        btnpor = tk.Button(self.panel6, text="4",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel6, text="5",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel6, text="6",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel6, text="-",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        self.panel7 = tk.Frame(self.vp, bg='#5E5654', width=350, height=50)
        self.panel7.pack()
        btnpor = tk.Button(self.panel7, text="1",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel7, text="2",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel7, text="3",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel7, text="+",bg='#5E5654',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        self.panel8 = tk.Frame(self.vp, bg='#5E5654', width=350, height=50)
        self.panel8.pack()
        btnpor = tk.Button(self.panel8, text="±",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel8, text="0",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel8, text=".",bg='#423C3B',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        btnpor = tk.Button(self.panel8, text="=",bg='#CD2672',fg='white',width=2).pack(side=tk.LEFT, ipadx=9,ipady=2,padx=5)
        self.vp.mainloop()

    def c3(self):
        self.vp = tk.Tk()
        self.vp.title("Calculadora")
        self.vp.geometry("216x270")
        self.vp.config(bg='#5E5654')
        #self.panel = tk.Frame(self.vp, bg='#5E5654', width=350, height=50)
        #self.panel.grid(row=0, column=0)
        caja1 = tk.Entry(self.vp, bg='#5E5654', fg='white').grid(row=0,column=0,sticky='w',columnspan=7,ipadx=45,ipady=8)
        #btn0 = tk.Button(self.vp, text="", bg='#5E5654', fg='white').grid(row=2, column=0, sticky='w',columnspan=19,ipadx=100)
        btn1 = tk.Button(self.vp, text="MC", bg='#5E5654', fg='white',width=2).grid(row=5,column=0,sticky='w',columnspan=1)
        btn2 = tk.Button(self.vp, text="MR", bg='#5E5654', fg='white',width=2).grid(row=5,column=1,columnspan=1)
        btn3 = tk.Button(self.vp, text="M+", bg='#5E5654', fg='white',width=2).grid(row=5,column=2,sticky='w')
        btn4 = tk.Button(self.vp, text="M-", bg='#5E5654', fg='white',width=2).grid(row=5,column=3,sticky='w',)
        btn5 = tk.Button(self.vp, text="MS", bg='#5E5654', fg='white',width=2).grid(row=5,column=4,sticky='w',)
        btn6 = tk.Button(self.vp, text="MV", bg='#5E5654', fg='white',width=2).grid(row=5,column=5,sticky='w')
        btnpor = tk.Button(self.vp, text="%", bg='#5E5654', fg='white',width=4).grid(row=6,column=0,sticky='w',)
        btnce = tk.Button(self.vp, text="CE", bg='#5E5654', fg='white',width=4).grid(row=6,column=1,sticky='w')
        btnc = tk.Button(self.vp, text="C", bg='#5E5654', fg='white',width=4).grid(row=6,column=2,sticky='w',)
        btndel = tk.Button(self.vp, text="DEL", bg='#5E5654', fg='white',width=4).grid(row=6,column=3,sticky='w')
        btnxx = tk.Button(self.vp, text="1/X", bg='#5E5654', fg='white',width=4).grid(row=7,column=0,sticky='w',)
        btnx2 = tk.Button(self.vp, text="x2", bg='#5E5654', fg='white',width=4).grid(row=7,column=1,sticky='w',)
        btnraiz = tk.Button(self.vp, text="√", bg='#5E5654', fg='white',width=4).grid(row=7,column=2,sticky='w')
        btndiv = tk.Button(self.vp, text="÷", bg='#5E5654', fg='white',width=4).grid(row=7,column=3,sticky='w',)
        btnsie = tk.Button(self.vp, text="7", bg='#423C3B', fg='white',width=4).grid(row=8,column=0,sticky='w',)
        btnocho = tk.Button(self.vp, text="8", bg='#423C3B', fg='white',width=4).grid(row=8,column=1,sticky='w',)
        btnnue = tk.Button(self.vp, text="9", bg='#423C3B', fg='white',width=4).grid(row=8,column=2,sticky='w',)
        btnmult = tk.Button(self.vp, text="x", bg='#5E5654', fg='white',width=4).grid(row=8,column=3,sticky='w')
        btnpor = tk.Button(self.vp, text="4", bg='#423C3B', fg='white',width=4).grid(row=9,column=0,sticky='w')
        btnpor = tk.Button(self.vp, text="5", bg='#423C3B', fg='white',width=4).grid(row=9,column=1,sticky='w')
        btnpor = tk.Button(self.vp, text="6", bg='#423C3B', fg='white',width=4).grid(row=9,column=2,sticky='w')
        btnpor = tk.Button(self.vp, text="-", bg='#5E5654', fg='white',width=4).grid(row=9,column=3,sticky='w')
        btnpor = tk.Button(self.vp, text="1", bg='#423C3B', fg='white',width=4).grid(row=10,column=0,sticky='w')
        btnpor = tk.Button(self.vp, text="2", bg='#423C3B', fg='white',width=4).grid(row=10,column=1,sticky='w')
        btnpor = tk.Button(self.vp, text="3", bg='#423C3B', fg='white',width=4).grid(row=10,column=2,sticky='w')
        btnpor = tk.Button(self.vp, text="+", bg='#5E5654', fg='white',width=4).grid(row=10,column=3,sticky='w')
        btnpor = tk.Button(self.vp, text="±", bg='#423C3B', fg='white',width=4).grid(row=11,column=0,sticky='w')
        btnpor = tk.Button(self.vp, text="0", bg='#423C3B', fg='white',width=4).grid(row=11,column=1,sticky='w')
        btnpor = tk.Button(self.vp, text=".", bg='#423C3B', fg='white',width=4).grid(row=11,column=2,sticky='w')
        btnpor = tk.Button(self.vp, text="=", bg='#CD2672', fg='white',width=4).grid(row=11,column=3,sticky='w')
        self.vp.mainloop()"""

C=Calculadoras()
C.C1()
#C.c2()
#C.c3()