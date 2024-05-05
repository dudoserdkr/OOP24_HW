from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

file_names = ("input01.txt", "input02.txt", "input03.txt")
output_context = ""

for file_name in file_names:
    with open(file_name, 'r') as file:
        TITLE = f"\n\n----------------------------------{file_name}----------------------------------\n\n"

        output_context += TITLE

        equation_number = 1

        for line in file:
            line = [int(d) for d in line.split()]
            if len(line) == 2:
                equation = Equation(*line)

            elif len(line) == 3:
                equation = QuadraticEquation(*line)

            else:
                a = line[0]
                b = line[2]
                c = line[4]
                equation = BiQuadraticEquation(a, b, c)

            output_context += f"{equation_number}. Корені {equation} -> {equation.solve()}\n"

            equation_number += 1

with open('output.txt', 'w', encoding='utf-8') as output:
    output.write(output_context)
