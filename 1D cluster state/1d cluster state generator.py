nq = [10, 12, 14, 16, 18]
output = {}

# generate sequence of cz gate for 1d cluster state
for n in nq:
    output[f"{n}"] = [[(i, i+1) for i in range(n-1)]]

with open('1d cluster state gate.py', 'w') as f:
    f.write("gates = " + output.__str__() + "\n")