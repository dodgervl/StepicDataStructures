def check(s):
	stack = []
	d ={'(':')','{':'}','[':']'}
	parentheses = ['(','{','[',')','}',']']
	print(type(s))
	for i in range(0,len(s)):
		if s[i] in parentheses:
			# opening parentheses
			if s[i] in parentheses[:3]:
				if len(stack)==0: idx = i
				stack.append(s[i])
			# closing parentheses
			else:
				if len(stack)==0 or d[stack.pop()] != s[i]:
					print('empty stack')
					return i+1 #index starts from 1
	if len(stack)!=0: return idx+1
	return "Success"
s = input()
a = check(s)
print(a)