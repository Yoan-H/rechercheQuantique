from qiskit import QuantumCircuit, Aer, execute
from qiskit.providers.aer import QasmSimulator

# Fonction pour créer une porte d'oracle
def oracle(qc, n):
    for i in range(n-1):
        qc.cx(i, n-1)

# Fonction pour créer l'algorithme de Grover
def grover(n):
    # Initialisation du circuit
    qc = QuantumCircuit(n, n-1)

    # Préparation de l'état |s>
    for i in range(n):
        qc.h(i)

    # Nombre d'itérations
    k = 2

    # Algorithme de Grover
    for i in range(k):
        oracle(qc, n)
        for j in range(n):
            qc.h(j)
            qc.x(j)
        qc.h(n-1)
        qc.mct(list(range(n-1)), n-1)
        qc.h(n-1)
        for j in range(n):
            qc.x(j)
            qc.h(j)
    
    qc.measure(list(range(n-1)), list(range(n-1)))

    return qc

# Exécution de l'algorithme
qc = grover(2)
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()

print(result.get_counts(qc))
