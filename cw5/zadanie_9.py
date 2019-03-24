from itertools import combinations


lista = ['python', 'cpp', 'html', 'css', 'scss', 'typescript', 'dluga wyspa zimna herbata']

for i in combinations(lista, 3):
    print(i)
