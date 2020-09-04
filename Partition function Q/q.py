from math import sqrt
from functools import lru_cache


class Q:

	@lru_cache()
	def calculate_q(n):
		"""
		Q partitioning function
		"""
		if n == 0:
			return 1

		else:
			sum_upper_limit = int(sqrt(n))
			temp_sum = sum((-1)**(k + 1) * Q.calculate_q(n - k**2) for k in range(1, sum_upper_limit + 1))
			return Q.check_s(n) + 2 * temp_sum

	def check_s(n):
		"""
		Check if n is in dict and get result
		"""
		temp_dict = Q.calculate_s(n)

		if n in temp_dict:
			return (-1)**temp_dict[n]
		else:
			return 0

	def calculate_s(n):
		
		result_dict = {}
		j = 0
		minus_part = -1

		while minus_part <= n:
			j_first = 3 * j**2
			plus_part = (j_first + j) // 2
			minus_part = (j_first - j) // 2
			result_dict[plus_part] = j
			result_dict[minus_part] = j
			j += 1

		return result_dict

	@staticmethod
	def q(n):
		return Q.calculate_q(n) - 1


"""
Test
"""
if __name__ == "__main__":
	for i in range(1, 101):
		print(i, "->", Q.q(i))
