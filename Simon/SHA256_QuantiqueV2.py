from braket.circuits import Circuit
from braket.devices import LocalSimulator

# Fonction de hachage SHA-256
sha256 = Circuit().h(0).h(1).h(2).h(3).h(4).h(5).h(6).h(7).cswap(0, 8, 16).cswap(1, 9, 17).cswap(2, 10, 18).cswap(3, 11, 19).cswap(4, 12, 20).cswap(5, 13, 21).cswap(6, 14, 22).cswap(7, 15, 23).sha256(24, 25, 26, 27, 28, 29, 30, 31)

# Instantiate the local simulator
local_sim = LocalSimulator()

# Run the circuit
result = local_sim.run(sha256, shots=1).result()
print(result.measurements['z']) # affiche le résultat du hashage
