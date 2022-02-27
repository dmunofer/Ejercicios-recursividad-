# Ejercicio 5

def busqueda_dico(table, i, j_low,
				j_high, x):

	while (j_low <= j_high):
		j_mid = (j_low + j_high) // 2

		if (table[i][j_mid] == x):
			return(i,j_mid)

		elif (table[i][j_mid] > x):
			j_high = j_mid - 1

		else:
			j_low = j_mid + 1

	return(None)

def sortedMatrixSearch(table, n, m, x):

	if (n == 1):
		busqueda_dico(table, 0, 0, m - 1, x)
		return (0,0)

	i_high = n - 1
	j_mid = m // 2
	while ((i_low + 1) < i_high):
		i_mid = (i_low + i_high) // 2
		if (table[i_mid][j_mid] == x):
			return( i_mid,j_mid)

		elif (table[i_mid][j_mid] > x):
			i_high = i_mid

		else:
			i_low = i_mid

	if(table[i_low][j_mid] == x):
		return( i_low, j_mid)

	elif(table[i_low + 1][j_mid] == x):
		return(i_low + 1, j_mid)

	elif(x <= table[i_low][j_mid - 1]):
		busqueda_dico(table, i_low, 0, j_mid - 1, x)

	elif(x >= table[i_low][j_mid + 1] and x <= table[i_low][m - 1]):
	    busqueda_dico(table, i_low, j_mid + 1, m - 1, x)