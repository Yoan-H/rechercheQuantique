import time
from qiskit import QuantumCircuit, Aer, execute
import math

def oracle(qc, n, x):
    for i in range(n):
        if i != x:
            qc.x(i)
    qc.barrier()

def grover(n, x):
    qc = QuantumCircuit(n+1, n)
    # IInitialise Qubits 
    for i in range(n):
        qc.h(i)
    qc.x(n)
    qc.h(n)
    #nombre d'iterration
    iterations = int(math.pi/4 * math.sqrt(2**n))
    # Aplication de l'alghorithme de grover
    start_time = time.time()
    for i in range(iterations):
        oracle(qc, n, x)
        for j in range(n):
            qc.h(j)
            qc.x(j)
        qc.h(n-1)
        qc.mct(list(range(n-1)), n-1)
        qc.h(n-1)
        for j in range(n):
            qc.x(j)
            qc.h(j)
    qc.measure(range(n), range(n))

    # Execute circuit et retourne le résultat et le temps d'exécution
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1).result().get_counts()
    execution_time = time.time() - start_time
    return result, execution_time

result, execution_time = grover(2, 10)
print(result)
print("Temps d'exécution: ", execution_time)
