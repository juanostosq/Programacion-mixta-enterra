

from __future__ import print_function

from ortools.linear_solver import pywraplp

from tkinter import *

import sys


def RunIntegerExampleNaturalLanguageAPI(optimization_problem_type):


    solver = pywraplp.Solver('Solucion ejemplo',
                             optimization_problem_type)
    infinity = solver.infinity()
    #se escribe cada variable se inicializa en cero, y se comprueba que nosea negativa
    x1 = solver.NumVar(0.0, infinity, 'x1')
    x2 = solver.NumVar(0.0, infinity, 'x2')
    x3 = solver.IntVar(0.0, infinity, 'x3')

    #ecuacion a optimizar Z= 4x1-2x2+7x3-1x4
    solver.Maximize(7000*x1+7300*x2+7500*x3)
    # -1 * x21 + 3 * x <= 10.


    solver.Add(510.75*x1 + 515.85*x2 + 500.10*x3 <=200000000)
    solver.Add(510.75*x1 + 515.85*x2 + 500.10*x3 <=100000000)
    solver.Add(50.5*x1 + 51.5*x2 + 50.75*x3 <=1800000)
    solver.Add( 1* x1 >= 5600)
    solver.Add( 1* x2 >= 7500)


    SolveAndPrint(solver, [x1, x2,x3])






def SolveAndPrint(solver, variable_list):
    raiz=Tk()
    raiz.geometry("750x550")
    raiz.title("Interfaz Soluciones PEM")
    """Solve the problem and print the solution."""
    print('Numero de variables = %d' % solver.NumVariables())
    print('Numero de ecuaciones = %d' % solver.NumConstraints())

    solver.SetNumThreads(8)
    result_status = solver.Solve()


    assert result_status == pywraplp.Solver.OPTIMAL

    assert solver.VerifySolution(1e-7, True)

    print('Problema resuelto en %f milisgundos' % solver.wall_time())


    print('Valor optimo = %f' % solver.Objective().Value())

    img=PhotoImage(file="/home/juan/Documentos/Semestre 2020-1/IO/Codigo python/ud.png")
    Label1=Label(raiz, image=img).grid(column = 0, row = 0)
    Label2=Label(raiz, text="Programación mixta entera", font=("Arial Bold", 20))
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
        print('%s = %f' % (variable.name(), variable.solution_value()))
        varn=str(variable.name())
        vars=str(variable.solution_value())
        labelx1 = Label(raiz, text = varn + "= " + vars , font=("Arial Bold", 15))
        labelx1.grid(column = 0, row = entero)
        entero=entero+1

















    raiz.iconphoto(True, PhotoImage(file="/home/juan/Documentos/Semestre 2020-1/IO/Codigo python/ud.png"))

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
