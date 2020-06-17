

from __future__ import print_function

from ortools.linear_solver import pywraplp


def RunIntegerExampleNaturalLanguageAPI(optimization_problem_type):
    """Example of simple integer program with natural language API."""
    solver = pywraplp.Solver('Solucion ejemplo',
                             optimization_problem_type)
    infinity = solver.infinity()
    # x1 and x2 are integer non-negative variables.
    x1 = solver.IntVar(0.0, infinity, 'x1')
    x2 = solver.IntVar(0.0, infinity, 'x2')
    x3 = solver.IntVar(0.0, infinity, 'x3')
    x4 = solver.IntVar(0.0, infinity, 'x4')

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
    print('Number of variables = %d' % solver.NumVariables())
    print('Number of constraints = %d' % solver.NumConstraints())

    solver.SetNumThreads(8)
    result_status = solver.Solve()

    # The problem has an optimal solution.
    assert result_status == pywraplp.Solver.OPTIMAL

    # The solution looks legit (when using solvers others than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
    assert solver.VerifySolution(1e-7, True)

    print('Problem solved in %f milliseconds' % solver.wall_time())

    # The objective value of the solution.
    print('Optimal objective value = %f' % solver.Objective().Value())

    # The value of each variable in the solution.
    for variable in variable_list:
        print('%s = %f' % (variable.name(), variable.solution_value()))

    print('Advanced usage:')
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())


def Announce(solver, api_type):
    print('---- Integer programming example with ' + solver + ' (' + api_type +
          ') -----')


def RunAllIntegerExampleNaturalLanguageAPI():
    if hasattr(pywraplp.Solver, 'GLPK_MIXED_INTEGER_PROGRAMMING'):
        Announce('GLPK', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.GLPK_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
        Announce('CBC', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'SCIP_MIXED_INTEGER_PROGRAMMING'):
        Announce('SCIP', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'GUROBI_MIXED_INTEGER_PROGRAMMING'):
        Announce('GUROBI', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.GUROBI_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'CPLEX_MIXED_INTEGER_PROGRAMMING'):
        Announce('CPLEX', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(
            pywraplp.Solver.CPLEX_MIXED_INTEGER_PROGRAMMING)


def RunAllIntegerExampleCppStyleAPI():
    if hasattr(pywraplp.Solver, 'GLPK_MIXED_INTEGER_PROGRAMMING'):
        Announce('GLPK', 'C++ style API')
        RunIntegerExampleCppStyleAPI(
            pywraplp.Solver.GLPK_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
        Announce('CBC', 'C++ style API')
        RunIntegerExampleCppStyleAPI(
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'SCIP_MIXED_INTEGER_PROGRAMMING'):
        Announce('SCIP', 'C++ style API')
        RunIntegerExampleCppStyleAPI(
            pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'GUROBI_MIXED_INTEGER_PROGRAMMING'):
        Announce('GUROBI', 'C++ style API')
        RunIntegerExampleCppStyleAPI(
            pywraplp.Solver.GUROBI_MIXED_INTEGER_PROGRAMMING)
    if hasattr(pywraplp.Solver, 'CPLEX_MIXED_INTEGER_PROGRAMMING'):
        Announce('CPLEX', 'C++ style API')
        RunIntegerExampleCppStyleAPI(
            pywraplp.Solver.CPLEX_MIXED_INTEGER_PROGRAMMING)


def main():
    RunAllIntegerExampleNaturalLanguageAPI()
    


if __name__ == '__main__':
    main()
