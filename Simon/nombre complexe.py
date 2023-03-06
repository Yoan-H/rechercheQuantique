import numpy as np
import qiskit as q

z1 = 2+3j
print(z1)
print(abs(z1))
print(z1**2)


z2 = np.sqrt(3)/2 + 1/2j
print(abs(z2))
print(z1*z2)
print(1/z2)

### Partie A. Préparation
simulator = q.Aer.get_backend('statevector_simulator')
### Partie B. Construction du circuit
circuit = q.QuantumCircuit(1)
# Initialisation à la main : écriture algébrique
alpha0 = 3+1j
beta0 = 1-2j
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)
alpha, beta = alpha0/norme, beta0/norme
etat_initial = [alpha,beta]
qubit_initial = q.extensions.Initialize(etat_initial)
circuit.append(qubit_initial, [0])

#circuit : porte X
circuit.x(0)

# Partie C. Exécution
job = q.execute(circuit, simulator)

# Partie D. Résultats
result = job.result()
coefficients = result.get_statevector()
print("Coefficient alpha:", coefficients[0])
print("Coefficient beta :", coefficients[1])