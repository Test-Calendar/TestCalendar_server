import cvxpy
import numpy as np

def binary(size, weight, capacity):
	result = []
	for i in size:
		x = cvxpy.Int(i.shape[0])
		objective = cvxpy.Maximize(weight * x)
		#
		constraints = [capacity >= size * x]
		constraints += [x >= 0, x <= 1]
		#
		prob = cvxpy.Problem(objective, constraints)
		prob.solve(solver=cvxpy.ECOS_BB)
		result.append([round(ix[0, 0]) for ix in x.value])

	return result

if __name__ == "__main__":
	binary()
