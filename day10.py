sample = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''.splitlines()

search = {5,2}

with open('input10') as fp:
	sample = fp.readlines()

search = {61,17}

rules = dict()
bots = dict()
outputs = dict()

inst = []
for n, cmd in enumerate(sample):
	if cmd.startswith('value'):
		left, right = cmd.split(' goes to ')
		value = int(left.split()[1])
		bot = int(right.split()[1])
		#print(value,'->',bot)
		if bot in bots:
			bots[bot].append(value)
		else:
			bots[bot] = [value]
	elif cmd.startswith('bot'):
		left, right = cmd.split(' gives ')
		bot = int(left.split()[1])
		left, right = right.split(' and ')
		lh, _, result, num = left.split()
		assert lh == 'low'
		low = (result, int(num))
		lh, _, result, num = right.split()
		assert lh == 'high'
		high = (result, int(num))
		rules[n] = (bot, low, high)
		#print(bot,'->low',low,'->high',high)
	else:
		print('error parsing',cmd)



while rules.keys():
	processed = set()
	for k, v in rules.items():
		bot, low, high = v
		if bot in bots and len(bots[bot]) == 2:
			if all(item in bots[bot] for item in search):
				print('#1',bot)
			# distribute high
			if high[0]=='bot':
				bots[high[1]] = bots.get(high[1],[])+[max(bots[bot])]
			elif high[0]=='output':
				outputs[high[1]] = outputs.get(high[1],[])+[max(bots[bot])]
			else:
				print('error distributing high')
			# distribute low
			if low[0]=='bot':
				bots[low[1]] = bots.get(low[1],[])+[min(bots[bot])]
			elif low[0]=='output':
				outputs[low[1]] = outputs.get(low[1],[])+[min(bots[bot])]
			else:
				print('error distributing high')
			bots[bot] = []
			processed.add(k)
	for k in processed:
		del rules[k]
#print(bots)
#print(outputs)
print('#2',outputs[0][0]*outputs[1][0]*outputs[2][0])