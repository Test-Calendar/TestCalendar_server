from models import Task, Test, TimeZone, Study
import datetime
import numpy as np
import math

def evaluate(count, until_test):
    return math.exp((count + 1) / float(until_test.days)) if count + 1 < until_test.days else -3

def evaluation_func(test_list, task_list, sizeLow):
	today = datetime.datetime.today()
	sizeCol = len(test_list)
	max_daye = max([tes.start for tes in test_list])
	evaluation_list = []

	""" function """
	for i in range(sizeLow):
		evaluation = []
		for j in range(sizeCol):
			evaluation_value = evaluate(i, test_list[j].start - today)
			# evaluation.append(evaluation_value)
			evaluation_list.append(evaluation_value)
		# evaluation_list.append(evaluation)

	return evaluation_list

def check_totaltime(study_list):
    pass
