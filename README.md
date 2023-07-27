git # Circuits for Different Algorithms
To evaluate the ability of [RAA system](https://www.nature.com/articles/s41586-022-04592-6), we need to give some circuits or algorithms for future test. 
This is just the prototype code, which can generate several circuits using qiskit and generate the [gate sequence](https://github.com/tbcdebug/OLSQ) of a given circuit. 
This can be further used in optimised layout synthesis of general quantum circuits. 



```python
# state_generator provides circuits such as GHZ, cluster_state (1d), 
# steane code (7 qubit) and surface code (13+6 qubit)
# gate_sequence_generator simply converts circuits into gate sequences
from state_generator import *
from gate_sequence_generator import *

circuit = ghz_state(5)
# This is equivalent to the QuantumCircuit(5) in qiskit
print(circuit)
output = gate_sequence(circuit)
print(output)
# output is in the form of [gate, (gate sequence), (gate type)]

# other kinds of circuits
# circuit = cluster_state(12)
# circuit = steane_code()
# circuit = surface_code()
```

## Acknowledgments

We would like to thank Daniel (Bochen) Tan for their contributions to this project. We have used code from their [repository](https://github.com/tbcdebug/OLSQ) under the terms of the BSD 3-Clause License.

Also, we would like to acknowledge the valuable contributions of the Qiskit team and its community to this project. We have used the Qiskit library [0.43.0] in our work.

Qiskit is an open-source software development kit for quantum computing provided by IBM. You can find the official Qiskit repository [here](https://github.com/Qiskit/qiskit).

## License

This project is licensed under the terms of the [BSD 3-Clause License](https://github.com/tbcdebug/OLSQ/blob/master/LICENSE) and the [Apache License 2.0](LICENSE.txt).


