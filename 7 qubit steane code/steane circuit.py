from qiskit import QuantumCircuit, transpile, execute, Aer
from qiskit.visualization import plot_state_city
from math import pi
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

circuit = QuantumCircuit(7, 7)
backend = Aer.get_backend("qasm_simulator")

# build the circuit
for i in range(7):
    circuit.ry(pi/2, i)
circuit.barrier()
###
circuit.cz(0, 1)
circuit.cz(2, 4)
circuit.cz(1, 3)
circuit.cz(0, 2)
circuit.cz(4, 5)
circuit.cz(2, 3)
circuit.cz(4, 6)
circuit.cz(0, 6)
circuit.cz(3, 5)
circuit.barrier()
###
circuit.ry(pi/2, 1)
circuit.ry(pi/2, 2)
circuit.ry(pi/2, 5)
circuit.ry(pi/2, 6)
circuit.barrier()
circuit.measure_all()

print(circuit)

job_sim = backend.run(transpile(circuit, backend), shots=5000)

# Grab the results from the job.
result_sim = job_sim.result()

counts = result_sim.get_counts(circuit)
print(counts)

plot_histogram(counts)