class MyDemoPy:

	def __init__(self):
		print("new object initiated!")

	def is_prime(self, number):
		for num in range(2, number):
			for x in range(2, num):
				if num%x == 0:
					print(num, 'equals', x, '*', num//x)
					break
		else:
			print(n, "is a prime number")

	def fib(self, number):
		a,b = 0,1
		while(a < number):
			print(a, end=' ')
			a, b = b, a+b
		print()

	def fib2(self, number):
		"""Return a list containing the Fibonacci series up to n."""
		result=[]
		a,b = 0,1
		while(a < number):
			result.append(a)
			a, b = b, a+b
		return result

	def f(a, L=[]):
		L.append(a)
		return L

	def f(a, L=None):
		if L is None:
			L = []
		L.append(a)
		return L

	def cheeseshop(self, kind, *arguments, **keywords):
		print("--Do you have any", kind, "?")
		print("--I'm sorry, we're all out of", kind)
		for arg in arguments:
			print(arg)
		print("-"*40)
		keys=sorted(keywords.keys)
		for kw in keys:
			print(kw, ":", keywords[kw])

	def write_multiple_items(self, file, seperator, *args):
		file.write(seperator.join(args))

	def concat(self, *args, sep="/"):
		"""all formal parameters which occur after the *args parameter are 'keyword-only' arguments"""
		return sep.join(args)

	"""
	unpacking arguments list
	* can be used to unpack list, ** can be used to unpack dictionary
	"""
	def parrot(self, voltage, state='a stiff', action='voom'):
		"""
		d={"voltage":"four million", "state":"bleedin' demised", "action":"VOOM"}
		parrot(**d)
		"""
		print("--This parrot wouldn't", action, end=' ')
		print("if you put", voltage, "volts through it.", end=' ')
		print("E's", state, "!")

	"""
	lambda expressions
	example:
	>>>pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
	>>>pairs.sort(key=lambda pair:pair[1])
	>>>pairs
	"""
	def make_incrementor(self, n):
		return lambda x:x+n

	


