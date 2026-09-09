# first, pip install qiskit qiskit-aer qiskit-ibm-runtime matplotlib pylatexenc

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

qc.h(0) # apply a Hadamard gate to create superpositions
qc.measure_all() # add measurement options to all quibits
#qc.draw("mpl") # draw the circuit

# Run the circuit on a simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print(counts) # raw data output in dictionary format
# test run: {'0': 491, '1': 533} (expect different values)