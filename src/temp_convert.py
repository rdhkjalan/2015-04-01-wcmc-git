def f_to_K(temp):
	return ((temp - 32) * (5.0 / 9.0)) + 273.15
def K_to_c(temp):
	return (temp - 273)

def f_to_c(temp):
	temp_K = f_to_K(temp)
	results = K_to_c(temp_K)
	return(result)

