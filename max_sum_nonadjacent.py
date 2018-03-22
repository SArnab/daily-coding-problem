# -*- coding: utf-8 -*-

def max_sum_nonadjacent(values):
	"""
	This method finds the maximum sum of two non-adjacent numbers
	in a given sequence. It runs in O(n) time.

	Args:
		values: A iterable sequence of numbers

	Returns:
		The maximum sum of two non-adjacent numbers in the sequence.
	"""
	prev_max_incl = 0
	prev_max_excl = 0
    
	for i in values:
		# Between the last two maximums, what is the larger one?
		next_max = max(prev_max_incl, prev_max_excl)
        
		# Include the current value in the sum for comparison on the
		# next iteration
		prev_max_incl = prev_max_excl + i

		# Save the running maximum excluding the current value
		# prevent adjacent sums
		prev_max_excl = next_max

	return max(prev_max_incl, prev_max_excl)

assert max_sum_nonadjacent([2, 4, 6, 8]) == 12
assert max_sum_nonadjacent([5, 1, 1, 5]) == 10
assert max_sum_nonadjacent([-2, -3, -1, -5]) == 0
