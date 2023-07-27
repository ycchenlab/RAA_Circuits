'''
need more investigation!!! There may be a more efficient way to implement the surface code.
'''

from qiskit import QuantumCircuit, transpile, execute, Aer
from math import pi
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

circuit = QuantumCircuit(19, 19)
backend = Aer.get_backend("qasm_simulator")
 
def surface_code(*args, ancilla: int):
    if len(args) < 3 or len(args) > 4:
        raise Exception("Invalid number of arguments")

    # single qubit gate
    circuit.ry(pi/2, ancilla)
    for i in args:
        circuit.ry(pi/2, i)
    # CZ gate
    for i in args:
        circuit.cz(i, ancilla)
    circuit.ry(pi/2, ancilla)

surface_code(0, 3, 5, ancilla=13)
surface_code(1, 3, 4, 6, ancilla=14)
surface_code(2, 4, 7, ancilla=15)
surface_code(5, 8, 10, ancilla=16)
surface_code(6, 8, 9, 11, ancilla=17)
surface_code(7, 9, 12, ancilla=18)

circuit.draw('mpl')

# stabilizer
from qiskit.quantum_info import Statevector, StabilizerState, Pauli
stab = StabilizerState(circuit)
print(stab)

# job_sim = backend.run(transpile(circuit, backend), shots=5000)
#
# # Grab the results from the job.
# result_sim = job_sim.result()
#
# counts = result_sim.get_counts(circuit)
# print(counts)
#
# plot_histogram(counts)