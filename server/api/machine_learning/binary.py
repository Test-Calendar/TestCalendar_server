import cvxpy
import numpy as np

def knapsack(size, weight, capacity):
	x = cvxpy.Int(size.shape[0])
	objective = cvxpy.Maximize(weight * x)
	constraints = [capacity >= size * x]
	constraints += [x >= 0, x <= 2]
	prob = cvxpy.Problem(objective, constraints)
	prob.solve(solver=cvxpy.ECOS_BB)
	result = [round(ix[0, 0]) for ix in x.value]

	return result

if __name__ == "__main__":
	knapsack()
