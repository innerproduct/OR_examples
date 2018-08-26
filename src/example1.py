from ortools.linear_solver import pywraplp

def main():
  solver = pywraplp.Solver('SolverSimpleSystem',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
  x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
  y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')
  
  constraint1 = solver.Constraint(-solver.infinity(), 14)
  constraint1.SetCoefficient(x, 1)
  constraint1.SetCoefficient(y, 2)

  constraint2 = solver.Constraint(0, solver.infinity())
  constraint2.SetCoefficient(x, 3)
  constraint2.SetCoefficient(y, -1)

  constraint3 = solver.Constraint(-solver.infinity(), 2)
  constraint3.SetCoefficient(x, 1)
  constraint3.SetCoefficient(y, -1)

  objective = solver.Objective()
  objective.SetCoefficient(x, 3)
  objective.SetCoefficient(y, 4)
  objective.SetMaximization()

  solver.Solve()
  opt_solution = 3*x.solution_value() + 4*y.solution_value()
  print('Solution:')
  print('x = ', x.solution_value())
  print('y = ', y.solution_value())
  print('optimal objective value =', opt_solution)
if __name__ == '__main__':
  main()
