import hashlib
import charger_chaine
import time
import json
import Bloc


def calculer_difficulty(chaîne, difficulty):
  blocks_last_hour = 0
  current_time = time.time()
  for block in chaîne:
    if current_time - block.timestamp < 3600:
      blocks_last_hour += 1
  if blocks_last_hour >= 10:
    return difficulty - 1
  elif blocks_last_hour <= 5:
    return difficulty + 1
  else:
    return difficulty


def sauvegarder_chaine(chaine):
    with open("blockchain.json", "w") as file:
        file.write(json.dumps(chaine, default=str))

def créer_bloc(chaine, données, difficulté):
    nouveau_bloc = {}
    nouveau_bloc["index"] = len(chaine) + 1
    nouveau_bloc["timestamp"] = time.time()
    nouveau_bloc["données"] = données
    nouveau_bloc["difficulté"] = difficulté
    nouveau_bloc["nonce"] = 0
    nouveau_bloc["hash_précédent"] = chaine[-1]["hash"] if chaine else None
    hash_val = hashlib.sha256(str(nouveau_bloc).encode()).hexdigest()
    compteur = 0 
    while hash_val[:difficulté] != "0" * difficulté:
        nouveau_bloc["nonce"] += 1
        compteur += 1
        hash_val = hashlib.sha256(str(nouveau_bloc).encode()).hexdigest()
    print("Nombre de calculs effectués :", compteur)
    nouveau_bloc["hash"] = hash_val
    return nouveau_bloc

def calculer_hash(input_data):
    sha = hashlib.sha256()
    sha.update(input_data.encode('utf-8'))
    return sha.hexdigest()

def mine_block(block, difficulty):
    nonce = 0
    trouve = False
    while not trouve:
        hash_input = block + str(nonce)
        hash = calculer_hash(hash_input)
        if hash[0:difficulty] == "0" * difficulty:
            trouve = True
        else:
            nonce += 1
    return nonce

def ajouter_block_à_chaîne(block, chaine):
    difficulty = calculer_difficulty(chaine, difficulty)
    nonce = mine_block(block, difficulty)
    block.nonce = nonce
    hash = calculer_hash(block + str(nonce))
    block.hash = hash
    chaine.append(block)


def calculer_difficulty(chaîne,difficulty):
  blocks_last_hour = 0
  current_time = time.time()
  for block in chaîne:
    if current_time - block.timestamp < 3600:
      blocks_last_hour += 1
  if blocks_last_hour >= 10:
    return difficulty - 1
  elif blocks_last_hour <= 5:
    return difficulty + 1
  else:
    return difficulty


def main():

    Bloc = []
    # Nombre de calculs effectués
    nombre_de_calculs = 0

    # Créer la chaine de blocs
    chaine = []

    # Ajouter le premier bloc à la chaîne
    prem = Bloc("Premier bloc dans la chaîne")
    ajouter_block_à_chaîne(prem, chaine)
    nombre_de_calculs = nombre_de_calculs + 1

    # Paramètre de difficulté
    Odifficulty = 2

    # Ajouter le second bloc à la chaîne
    deux = Bloc("Deuxième bloc dans la chaîne")
    difficulty = Odifficulty
    ajouter_block_à_chaîne(deux, chaine, difficulty)
    nombre_de_calculs = nombre_de_calculs + 1

    # Ajouter des blocs supplémentaires à la chaîne
    for i in range(0, 10):
        nouveau_bloc = Bloc("Bloc " + str(i) + " dans la chaîne")
        difficulty = calculer_difficulty(chaine, difficulty)
        ajouter_block_à_chaîne(nouveau_bloc, chaine, difficulty)
        nombre_de_calculs = nombre_de_calculs + 1

    # Afficher la chaine de blocs
    for i in range(0, len(chaine)):
        bloc = chaine[i]
        print("Bloc " + str(i) + " --- Données : " + bloc.données + " --- Hash : " + bloc.hash + " --- Nonce : " + str(bloc.nonce))

    # Afficher le nombre de calculs effectués
    print("Nombre de calculs effectués : " + str(nombre_de_calculs))



main()