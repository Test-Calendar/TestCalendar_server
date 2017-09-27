import numpy as np
# import onemax as ga
import binary as binary
import cvxpy

def evaluation_value (value):
	if (x > 0.5):
		return x
	else:
		return 1 - x

def main():
	size = np.array([21, 11, 15, 9, 34, 25, 41, 52])
	weight = np.array([22, 12, 16, 10, 35, 26, 42, 53])
	capacity = 100

	print("result", binary.knapsack(size, weight, capacity))

if __name__ == "__main__":
	main()
