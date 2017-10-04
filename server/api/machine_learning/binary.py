# -*- coding: utf-8 -*-
import cvxpy
import numpy as np

def binary(size, weight, capacity):
	result = []
	count = 0
	for i in size:
		x = cvxpy.Int(i.shape[0])
		objective = cvxpy.Maximize(weight[count] * x)
		#
		constraints = [capacity >= size * x]
		constraints += [x >= 0, x <= 1]
		# constraints += [objective < 100]
		#
		prob = cvxpy.Problem(objective, constraints)
		prob.solve(solver=cvxpy.ECOS_BB)
		result.append([round(ix[0, 0]) for ix in x.value])
		count += 1

	return result
