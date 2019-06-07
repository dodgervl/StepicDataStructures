stack = []
max_stack =[]
def get_max(querie):
	if querie[:3] == 'pop':
		stack.pop()
		max_stack.pop()
	elif querie[:3] == 'pus':
		element = int(querie.split(' ')[1])
		stack.append(element)
		if not max_stack:
			#print('first')
			max_stack.append(element)
			#print(max_stack)
		else:
			max_stack.append(max(element,max_stack[-1]))
			#print(stack,max_stack,element)
	elif querie[:3] == 'max':
		print(max_stack[-1])

n = int(input())
for i in range(n):
	querie = input()
	get_max(querie)