from BiQuadraticEquation import BiQuadraticEquation

file_names = ("input01.txt", "input02.txt", "input03.txt")

for file_name in file_names:
    with open(file_name, 'r') as file:

        for line in file:
            line = [int(d) for d in line.split()]
            if len(line) == 2:
                pass
