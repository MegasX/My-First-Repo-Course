lst = [8, 6, 41, 41, 6, 8, 9, 1]
d = {}


for el in lst:
	if el in d:
		d[el] += d.setdefault(el, 0) + 1

for k, v in d.items():
	if v > 1:
		print(k)




OR ------------------------------------------------------------------------


lst = [8, 6, 4, 3, 2, 9, 13]

seen = set()
dups = set()

for el in lst:
	if el in seen:
		dups.add(el)
	else:
		seen.add(el)

print(dups)



OR--------------------------------------------------------------------------
















