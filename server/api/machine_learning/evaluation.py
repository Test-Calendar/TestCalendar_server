from models import Task, Test, TimeZone, Study
import ga
import binary as binary
import cvxpy
import datetime
import numpy as np
import random

def evaluation_func(test_list):
	today = datetime.datetime.today()
	sizeCol = len(test_list)
	max_daye = max([tes.start for tes in test_list])
	sizeLow = max_daye - today
	evaluation_list = []

	""" function """
	for i in range(sizeLow.days):
		evaluation = []
		for j in range(sizeCol):
			"""
			evaluation process
			"""
			until_test = test_list[j].start - today
			evaluation_value = ((i + 1) / float(until_test.days)) * 100 if i + 1 < until_test.days else -2
			# evaluation.append(random.randint(1, 50))
			evaluation.append(evaluation_value)
		evaluation_list.append(evaluation)

	return evaluation_list

def check_totaltime(study_list):
    pass
