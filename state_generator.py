'''
Algorithms: 1D cluster states, GHZ states, 7 qubit steane code, 13+6 surface code
output: QuantumCircuit object from Qiskit
'''
from qiskit import QuantumCircuit
from math import pi


def cluster_state(n: int):
    circuit = QuantumCircuit(n)

    for i in range(n):
        circuit.ry(pi / 2, i)
    for i in range(n-1):
        circuit.cz(i, i + 1)
    for i in range(n):
        if i % 2 == 0:
            circuit.ry(pi / 2, i)
    return circuit

def ghz_state(n: int):
    # the phase shift of e^i\phi |1^n> originates from Rz(phi) on |+>
    circuit = QuantumCircuit(n)

    # H - 4 types of decomposition - xy^1/2, y^-1/2x, zy^-1/2, y^1/2z
    for i in range(n):
        circuit.ry(pi / 2, i)
        circuit.rx(pi, i)
    for i in range(n-1):
        circuit.cz(0, i + 1)
    for i in range(n-1):
        circuit.ry(pi / 2, i + 1)
        circuit.rx(pi, i+1)
    return circuit

def steane_code():
    # 7 qubit steane code
    circuit = QuantumCircuit(7)

    for i in range(7):
        circuit.ry(pi / 2, i)
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
    ###
    circuit.ry(pi / 2, 1)
    circuit.ry(pi / 2, 2)
    circuit.ry(pi / 2, 5)
    circuit.ry(pi / 2, 6)

    return circuit

def surface_code():
    # 13+6 surface code, need more efficient, general way to construct
    circuit = QuantumCircuit(19)
    def func(*args, ancilla: int):
        if len(args) < 3 or len(args) > 4:
            raise Exception("Invalid number of arguments")

        # single qubit gate
        circuit.ry(pi / 2, ancilla)
        for i in args:
            circuit.ry(pi / 2, i)
        # CZ gate
        for i in args:
            circuit.cz(i, ancilla)
        circuit.ry(pi / 2, ancilla)

    func(0, 3, 5, ancilla=13)
    func(1, 3, 4, 6, ancilla=14)
    func(2, 4, 7, ancilla=15)
    func(5, 8, 10, ancilla=16)
    func(6, 8, 9, 11, ancilla=17)
    func(7, 9, 12, ancilla=18)

    return circuit




