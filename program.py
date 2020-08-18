

from __future__ import print_function

from ortools.linear_solver import pywraplp

from tkinter import *
import tkinter as tk

import sys

from tkinter.ttk import *


def RunIntegerExampleNaturalLanguageAPI(optimization_problem_type):
    raiz1=tk.Tk()
    raiz1.geometry("1300x550")
    raiz1.title("Interfaz Soluciones PEM")
    img=PhotoImage(file="/home/juan/Documentos/Semestre 2020-1/IO/Codigo python/ud.png")
    Label1=Label(raiz1, image=img).grid(column = 0, row = 0)
    Label2=Label(raiz1, text="Programación mixta entera", font=("Arial Bold", 20))
    Label2.grid(column = 2, row = 0)


    solver = pywraplp.Solver('Solucion ejemplo',
                             optimization_problem_type)
    infinity = solver.infinity()
    #se escribe cada variable se inicializa en cero, y se comprueba que nosea negativa
    #si la variable es numerica se escribe Numvar
    #si la variable es entera se escribe IntVar






    labelz130 = Label(raiz1, text = "Ingresar tipo de problema" , font=("Arial Bold", 10))
    labelz130.grid(column = 0, row = 1)


    com = Combobox(raiz1,values=["Maximizar","Minimizar"], state="readonly")
    com.grid(column = 1, row = 1)



    despla=4
    labelz13 = Label(raiz1, text = "Ingresar ecuacion a optimizar" , font=("Arial Bold", 10))
    labelz13.grid(column = 0, row = 5)





    j1=IntVar()
    j2=IntVar()
    j3=IntVar()
    j4=IntVar()
    j5=IntVar()


    j1R=IntVar()
    j2R=IntVar()
    j3R=IntVar()
    j4R=IntVar()
    j5R=IntVar()
    jIR=IntVar()

    j1R2=IntVar()
    j2R2=IntVar()
    j3R2=IntVar()
    j4R2=IntVar()
    j5R2=IntVar()
    jIR2=IntVar()

    j1R3=IntVar()
    j2R3=IntVar()
    j3R3=IntVar()
    j4R3=IntVar()
    j5R3=IntVar()
    jIR3=IntVar()


    j1R4=IntVar()
    j2R4=IntVar()
    j3R4=IntVar()
    j4R4=IntVar()
    j5R4=IntVar()
    jIR4=IntVar()

    j1R5=IntVar()
    j2R5=IntVar()
    j3R5=IntVar()
    j4R5=IntVar()
    j5R5=IntVar()
    jIR5=IntVar()

    j1R6=IntVar()
    j2R6=IntVar()
    j3R6=IntVar()
    j4R6=IntVar()
    j5R6=IntVar()
    jIR6=IntVar()
    jIR6=IntVar()

    j1R7=IntVar()
    j2R7=IntVar()
    j3R7=IntVar()
    j4R7=IntVar()
    j5R7=IntVar()
    jIR7=IntVar()
    jIR7=IntVar()


    labelz1 = Label(raiz1, text = "Ingresar variables enteras" , font=("Arial Bold", 10))
    labelz1.grid(column = 0, row = 4)
    ec4 =Entry(raiz1, width=20)
    ec4.grid(column = 1, row =4)
    def numvarc():

        if ecnumecu.get()=="1":

            if ec4.get()=="x1":
                x1 = solver.floatVar(0.0, infinity, 'x1')


            ec10 =Entry(raiz1, width=5,textvariable=j1)
            ec10.place(x=200, y=210)
            labelec10 = Label(raiz1, text = "*x1" , font=("Arial Bold", 10))
            labelec10.place(x=243, y=210)

            def termine():
                 if com.get()=="Maximizar":
                    solver.Maximize(float(ec10.get())*x1)
                 if com.get()=="Minimizar":
                    solver.Minimize(float(ec10.get())*x1)

            btermine = tk.Button(raiz1, height=1, width=1 ,text="Y", command=termine)
            btermine.place(x=268, y=207)

        if ecnumecu.get()=="2":

            if ec4.get()=="x1":
                x1 = solver.IntVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')


            if ec4.get()=="x2":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.IntVar(0.0, infinity, 'x2')





            ec10 =Entry(raiz1, width=5,textvariable=j1)
            ec10.place(x=200, y=210)
            abelec10 = Label(raiz1, text = "*x1" , font=("Arial Bold", 10))
            abelec10.place(x=243, y=210)

            ec11 =Entry(raiz1, width=5,textvariable=j2)
            ec11.place(x=270, y=210)
            labelec11 = Label(raiz1, text = "*x2" , font=("Arial Bold", 10))
            labelec11.place(x=313, y=210)

            def termine():
                if com.get()=="Maximizar":
                  solver.Maximize(float(ec10.get())*x1+float(ec11.get())*x2)
                if com.get()=="Minimizar":
                  solver.Minimize(float(ec10.get())*x1+float(ec11.get())*x2)

            btermine = tk.Button(raiz1, height=1, width=1 ,text="Y", command=termine)
            btermine.place(x=338, y=207)

        if ecnumecu.get()=="3":

            if ec4.get()=="x1":
                x1 = solver.IntVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')

            if ec4.get()=="x2":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.IntVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')

            if ec4.get()=="x3":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.IntVar(0.0, infinity, 'x3')



            if ec4.get()=="x1":
                x1 = solver.IntVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')

            if ec4.get()=="x2":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.IntVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')

            if ec4.get()=="x3":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.IntVar(0.0, infinity, 'x3')



            ec10 =Entry(raiz1, width=5,textvariable=j1)
            ec10.place(x=200, y=210)
            labelec10 = Label(raiz1, text = "*x1" , font=("Arial Bold", 10))
            labelec10.place(x=243, y=210)

            ec11 =Entry(raiz1, width=5,textvariable=j2)
            ec11.place(x=270, y=210)
            labelec11 = Label(raiz1, text = "*x2" , font=("Arial Bold", 10))
            labelec11.place(x=315, y=210)

            ec12 =Entry(raiz1, width=5,textvariable=j3)
            ec12.place(x=340, y=210)
            labelec12 = Label(raiz1, text = "*x3" , font=("Arial Bold", 10))
            labelec12.place(x=387, y=210)

            def termine():
                if com.get()=="Maximizar":
                   solver.Maximize(float(ec10.get())*x1+float(ec11.get())*x2+float(ec12.get())*x3)
                if com.get()=="Minimizar":
                   solver.Minimize(float(ec10.get())*x1+float(ec11.get())*x2+float(ec12.get())*x3)

            btermine = tk.Button(raiz1, height=1, width=1 ,text="Y", command=termine)
            btermine.place(x=412, y=207)




        if ecnumecu.get()=="4":



            if ec4.get()=="x1":
                x1 = solver.IntVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')
                x4 = solver.NumVar(0.0, infinity, 'x4')
            if ec4.get()=="x2":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.IntVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')
                x4 = solver.NumVar(0.0, infinity, 'x4')
            if ec4.get()=="x3":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.IntVar(0.0, infinity, 'x3')
                x4 = solver.NumVar(0.0, infinity, 'x4')
            if ec4.get()=="x4":
                x1 = solver.NumVar(0.0, infinity, 'x1')
                x2 = solver.NumVar(0.0, infinity, 'x2')
                x3 = solver.NumVar(0.0, infinity, 'x3')
                x4 = solver.IntVar(0.0, infinity, 'x4')



            ec10 =Entry(raiz1, width=5,textvariable=j1)
            ec10.place(x=200, y=210)
            labelec10 = Label(raiz1, text = "*x1" , font=("Arial Bold", 10))
            labelec10.place(x=243, y=210)



            ec11 =Entry(raiz1, width=5,textvariable=j2)
            ec11.place(x=270, y=210)
            labelec11 = Label(raiz1, text = "*x2" , font=("Arial Bold", 10))
            labelec11.place(x=315, y=210)


            ec12 =Entry(raiz1, width=5,textvariable=j3)
            ec12.place(x=340, y=210)
            labelec12 = Label(raiz1, text = "*x3" , font=("Arial Bold", 10))
            labelec12.place(x=385, y=210)


            ec13 =Entry(raiz1, width=5,textvariable=j4)
            ec13.place(x=410, y=210)
            labelec13 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
            labelec13.place(x=457, y=210)




            def termine():
                if com.get()=="Maximizar":
                   solver.Maximize(float(ec10.get())*x1+float(ec11.get())*x2+float(ec12.get())*x3+float(ec13.get())*x4)

                if com.get()=="Minimizar":
                   solver.Minimize(float(ec10.get())*x1+float(ec11.get())*x2+float(ec12.get())*x3+float(ec13.get())*x4)



            def clicked():

                if ec22.get()=="1":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)
                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))


                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=410)




                if ec22.get()=="2":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">=","="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)

                    solv12 =Entry(raiz1, width=5,textvariable=j1R2)
                    solv12.place(x=650, y=232)
                    labelsolv12 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv12.place(x=693, y=232)

                    solv22 =Entry(raiz1, width=5,textvariable=j2R2)
                    solv22.place(x=738, y=232)
                    labelsolv22 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv22.place(x=783, y=232)

                    solv32 =Entry(raiz1, width=5,textvariable=j3R2)
                    solv32.place(x=828, y=232)
                    labelsolv32= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv32.place(x=873, y=232)

                    solv42 =Entry(raiz1, width=5,textvariable=j4R2)
                    solv42.place(x=918, y=232)
                    labelsolv42 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv42.place(x=963, y=232)

                    comsolv12 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv12.place(x=990, y=232)

                    solv2igual =Entry(raiz1, width=5,textvariable=jIR2)
                    solv2igual.place(x=1045, y=232)
                    labeligual2 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual2.place(x=1025, y=232)

                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))

                        if comsolv12.get()=="<=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 <= float(solv2igual.get()))
                        if comsolv12.get()==">=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 >= float(solv2igual.get()))

                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=510)

                if ec22.get()=="3":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">=","="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)

                    #otro

                    solv12 =Entry(raiz1, width=5,textvariable=j1R2)
                    solv12.place(x=650, y=232)
                    labelsolv12 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv12.place(x=693, y=232)

                    solv22 =Entry(raiz1, width=5,textvariable=j2R2)
                    solv22.place(x=738, y=232)
                    labelsolv22 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv22.place(x=783, y=232)

                    solv32 =Entry(raiz1, width=5,textvariable=j3R2)
                    solv32.place(x=828, y=232)
                    labelsolv32= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv32.place(x=873, y=232)

                    solv42 =Entry(raiz1, width=5,textvariable=j4R2)
                    solv42.place(x=918, y=232)
                    labelsolv42 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv42.place(x=963, y=232)

                    comsolv12 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv12.place(x=990, y=232)

                    solv2igual =Entry(raiz1, width=5,textvariable=jIR2)
                    solv2igual.place(x=1045, y=232)
                    labeligual2 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual2.place(x=1025, y=232)

                    #otro

                    solv13 =Entry(raiz1, width=5,textvariable=j1R3)
                    solv13.place(x=650, y=254)
                    labelsolv13 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv13.place(x=693, y=254)

                    solv23 =Entry(raiz1, width=5,textvariable=j2R3)
                    solv23.place(x=738, y=254)
                    labelsolv23 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv23.place(x=783, y=254)

                    solv33 =Entry(raiz1, width=5,textvariable=j3R3)
                    solv33.place(x=828, y=254)
                    labelsolv33= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv33.place(x=873, y=254)

                    solv43 =Entry(raiz1, width=5,textvariable=j4R3)
                    solv43.place(x=918, y=254)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=254)

                    comsolv13 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv13.place(x=990, y=254)

                    solv3igual =Entry(raiz1, width=5,textvariable=jIR3)
                    solv3igual.place(x=1045, y=254)
                    labeligual3 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual3.place(x=1025, y=254)

                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))

                        if comsolv12.get()=="<=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 <= float(solv2igual.get()))
                        if comsolv12.get()==">=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 >= float(solv2igual.get()))

                        if comsolv13.get()=="<=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 <= float(solv3igual.get()))
                        if comsolv13.get()==">=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 >= float(solv3igual.get()))



                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=510)

                if ec22.get()=="4":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">=","="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)

                    #otro

                    solv12 =Entry(raiz1, width=5,textvariable=j1R2)
                    solv12.place(x=650, y=232)
                    labelsolv12 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv12.place(x=693, y=232)

                    solv22 =Entry(raiz1, width=5,textvariable=j2R2)
                    solv22.place(x=738, y=232)
                    labelsolv22 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv22.place(x=783, y=232)

                    solv32 =Entry(raiz1, width=5,textvariable=j3R2)
                    solv32.place(x=828, y=232)
                    labelsolv32= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv32.place(x=873, y=232)

                    solv42 =Entry(raiz1, width=5,textvariable=j4R2)
                    solv42.place(x=918, y=232)
                    labelsolv42 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv42.place(x=963, y=232)

                    comsolv12 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv12.place(x=990, y=232)

                    solv2igual =Entry(raiz1, width=5,textvariable=jIR2)
                    solv2igual.place(x=1045, y=232)
                    labeligual2 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual2.place(x=1025, y=232)

                    #otro

                    solv13 =Entry(raiz1, width=5,textvariable=j1R3)
                    solv13.place(x=650, y=254)
                    labelsolv13 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv13.place(x=693, y=254)

                    solv23 =Entry(raiz1, width=5,textvariable=j2R3)
                    solv23.place(x=738, y=254)
                    labelsolv23 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv23.place(x=783, y=254)

                    solv33 =Entry(raiz1, width=5,textvariable=j3R3)
                    solv33.place(x=828, y=254)
                    labelsolv33= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv33.place(x=873, y=254)

                    solv43 =Entry(raiz1, width=5,textvariable=j4R3)
                    solv43.place(x=918, y=254)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=254)

                    comsolv13 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv13.place(x=990, y=254)

                    solv3igual =Entry(raiz1, width=5,textvariable=jIR3)
                    solv3igual.place(x=1045, y=254)
                    labeligual3 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual3.place(x=1025, y=254)

                    #otro

                    solv14 =Entry(raiz1, width=5,textvariable=j1R4)
                    solv14.place(x=650, y=276)
                    labelsolv14 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv14.place(x=693, y=276)

                    solv24 =Entry(raiz1, width=5,textvariable=j2R4)
                    solv24.place(x=738, y=276)
                    labelsolv24 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv24.place(x=783, y=276)

                    solv34 =Entry(raiz1, width=5,textvariable=j3R4)
                    solv34.place(x=828, y=276)
                    labelsolv34= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv34.place(x=873, y=276)

                    solv44 =Entry(raiz1, width=5,textvariable=j4R4)
                    solv44.place(x=918, y=276)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=276)

                    comsolv14 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv14.place(x=990, y=276)

                    solv4igual =Entry(raiz1, width=5,textvariable=jIR4)
                    solv4igual.place(x=1045, y=276)
                    labeligual4 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual4.place(x=1025, y=276)

                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))

                        if comsolv12.get()=="<=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 <= float(solv2igual.get()))
                        if comsolv12.get()==">=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 >= float(solv2igual.get()))

                        if comsolv13.get()=="<=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 <= float(solv3igual.get()))
                        if comsolv13.get()==">=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 >= float(solv3igual.get()))

                        if comsolv14.get()=="<=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 <= float(solv4igual.get()))
                        if comsolv14.get()==">=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 >= float(solv4igual.get()))

                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=510)

                if ec22.get()=="5":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">=","="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)

                    #otro

                    solv12 =Entry(raiz1, width=5,textvariable=j1R2)
                    solv12.place(x=650, y=232)
                    labelsolv12 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv12.place(x=693, y=232)

                    solv22 =Entry(raiz1, width=5,textvariable=j2R2)
                    solv22.place(x=738, y=232)
                    labelsolv22 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv22.place(x=783, y=232)

                    solv32 =Entry(raiz1, width=5,textvariable=j3R2)
                    solv32.place(x=828, y=232)
                    labelsolv32= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv32.place(x=873, y=232)

                    solv42 =Entry(raiz1, width=5,textvariable=j4R2)
                    solv42.place(x=918, y=232)
                    labelsolv42 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv42.place(x=963, y=232)

                    comsolv12 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv12.place(x=990, y=232)

                    solv2igual =Entry(raiz1, width=5,textvariable=jIR2)
                    solv2igual.place(x=1045, y=232)
                    labeligual2 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual2.place(x=1025, y=232)

                    #otro

                    solv13 =Entry(raiz1, width=5,textvariable=j1R3)
                    solv13.place(x=650, y=254)
                    labelsolv13 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv13.place(x=693, y=254)

                    solv23 =Entry(raiz1, width=5,textvariable=j2R3)
                    solv23.place(x=738, y=254)
                    labelsolv23 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv23.place(x=783, y=254)

                    solv33 =Entry(raiz1, width=5,textvariable=j3R3)
                    solv33.place(x=828, y=254)
                    labelsolv33= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv33.place(x=873, y=254)

                    solv43 =Entry(raiz1, width=5,textvariable=j4R3)
                    solv43.place(x=918, y=210)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=254)

                    comsolv13 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv13.place(x=990, y=254)

                    solv3igual =Entry(raiz1, width=5,textvariable=jIR3)
                    solv3igual.place(x=1045, y=254)
                    labeligual3 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual3.place(x=1025, y=254)

                    #otro

                    solv14 =Entry(raiz1, width=5,textvariable=j1R4)
                    solv14.place(x=650, y=276)
                    labelsolv14 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv14.place(x=693, y=276)

                    solv24 =Entry(raiz1, width=5,textvariable=j2R4)
                    solv24.place(x=738, y=276)
                    labelsolv24 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv24.place(x=783, y=276)

                    solv34 =Entry(raiz1, width=5,textvariable=j3R4)
                    solv34.place(x=828, y=276)
                    labelsolv34= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv34.place(x=873, y=276)

                    solv44 =Entry(raiz1, width=5,textvariable=j4R4)
                    solv44.place(x=918, y=276)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=276)

                    comsolv14 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv14.place(x=990, y=276)

                    solv4igual =Entry(raiz1, width=5,textvariable=jIR4)
                    solv4igual.place(x=1045, y=276)
                    labeligual4 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual4.place(x=1025, y=276)

                    #otro

                    solv15 =Entry(raiz1, width=5,textvariable=j1R5)
                    solv15.place(x=650, y=298)
                    labelsolv15 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv15.place(x=693, y=298)

                    solv25 =Entry(raiz1, width=5,textvariable=j2R5)
                    solv25.place(x=738, y=298)
                    labelsolv25 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv25.place(x=783, y=298)

                    solv35 =Entry(raiz1, width=5,textvariable=j3R5)
                    solv35.place(x=828, y=298)
                    labelsolv35= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv35.place(x=873, y=298)

                    solv45 =Entry(raiz1, width=5,textvariable=j4R5)
                    solv45.place(x=918, y=298)
                    labelsolv45 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv45.place(x=963, y=298)

                    comsolv15 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv15.place(x=990, y=298)

                    solv5igual =Entry(raiz1, width=5,textvariable=jIR5)
                    solv5igual.place(x=1045, y=298)
                    labeligual5 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual5.place(x=1025, y=298)

                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))

                        if comsolv12.get()=="<=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 <= float(solv2igual.get()))
                        if comsolv12.get()==">=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 >= float(solv2igual.get()))

                        if comsolv13.get()=="<=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 <= float(solv3igual.get()))
                        if comsolv13.get()==">=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 >= float(solv3igual.get()))

                        if comsolv14.get()=="<=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 <= float(solv4igual.get()))
                        if comsolv14.get()==">=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 >= float(solv4igual.get()))

                        if comsolv15.get()=="<=":
                            solver.Add(float(solv15.get())*x1+float(solv25.get())*x2+float(solv35.get())*x3+float(solv45.get())*x4 <= float(solv5igual.get()))
                        if comsolv15.get()==">=":
                            solver.Add(float(solv15.get())*x1+float(solv25.get())*x2+float(solv35.get())*x3+float(solv45.get())*x4 >= float(solv5igual.get()))

                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=510)


                if ec22.get()=="6":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">=","="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)

                    #otro

                    solv12 =Entry(raiz1, width=5,textvariable=j1R2)
                    solv12.place(x=650, y=232)
                    labelsolv12 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv12.place(x=693, y=232)

                    solv22 =Entry(raiz1, width=5,textvariable=j2R2)
                    solv22.place(x=738, y=232)
                    labelsolv22 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv22.place(x=783, y=232)

                    solv32 =Entry(raiz1, width=5,textvariable=j3R2)
                    solv32.place(x=828, y=232)
                    labelsolv32= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv32.place(x=873, y=232)

                    solv42 =Entry(raiz1, width=5,textvariable=j4R2)
                    solv42.place(x=918, y=232)
                    labelsolv42 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv42.place(x=963, y=232)

                    comsolv12 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv12.place(x=990, y=232)

                    solv2igual =Entry(raiz1, width=5,textvariable=jIR2)
                    solv2igual.place(x=1045, y=232)
                    labeligual2 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual2.place(x=1025, y=232)

                    #otro

                    solv13 =Entry(raiz1, width=5,textvariable=j1R3)
                    solv13.place(x=650, y=254)
                    labelsolv13 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv13.place(x=693, y=254)

                    solv23 =Entry(raiz1, width=5,textvariable=j2R3)
                    solv23.place(x=738, y=254)
                    labelsolv23 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv23.place(x=783, y=254)

                    solv33 =Entry(raiz1, width=5,textvariable=j3R3)
                    solv33.place(x=828, y=254)
                    labelsolv33= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv33.place(x=873, y=254)

                    solv43 =Entry(raiz1, width=5,textvariable=j4R3)
                    solv43.place(x=918, y=254)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=254)

                    comsolv13 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv13.place(x=990, y=254)

                    solv3igual =Entry(raiz1, width=5,textvariable=jIR3)
                    solv3igual.place(x=1045, y=254)
                    labeligual3 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual3.place(x=1025, y=254)

                    #otro

                    solv14 =Entry(raiz1, width=5,textvariable=j1R4)
                    solv14.place(x=650, y=276)
                    labelsolv14 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv14.place(x=693, y=276)

                    solv24 =Entry(raiz1, width=5,textvariable=j2R4)
                    solv24.place(x=738, y=276)
                    labelsolv24 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv24.place(x=783, y=276)

                    solv34 =Entry(raiz1, width=5,textvariable=j3R4)
                    solv34.place(x=828, y=276)
                    labelsolv34= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv34.place(x=873, y=276)

                    solv44 =Entry(raiz1, width=5,textvariable=j4R4)
                    solv44.place(x=918, y=276)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=276)

                    comsolv14 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv14.place(x=990, y=276)

                    solv4igual =Entry(raiz1, width=5,textvariable=jIR4)
                    solv4igual.place(x=1045, y=276)
                    labeligual4 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual4.place(x=1025, y=276)

                    #otro

                    solv15 =Entry(raiz1, width=5,textvariable=j1R5)
                    solv15.place(x=650, y=298)
                    labelsolv15 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv15.place(x=693, y=298)

                    solv25 =Entry(raiz1, width=5,textvariable=j2R5)
                    solv25.place(x=738, y=298)
                    labelsolv25 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv25.place(x=783, y=298)

                    solv35 =Entry(raiz1, width=5,textvariable=j3R5)
                    solv35.place(x=828, y=298)
                    labelsolv35= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv35.place(x=873, y=298)

                    solv45 =Entry(raiz1, width=5,textvariable=j4R5)
                    solv45.place(x=918, y=298)
                    labelsolv45 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv45.place(x=963, y=298)

                    comsolv15 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv15.place(x=990, y=298)

                    solv5igual =Entry(raiz1, width=5,textvariable=jIR5)
                    solv5igual.place(x=1045, y=298)
                    labeligual5 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual5.place(x=1025, y=298)

                    #otro

                    solv16 =Entry(raiz1, width=5,textvariable=j1R6)
                    solv16.place(x=650, y=320)
                    labelsolv16 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv16.place(x=693, y=320)

                    solv26 =Entry(raiz1, width=5,textvariable=j2R6)
                    solv26.place(x=738, y=320)
                    labelsolv26 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv26.place(x=783, y=320)

                    solv36 =Entry(raiz1, width=5,textvariable=j3R6)
                    solv36.place(x=828, y=320)
                    labelsolv36= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv36.place(x=873, y=320)

                    solv46 =Entry(raiz1, width=5,textvariable=j4R6)
                    solv46.place(x=918, y=320)
                    labelsolv46 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv46.place(x=963, y=320)

                    comsolv16 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv16.place(x=990, y=320)

                    solv6igual =Entry(raiz1, width=5,textvariable=jIR6)
                    solv6igual.place(x=1045, y=320)
                    labeligual6 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual6.place(x=1025, y=320)

                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))

                        if comsolv12.get()=="<=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 <= float(solv2igual.get()))
                        if comsolv12.get()==">=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 >= float(solv2igual.get()))

                        if comsolv13.get()=="<=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 <= float(solv3igual.get()))
                        if comsolv13.get()==">=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 >= float(solv3igual.get()))

                        if comsolv14.get()=="<=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 <= float(solv4igual.get()))
                        if comsolv14.get()==">=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 >= float(solv4igual.get()))

                        if comsolv15.get()=="<=":
                            solver.Add(float(solv15.get())*x1+float(solv25.get())*x2+float(solv35.get())*x3+float(solv45.get())*x4 <= float(solv5igual.get()))
                        if comsolv15.get()==">=":
                            solver.Add(float(solv15.get())*x1+float(solv25.get())*x2+float(solv35.get())*x3+float(solv45.get())*x4 >= float(solv5igual.get()))

                        if comsolv16.get()=="<=":
                            solver.Add(float(solv16.get())*x1+float(solv26.get())*x2+float(solv36.get())*x3+float(solv46.get())*x4 <= float(solv6igual.get()))
                        if comsolv16.get()==">=":
                            solver.Add(float(solv16.get())*x1+float(solv26.get())*x2+float(solv36.get())*x3+float(solv46.get())*x4 >= float(solv6igual.get()))

                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=510)


                if ec22.get()=="7":

                    solv1 =Entry(raiz1, width=5,textvariable=j1R)
                    solv1.place(x=650, y=210)
                    labelsolv1 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv1.place(x=693, y=210)

                    solv2 =Entry(raiz1, width=5,textvariable=j2R)
                    solv2.place(x=738, y=210)
                    labelsolv2 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv2.place(x=783, y=210)

                    solv3 =Entry(raiz1, width=5,textvariable=j3R)
                    solv3.place(x=828, y=210)
                    labelsolv3= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv3.place(x=873, y=210)

                    solv4 =Entry(raiz1, width=5,textvariable=j4R)
                    solv4.place(x=918, y=210)
                    labelsolv4 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv4.place(x=963, y=210)

                    comsolv1 = Combobox(raiz1, width=2,values=["<=",">=","="], state="readonly")
                    comsolv1.place(x=990, y=210)

                    solv1igual =Entry(raiz1, width=5,textvariable=jIR)
                    solv1igual.place(x=1045, y=210)
                    labeligual = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual.place(x=1025, y=210)

                    #otro

                    solv12 =Entry(raiz1, width=5,textvariable=j1R2)
                    solv12.place(x=650, y=232)
                    labelsolv12 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv12.place(x=693, y=232)

                    solv22 =Entry(raiz1, width=5,textvariable=j2R2)
                    solv22.place(x=738, y=232)
                    labelsolv22 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv22.place(x=783, y=232)

                    solv32 =Entry(raiz1, width=5,textvariable=j3R2)
                    solv32.place(x=828, y=232)
                    labelsolv32= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv32.place(x=873, y=232)

                    solv42 =Entry(raiz1, width=5,textvariable=j4R2)
                    solv42.place(x=918, y=232)
                    labelsolv42 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv42.place(x=963, y=232)

                    comsolv12 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv12.place(x=990, y=232)

                    solv2igual =Entry(raiz1, width=5,textvariable=jIR2)
                    solv2igual.place(x=1045, y=232)
                    labeligual2 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual2.place(x=1025, y=232)

                    #otro

                    solv13 =Entry(raiz1, width=5,textvariable=j1R3)
                    solv13.place(x=650, y=254)
                    labelsolv13 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv13.place(x=693, y=254)

                    solv23 =Entry(raiz1, width=5,textvariable=j2R3)
                    solv23.place(x=738, y=254)
                    labelsolv23 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv23.place(x=783, y=254)

                    solv33 =Entry(raiz1, width=5,textvariable=j3R3)
                    solv33.place(x=828, y=254)
                    labelsolv33= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv33.place(x=873, y=254)

                    solv43 =Entry(raiz1, width=5,textvariable=j4R3)
                    solv43.place(x=918, y=254)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=254)

                    comsolv13 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv13.place(x=990, y=254)

                    solv3igual =Entry(raiz1, width=5,textvariable=jIR3)
                    solv3igual.place(x=1045, y=254)
                    labeligual3 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual3.place(x=1025, y=254)

                    #otro

                    solv14 =Entry(raiz1, width=5,textvariable=j1R4)
                    solv14.place(x=650, y=276)
                    labelsolv14 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv14.place(x=693, y=276)

                    solv24 =Entry(raiz1, width=5,textvariable=j2R4)
                    solv24.place(x=738, y=276)
                    labelsolv24 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv24.place(x=783, y=276)

                    solv34 =Entry(raiz1, width=5,textvariable=j3R4)
                    solv34.place(x=828, y=276)
                    labelsolv34= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv34.place(x=873, y=276)

                    solv44 =Entry(raiz1, width=5,textvariable=j4R4)
                    solv44.place(x=918, y=276)
                    labelsolv43 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv43.place(x=963, y=276)

                    comsolv14 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv14.place(x=990, y=276)

                    solv4igual =Entry(raiz1, width=5,textvariable=jIR4)
                    solv4igual.place(x=1045, y=276)
                    labeligual4 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual4.place(x=1025, y=276)

                    #otro

                    solv15 =Entry(raiz1, width=5,textvariable=j1R5)
                    solv15.place(x=650, y=298)
                    labelsolv15 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv15.place(x=693, y=298)

                    solv25 =Entry(raiz1, width=5,textvariable=j2R5)
                    solv25.place(x=738, y=298)
                    labelsolv25 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv25.place(x=783, y=298)

                    solv35 =Entry(raiz1, width=5,textvariable=j3R5)
                    solv35.place(x=828, y=298)
                    labelsolv35= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv35.place(x=873, y=298)

                    solv45 =Entry(raiz1, width=5,textvariable=j4R5)
                    solv45.place(x=918, y=298)
                    labelsolv45 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv45.place(x=963, y=298)

                    comsolv15 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv15.place(x=990, y=298)

                    solv5igual =Entry(raiz1, width=5,textvariable=jIR5)
                    solv5igual.place(x=1045, y=298)
                    labeligual5 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual5.place(x=1025, y=298)

                    #otro

                    solv16 =Entry(raiz1, width=5,textvariable=j1R6)
                    solv16.place(x=650, y=320)
                    labelsolv16 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv16.place(x=693, y=320)

                    solv26 =Entry(raiz1, width=5,textvariable=j2R6)
                    solv26.place(x=738, y=320)
                    labelsolv26 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv26.place(x=783, y=320)

                    solv36 =Entry(raiz1, width=5,textvariable=j3R6)
                    solv36.place(x=828, y=320)
                    labelsolv36= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv36.place(x=873, y=320)

                    solv46 =Entry(raiz1, width=5,textvariable=j4R6)
                    solv46.place(x=918, y=320)
                    labelsolv46 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv46.place(x=963, y=320)

                    comsolv16 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv16.place(x=990, y=320)

                    solv6igual =Entry(raiz1, width=5,textvariable=jIR6)
                    solv6igual.place(x=1045, y=320)
                    labeligual6 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual6.place(x=1025, y=320)

                    #otro

                    solv17 =Entry(raiz1, width=5,textvariable=j1R7)
                    solv17.place(x=650, y=342)
                    labelsolv17 = Label(raiz1, text = "*x1 +" , font=("Arial Bold", 10))
                    labelsolv16.place(x=693, y=342)

                    solv27 =Entry(raiz1, width=5,textvariable=j2R7)
                    solv27.place(x=738, y=342)
                    labelsolv27 = Label(raiz1, text = "*x2 +" , font=("Arial Bold", 10))
                    labelsolv27.place(x=783, y=342)

                    solv37 =Entry(raiz1, width=5,textvariable=j3R7)
                    solv37.place(x=828, y=342)
                    labelsolv37= Label(raiz1, text = "*x3 +" , font=("Arial Bold", 10))
                    labelsolv37.place(x=873, y=342)

                    solv47 =Entry(raiz1, width=5,textvariable=j4R7)
                    solv47.place(x=918, y=342)
                    labelsolv47 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
                    labelsolv47.place(x=963, y=342)

                    comsolv17 = Combobox(raiz1, width=2,values=["<=",">="], state="readonly")
                    comsolv17.place(x=990, y=342)

                    solv7igual =Entry(raiz1, width=5,textvariable=jIR7)
                    solv7igual.place(x=1045, y=342)
                    labeligual7 = Label(raiz1, text = "=" , font=("Arial Bold", 10))
                    labeligual7.place(x=1025, y=342)

                    def terminef():

                        if comsolv1.get()=="<=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 <= float(solv1igual.get()))
                        if comsolv1.get()==">=":
                            solver.Add(float(solv1.get())*x1+float(solv2.get())*x2+float(solv3.get())*x3+float(solv4.get())*x4 >= float(solv1igual.get()))

                        if comsolv12.get()=="<=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 <= float(solv2igual.get()))
                        if comsolv12.get()==">=":
                            solver.Add(float(solv12.get())*x1+float(solv22.get())*x2+float(solv32.get())*x3+float(solv42.get())*x4 >= float(solv2igual.get()))

                        if comsolv13.get()=="<=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 <= float(solv3igual.get()))
                        if comsolv13.get()==">=":
                            solver.Add(float(solv13.get())*x1+float(solv23.get())*x2+float(solv33.get())*x3+float(solv43.get())*x4 >= float(solv3igual.get()))

                        if comsolv14.get()=="<=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 <= float(solv4igual.get()))
                        if comsolv14.get()==">=":
                            solver.Add(float(solv14.get())*x1+float(solv24.get())*x2+float(solv34.get())*x3+float(solv44.get())*x4 >= float(solv4igual.get()))

                        if comsolv15.get()=="<=":
                            solver.Add(float(solv15.get())*x1+float(solv25.get())*x2+float(solv35.get())*x3+float(solv45.get())*x4 <= float(solv5igual.get()))
                        if comsolv15.get()==">=":
                            solver.Add(float(solv15.get())*x1+float(solv25.get())*x2+float(solv35.get())*x3+float(solv45.get())*x4 >= float(solv5igual.get()))

                        if comsolv16.get()=="<=":
                            solver.Add(float(solv16.get())*x1+float(solv26.get())*x2+float(solv36.get())*x3+float(solv46.get())*x4 <= float(solv6igual.get()))
                        if comsolv16.get()==">=":
                            solver.Add(float(solv16.get())*x1+float(solv26.get())*x2+float(solv36.get())*x3+float(solv46.get())*x4 >= float(solv6igual.get()))

                        if comsolv17.get()=="<=":
                            solver.Add(float(solv17.get())*x1+float(solv27.get())*x2+float(solv37.get())*x3+float(solv47.get())*x4 <= float(solv7igual.get()))
                        if comsolv17.get()==">=":
                            solver.Add(float(solv17.get())*x1+float(solv27.get())*x2+float(solv37.get())*x3+float(solv47.get())*x4 >= float(solv7igual.get()))

                        SolveAndPrint(solver, [x1, x2, x3,x4])

                    bterminef = tk.Button(raiz1,text="finalizar", command=terminef)
                    bterminef.place(x=563, y=510)










            btermine = tk.Button(raiz1, height=1, width=1 ,text="Y", command=termine)
            btermine.place(x=482, y=207)

            j=IntVar()
            ec22=Entry(raiz1, width=10,textvariable=j)
            ec22.grid(column=3, row=3)
            btn = Button(raiz1, text="Ingresar ecuaciones", command=clicked)
            btn.grid(column = 4, row = 3)







        if ecnumecu.get()=="5":


            ec10 =Entry(raiz1, width=5,textvariable=j1)
            ec10.place(x=200, y=210)
            labelec10 = Label(raiz1, text = "*x1" , font=("Arial Bold", 10))
            labelec10.place(x=245, y=210)
            int10=int(ec10.get())

            ec11 =Entry(raiz1, width=5,textvariable=j2)
            ec11.place(x=270, y=210)
            labelec11 = Label(raiz1, text = "*x2" , font=("Arial Bold", 10))
            labelec11.place(x=315, y=210)

            ec12 =Entry(raiz1, width=5,textvariable=j3)
            ec12.place(x=340, y=210)
            labelec12 = Label(raiz1, text = "*x3" , font=("Arial Bold", 10))
            labelec12.place(x=385, y=210)

            ec13 =Entry(raiz1, width=5,textvariable=j4)
            ec13.place(x=410, y=210)
            labelec13 = Label(raiz1, text = "*x4" , font=("Arial Bold", 10))
            labelec13.place(x=457, y=210)

            ec14 =Entry(raiz1, width=5,textvariable=j5)
            ec14.place(x=480, y=210)
            labelec14 = Label(raiz1, text = "*x5" , font=("Arial Bold", 10))
            labelec14.place(x=531, y=210)

            def termine():
                if com.get()=="Maximizar":
                   solver.Maximize(int(ec10.get())*x1+float(ec11.get())*x2+float(ec12.get())*x3+float(ec13.get())*x4+float(ec12.get())*x5)
                if com.get()=="Minimizar":
                   solver.Minimize(float(ec10.get())*x1+float(ec11.get())*x2+float(ec12.get())*x3+float(ec13.get())*x4+float(ec12.get())*x5)

            btermine = tk.Button(raiz1, height=1, width=1 ,text="Y", command=termine)
            btermine.place(x=554, y=207)







    #def clicked1():









    labelnumecu = Label(raiz1, text = "Ingresar cantidad de variables" , font=("Arial Bold", 10))
    labelnumecu.grid(column = 0, row = 3)
    ecnumecu =Entry(raiz1, width=5)
    ecnumecu.grid(column = 1, row = 3)
    btnnum= Button(raiz1, text="Hecho", command=numvarc)
    btnnum.grid(column = 2, row = 4)

















    raiz1.mainloop()


