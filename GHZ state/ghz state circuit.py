from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from math import pi


simulator = AerSimulator()
circuit = QuantumCircuit(5, 5)

# build circuit, for 5 qubits
# for i in range(5):
#     circuit.h(i)
# circuit.barrier()
# for i in range(4):
#     circuit.cz(0, i+1)
#     circuit.barrier()
# for i in range(4):
#     circuit.h(i+1)
# circuit.barrier()
# circuit.measure_all()

for i in range(5):
    circuit.ry(pi/2, i)
    circuit.rx(pi, i)
for i in range(4):
    circuit.cz(0, i+1)
for i in range(4):
    circuit.ry(pi/2, i+1)
    circuit.rx(pi, i+1)
circuit.barrier()
circuit.measure_all()

# compile, run, ang get results
compile_circuit = transpile(circuit, simulator, optimization_level=0)
job = simulator.run(compile_circuit, shots=1000)
result = job.result()
counts = result.get_counts(compile_circuit)
print(counts)

# circuit.draw(output='mpl', filename=f'ghz.png')


