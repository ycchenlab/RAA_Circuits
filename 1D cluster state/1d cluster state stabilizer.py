from qiskit import QuantumCircuit, transpile, execute, Aer
from qiskit.visualization import plot_state_city
from math import pi
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector, StabilizerState, Pauli

circuit = QuantumCircuit(12, 12)
backend = Aer.get_backend("qasm_simulator")

# build the circuit, 12 qubit cluster state
for i in range(12):
    circuit.ry(pi/2, i)
circuit.barrier()
for i in range(11):
    circuit.cz(i, i+1)
circuit.barrier()
#
stab = StabilizerState(circuit)
print(stab)

stab_2 = ['+IIIIIIIIIIZX', '+IIIIIIIIIZXZ', '+IIIIIIIIZXZI', '+IIIIIIIZXZII', '+IIIIIIZXZIII', '+IIIIIZXZIIII', '+IIIIZXZIIIII', '+IIIZXZIIIIII', '+IIZXZIIIIIII', '+IZXZIIIIIIII', '+ZXZIIIIIIIII', '+XZIIIIIIIIII']
for s in stab_2:
    print(f"{s}:", stab.expectation_value(Pauli(f"{s.replace('+', '')}")))