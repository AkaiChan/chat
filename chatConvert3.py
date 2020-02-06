lines = []
with open("3.txt", "r", encoding= "utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(" ")
	strtime = s[0][:5]
	strPerson = s[0][5:]
	print(strtime, " ", strPerson, " ", s[1:])

