from models import Task, Test, TimeZone, Study
import datetime
import numpy as np
import math

today = datetime.datetime.today()
date_from = today.date() + datetime.timedelta(days=1)

def evaluate(count, until_test):
    if until_test.stype == 1:
        return math.exp((count + 1) / float((until_test.start.date() - date_from).days)) if count + 1 < (until_test.start.date() - date_from).days else -10
    else:
        return 2 * math.exp((count + 1) / float((until_test.start.date() - date_from).days)) if count + 1 < (until_test.start.date() - date_from).days else -10

def evaluation_func(test_list, task_list, sizeLow):
	sizeCol = len(test_list)
	max_daye = max([tes.start for tes in test_list])
	evaluation_list = []

	""" function """
	for i in range(sizeLow):
		evaluation = []
		for j in range(sizeCol):
			evaluation_value = evaluate(i, test_list[j])
			evaluation_list.append(evaluation_value)

	return evaluation_list

def check_totaltime(study_list):
    pass
