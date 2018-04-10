# -*- coding: utf-8 -*-

def num_paths_to_top(height, possible_steps):
	"""
	Given the height of a staircase n, and a list of possible steps you
	can take at a time, calculate the number of possible paths
	you can take to reach the top of the staircase.

	For example, given a height 3, and the possible steps [1, 2, 3],
	there would be 4 possible ways to climb the staircase"
	[1,1,1]
	[1,2]
	[2,1]
	[3]

	Args:
		height: The height of the staircase
		possible_steps: A list of integer value for the number of steps
		we can climb at a time.

	Returns:
		The total number of possible paths we can take to the top.
	"""

	memoized = [None] * (height + 1)

	# We use an inner function to capture the memoization table
	def _num_paths_to_top(height, possible_steps):

		# If we are at the top, then we terminate the recursion.
		if height < 1:
			return 0

		# Do we already know the possible steps at this height?
		if memoized[height] is not None:
			return memoized[height]

		# The remaining combinations will be 1 (for this step),
		# plus all the possible remaining steps we can take.
		combos = 1
		for i in possible_steps:
			# Do not bother checking steps that are larger than the remaining height,
			# they will return 0 anyway.
			if i <= height:
				combos = combos + _num_paths_to_top(height - i, possible_steps)

		# Store the possible steps for this height for future calculations
		memoized[height] = combos
		return combos

	return _num_paths_to_top(height, possible_steps)

assert num_paths_to_top(3, [1, 2, 3]) == 4