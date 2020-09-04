class UnequalWidthError(Exception):
	pass


class Path:

	def __init__(self, matrix):
		for element in matrix:
			if not isinstance(element, list):
				raise TypeError(f"Expected matrix (list of lists), got {type(element)} ")

		self.matrix = matrix
		self.paths = []
		self.paths_lenght = []
		self.neighbours = []
		self.rows = 0
		self.cols = 0

		self.set_rows_and_cols()

	def run_alghorithm(self):

		if not self.matrix:
			return []

		if not self.cols:
			self.vector_matrix()

		else:
			for i in range(self.rows):
				for j in range(self.cols[i]):
					if self.check_path((i, j)):
						if self.matrix[i][j]:
							self.paths.append(self.get_path_size(i, j)[:])
			self.set_paths_lenght()

		return self.get_paths_lenght()

	def set_rows_and_cols(self):
		self.rows = len(self.matrix)
		if self.rows > 1:
			self.cols = [len(row) for row in self.matrix]
			if len(set(self.cols)) > 1:
				raise UnequalWidthError (f"expected matrix with equal width, got width -> {set(self.cols)}")

	def vector_matrix(self):
		path_counter = 0
		for i in range(len(self.matrix[0])):
			if self.matrix[0][i]:
				path_counter += 1
			else:
				if path_counter:
					self.paths_lenght.append(path_counter)
					path_counter = 0
		if path_counter:
			self.paths_lenght.append(path_counter)

	def get_path_size(self, i, j):

		path = self.append_neighbours(i, j)

		if path:
			current_path = path[:]
			path = []
			return current_path
		else:
			return []

	def append_neighbours(self, i, j, path=[]):
		"""
		iterate through matrix until False is hit, if adjacent True vortexes are present
		call "find_neighbours"
		"""
		neighbours = []

		while self.matrix[i][j]:

			if (i, j) not in path:
				path.append((i, j))

			if i == 0:
				if self.matrix[i+1][j] and (i+1, j) not in path:
					neighbours.append((i+1, j))
			elif i == self.rows - 1:
				if self.matrix[i-1][j] and (i-1, j) not in path:
					neighbours.append((i-1, j))
			else:
				if self.matrix[i+1][j] and (i+1, j) not in path:
					neighbours.append((i+1, j))
				if self.matrix[i-1][j] and (i-1, j) not in path:
					neighbours.append((i-1, j))

			if j == 0:
				if self.matrix[i][j+1] and (i, j+1) not in path:
					neighbours.append((i, j+1))
			elif j == self.cols[i]-1:
				if self.matrix[i][j-1] and (i, j-1) not in path:
					neighbours.append((i, j-1))
			else:
				if self.matrix[i][j-1] and (i, j-1) not in path:
					neighbours.append((i, j-1))
				if self.matrix[i][j+1] and (i, j+1) not in path:
					neighbours.append((i, j+1))

			if j < self.cols[i] - 1:
				j += 1
			else:
				break

		if neighbours:
			self.find_neighbours(neighbours, path)

		current_path = path[:]
		path = []
		return current_path

	def find_neighbours(self, neighbours, path):
		"""
		while there are "adjacent" vortexes append them to the current path
				and remove them from neighbours list
		"""

		while neighbours:
			current_neighbour = neighbours[0]
			if neighbours[0] not in path:
				path.append(neighbours[0])

			neighbours.remove(current_neighbour)

			self.append_neighbours(current_neighbour[0], current_neighbour[1], path)

	def check_path(self, element):

		for path in self.paths:
			if element not in path:
				pass
			else:
				return False

		return True

	def set_paths_lenght(self):
		"""
		get lenghts of independant paths
		"""
		for i, path in enumerate(self.paths):
			if i:
				self.paths_lenght.append(len(path) - len(self.paths[i-1]))
			else:
				self.paths_lenght.append(len(path))

	def get_paths_lenght(self):
		return self.paths_lenght


"""
Test
"""
if __name__ == "__main__":

	matrix = [
		[1, 0, 0, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 1],
		[1, 0, 0, 0, 1],
		[1, 0, 1, 1, 1],
		[1, 1, 0, 0, 1]
	]

	matrix_2 = [
		[1, 1, 1, 0, 0],
		[0, 1, 1, 0, 0],
		[0, 1, 1, 0, 0],
		[0, 1, 0, 1, 0],
		[0, 1, 1, 1, 1],
		[0, 0, 0, 1, 0],
		[0, 0, 1, 1, 1]
	]

	matrix_3 = [[1, 1, 0, 1, 1, 0, 0, 1, 1, 1]]

	matrix_4 = [[1, 0],
				[0, 1],
				[1, 0]
				]

	matrix_5 = [[]]

	new_path = Path(matrix)
	print(new_path.run_alghorithm())
