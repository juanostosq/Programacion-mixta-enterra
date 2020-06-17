

from __future__ import print_function

from ortools.linear_solver import pywraplp


def RunIntegerExampleNaturalLanguageAPI(optimization_problem_type):
    """Example of simple integer program with natural language API."""
    solver = pywraplp.Solver('Solucion ejemplo',
                             optimization_problem_type)
    infinity = solver.infinity()
    #se escriba cada variable se inicializa en cero, y se comprueba que nosea negativa
    x1 = solver.IntVar(0.0, infinity, 'x1')
    x2 = solver.IntVar(0.0, infinity, 'x2')
    x3 = solver.IntVar(0.0, infinity, 'x3')
    x4 = solver.IntVar(0.0, infinity, 'x4')
    #ecuacion a optimizar Z= 4x1-2x2+7x3-1x4
    solver.Maximize(4*x1 + -2 * x2 + 7 * x3 - 1*x4)

    solver.Add(1 * x1 + 5 * x3 <= 10)
    solver.Add(1 * x1 + 1 * x2 + -1 * x3 <= 1)
    solver.Add(6 * x1 + -5 * x2 <= 0)
    solver.Add(-1 * x1 + 2 * x3 - 2* x4 <= 3)


    SolveAndPrint(solver, [x1, x2,x3,x4])


def RunIntegerExampleCppStyleAPI(optimization_problem_type):
    """Example of simple integer program with the C++ style API."""
    solver = pywraplp.Solver('RunIntegerExampleCppStyleAPI',
                             optimization_problem_type)
    infinity = solver.infinity()

    x1 = solver.IntVar(0.0, infinity, 'x1')
    x2 = solver.IntVar(0.0, infinity, 'x2')
    x3 = solver.IntVar(0.0, infinity, 'x3')
    x4 = solver.IntVar(0.0, infinity, 'x4')


    objective = solver.Objective()
    objective.SetCoefficient(x1, 4)
    objective.SetCoefficient(x2, -2)
    objective.SetCoefficient(x3, 7)
    objective.SetCoefficient(x4, -1)


    ct = solver.Constraint(10, -infinity)
    ct.SetCoefficient(x1, -1)
    ct.SetCoefficient(x3, 5)

    # -1 * x21 + 3 * x <= 10.
    ct = solver.Constraint(1, -infinity)
    ct.SetCoefficient(x1, 1)
    ct.SetCoefficient(x2, 1)
    ct.SetCoefficient(x3, -1)

    ct = solver.Constraint(0, -infinity)
    ct.SetCoefficient(x1, 6)
    ct.SetCoefficient(x2, -5)

    ct = solver.Constraint(3, -infinity)
    ct.SetCoefficient(x1, -1)
    ct.SetCoefficient(x3, 2)
    ct.SetCoefficient(x4, -2)

    SolveAndPrint(solver, [x1, x2,x3,x4])


def SolveAndPrint(solver, variable_list):
    """Solve the problem and print the solution."""
    print('Numero de variables = %d' % solver.NumVariables())
    print('Numero de ecuaciones = %d' % solver.NumConstraints())

    solver.SetNumThreads(8)
    result_status = solver.Solve()


    assert result_status == pywraplp.Solver.OPTIMAL

    assert solver.VerifySolution(1e-7, True)

    print('Problema resuelto en %f milisgundos' % solver.wall_time())


    print('Valor optimo = %f' % solver.Objective().Value())


    for variable in variable_list:
        print('%s = %f' % (variable.name(), variable.solution_value()))




def Announce(solver, api_type):
    print('---- Problema programacion mixto' + solver + ' (' + api_type +
          ') -----')


def RunAllIntegerExampleNaturalLanguageAPI():

    if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
        Announce('CBC', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)



def main():
    RunAllIntegerExampleNaturalLanguageAPI()



if __name__ == '__main__':
    main()
