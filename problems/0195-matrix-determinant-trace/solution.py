def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:

	n = len(matrix)
	trace = sum(matrix[i][i] for i in range(n))

	def determinant(m):
		size = len(m)
		
		if size == 1:
			return m[0][0]
		elif size == 2:
			return (m[0][0]*m[1][1] - m[0][1]*m[1][0])
		
		det = 0
		for j in range(size):
            minor = [
                row[:j] + row[j+1:]
                for row in m[1:]
            ]
            det += ((-1) ** j) * m[0][j] * determinant(minor)

        return det
	return (determinant(matrix), trace)

