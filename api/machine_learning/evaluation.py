from models import Task, Test, TimeZone, Study
import datetime
import numpy as np
import math

today = datetime.datetime.today()
date_from = today.date() + datetime.timedelta(days=1)

def evaluate(count, dayMax, until_test):
    if until_test.stype == 1:
        return math.exp((count) / float((until_test.start.date() - date_from).days)) if count < (until_test.start.date() - date_from).days else -10
    else:
        return math.exp((dayMax - count) / float((until_test.start.date() - date_from).days)) if count < (until_test.start.date() - date_from).days else -10

def evaluation_func(test_list, task_list, sizeLow):
	sizeCol = len(test_list)
	max_daye = max([tes.start for tes in test_list])
	evaluation_list = []

	""" function """
	for i in range(sizeLow):
		evaluation = []
		for j in range(sizeCol):
			evaluation_value = evaluate(i, sizeCol, test_list[j])
			evaluation_list.append(evaluation_value)

	return evaluation_list

def check_totaltime(study_list):
    pass
