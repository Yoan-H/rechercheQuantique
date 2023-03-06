import qiskit  as q
import matplotlib.pyplot as plt 

#Simule un ordinateur quantique
simulator = q.Aer.get_backend('qasm_simulator')


#Circuit avec un quibit et une mesure 
circuit = q.QuantumCircuit(1,1)

#porte de hadamard sur la ligne 0  
circuit.h(0)

#Mesure du qubit 
circuit.measure(0,0)

print(circuit.draw(output='text'))

#Execution 
#Lancer 1000 simulation
job = q.execute(circuit, simulator, shots =1000)
result = job.result()

#Comptage
counts = result.get_counts(circuit)
print("nombre de '0' et de '1' :", counts)

#Diagramme en barre 
q.visualization.plot_histogram(counts)
plt.show()