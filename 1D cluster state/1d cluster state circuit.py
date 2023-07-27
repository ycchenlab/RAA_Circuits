from qiskit import QuantumCircuit, transpile, Aer
from qiskit_aer import AerSimulator
from math import pi

circuit = QuantumCircuit(12, 12)
backend = Aer.get_backend("qasm_simulator")

# build the circuit, 12 qubit cluster state
for i in range(12):
    circuit.ry(pi/2, i)
circuit.barrier()
for i in range(11):
    circuit.cz(i, i+1)
circuit.barrier()
for i in range(12):
    if i%2 == 0:
        circuit.ry(pi/2, i)
circuit.barrier()
circuit.measure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11])

print(circuit, 'mpl')

job_sim = backend.run(transpile(circuit, backend), shots=5000)

# Grab the results from the job.
result_sim = job_sim.result()

counts = result_sim.get_counts(circuit)

# for even stabilizers
stabilizers = []
output = {}
for i in range(12):
    if i-1 < 0:
        stabilizers.append((i, i+1))
        output[f'({i}, {i+1})'] = 0
    elif i+1 > 11:
        stabilizers.append((i-1, i))
        output[f'({i-1}, {i})'] = 0
    else:
        stabilizers.append((i-1, i, i+1))
        output[f'({i-1}, {i}, {i+1})'] = 0

for state in counts.keys():
    for stab in stabilizers:
        tmp = 1
        for j in stab:
            if state[j] == '0':
                tmp *= -1
        output[str(stab)] += tmp * counts[state] / 5000
print(output)




