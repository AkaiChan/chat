def read_file(strfilename):
	lines = []
	with open(strfilename,"r", encoding= "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == "Allen":
			person = "Allen"
		elif line == "Tom":
			person = "Tom"
		else:
			if person:
				new.append(person + ": " + line)
	return new

def write_function(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n") 


def mainfun():
	lines = read_file("input.txt")
	lines = convert(lines)
	write_function("output2.txt", lines)


mainfun()