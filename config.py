import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

private = {}

try:
	file = open(dir_path+"config").read().strip().split('\n')

	for line in file:
		line = line.strip()
		if (len(line) == 0):
			continue
		if (line[0] == '#'):
			continue
		try:
			line = line.split('=')
			key = line[0].strip()
			value = line[1].strip().strip('"')
			private[key] = value
		except Exception as e:
			print(e)
			continue


except Exception as e:
	print(e)


def get():
	if (len(private) > 0):
		return private
	print("no keys found")
	return {}


