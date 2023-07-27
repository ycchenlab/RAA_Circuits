nq = [5, 6, 7, 8, 9, 10, 11, 12]
output = {}

# cz gate (control, target)
for i in nq:
    tmp = [(j, j+1) for j in range(i-1)]
    output[f"{i}"] = tmp

with open("ghz gate.py", "w") as f:
    f.write("gates = " + output.__str__() + "\n")
