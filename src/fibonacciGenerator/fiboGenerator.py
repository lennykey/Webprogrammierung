'''
Generatorfunktion fuer Fibonaccizahlen
'''


def fibogen():
	step0 = 0
	step1 = 1
	
	step2 = step0 + step1

	counter = 0
	while True:
		
		if counter == 0:
			yield 0
			counter += 1
		elif counter == 1:
			yield 1
			counter += 1
		else:
			yield step2
			step0 = step1
			step1= step2
			
			step2 = step0 + step1
		
	
if __name__ == "__main__": 

	for i, fibo in enumerate(fibogen()):
		if i > 6:
			break
		print fibo