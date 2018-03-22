# -*- coding: utf-8 -*-
import sys

def max_sum_nonadjacent_pair(values):
	"""
	This method finds the maximum sum of a pair of non-adjacent
	numbers in a given sequence. It runs in O(n) time.

	We find the 4 maximum elements in the array, of which two elements
	must be non-adjacent in the original sequence. We then take the
	sum of each possible combination.

	Args:
		values: A iterable sequence of numbers

	Returns:
		The maximum sum of a pair of non-adjacent numbers from a given
		sequence.
	"""

	if len(values) < 3:
		raise Error("Must be at least 3 elements in the sequence.")

	max1 = -1 * sys.maxint - 1
	max2 = -1 * sys.maxint - 1
	max3 = -1 * sys.maxint - 1
	max4 = -1 * sys.maxint - 1

	max1_idx = 0
	max2_idx = 0
	max3_idx = 0
	max4_idx = 0

	for idx in xrange(0, len(values)):
		
		value = values[idx]

		if value > max1:
			max4 = max3
			max4_idx = max3_idx

			max3 = max2
			max3_idx = max2_idx

			max2 = max1
			max2_idx = max1_idx

			max1 = value
			max1_idx = idx

		elif value > max2:
			max4 = max3
			max4_idx = max3_idx

			max3 = max2
			max3_idx = max2_idx

			max2 = value
			max2_idx = idx

		elif value > max3:
			max4 = max3
			max4_idx = max3_idx

			max3 = value
			max3_idx = idx

		elif value > max4:
			max4 = value
			max4_idx = idx

	return max(
		(max1 + max2) if abs(max1_idx - max2_idx) > 1 else None,
		(max1 + max3) if abs(max1_idx - max3_idx) > 1 else None,
		(max1 + max4) if abs(max1_idx - max4_idx) > 1 else None,
		(max2 + max3) if abs(max2_idx - max3_idx) > 1 else None,
		(max2 + max4) if abs(max2_idx - max4_idx) > 1 else None,
		(max3 + max4) if abs(max3_idx - max4_idx) > 1 else None
	)

assert max_sum_nonadjacent_pair([2, 4, 2, 8, 9, 10, 12, 14]) == 24
assert max_sum_nonadjacent_pair([5, 1, 1, 5]) == 10
assert max_sum_nonadjacent_pair([-2, -3, -1, -5, 8]) == 7