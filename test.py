from state_generator import *
from gate_sequence_generator import *

circuit = ghz_state(5)
print(circuit)
output = gate_sequence(circuit)
print(output)