def SolveAndPrint(solver, variable_list):
    raiz=Tk()
    raiz.geometry("750x550")
    raiz.title("Interfaz Soluciones PEM")


    solver.SetNumThreads(8)
    result_status = solver.Solve()


    assert result_status == pywraplp.Solver.OPTIMAL

    assert solver.VerifySolution(1e-7, True)



    Label2=Label(raiz, text="solución al problema", font=("Arial Bold", 20))
    Label2.grid(column = 1, row = 0)
    ec1 = Entry(raiz, justify=RIGHT)

    varle=str(solver.Objective().Value())
    label = Label(raiz, text = 'Valor optimo: ', font=("Arial Bold", 15))
    label.grid(column = 1, row = 5)
    labelvp = Label(raiz, text = varle, font=("Arial Bold", 15))
    labelvp.grid(column = 1, row = 6)
    label = Label(raiz, text = 'Variables y soluciones: ', font=("Arial Bold", 15))
    label.grid(column = 0, row = 5)

    entero=6

    for variable in variable_list:

        varn=str(variable.name())
        vars=str(variable.solution_value())
        labelx1 = Label(raiz, text = varn + "= " + vars , font=("Arial Bold", 15))
        labelx1.grid(column = 0, row = entero)
        entero=entero+1



















    raiz.mainloop()



def Announce(solver, api_type):
    print('---- Problema programacion mixto' + ' -----')


def RunAllIntegerExampleNaturalLanguageAPI():

    if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
        Announce('CBC', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)





def main():
    RunAllIntegerExampleNaturalLanguageAPI()



if __name__ == '__main__':
    main()
