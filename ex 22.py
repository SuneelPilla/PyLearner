filename = 'Names.txt'
with open(filename, 'r') as open_file:
    data = open_file.read()
extract = data.split('\n')
names = set(extract)
R = {}
for i in names:
    c = 0
    for j in extract:
        if i == j:
            c += 1
    #R.append({i,c}) print as a list of Tuples
    R[i] = c #print as a dictionary
print(R)
