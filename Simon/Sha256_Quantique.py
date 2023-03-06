from braket.circuits import Circuit

# Entrée pour le hachage
message = "Hello, world!"

# Création du circuit quantique
circuit = Circuit()

# Définition des registres pour le message et le hachage
msg_reg = circuit.qubits(len(message) * 8, name='msg_reg')
hash_reg = circuit.qubits(256, name='hash_reg')

# Initialisation du message
for i, char in enumerate(message):
    byte = ord(char)
    bit_string = bin(byte)[2:].zfill(8)
    for j, bit in enumerate(bit_string):
        if bit == "1":
            circuit.x(msg_reg[i * 8 + j])

# Implémentation de la fonction de hachage SHA-256
circuit.sha256(msg_reg, hash_reg)

# Mesure des qubits du registre de hachage
circuit.measure_all()

# Exécution du circuit sur un simulateur local
from braket.devices import LocalSimulator
device = LocalSimulator()
result = device.run(circuit, shots=1).result()

# Affichage du résultat
print(result.measurement_counts)
