def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	result = []

	if mode == "row":
		for row in matrix:
			mean = sum(row)/len(row)
			result.append(mean)

	elif mode == "column":
    	for j in range(len(matrix[0])):
        	column = []

        	for row in matrix:
            	column.append(row[j])

        	result.append(sum(column) / len(column))
	return result