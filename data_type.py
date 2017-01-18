def data_type( dataType ):
	"""
	This function determines the type of data passed to it
	and performs a certain operation as described for the
	specific data type
	"""
	if isinstance(dataType, basestring):
		return len(dataType)
	elif isinstance(dataType, bool):
		return dataType
	elif isinstance(dataType, int):
		if dataType < 100:
			return "less than 100"
		elif dataType > 100:
			return "more than 100"
		else:
			return "equal to 100"
	elif isinstance(dataType, list):
		try:
			return dataType[2]
		except IndexError:
			return None
	else:
		return "no value"
