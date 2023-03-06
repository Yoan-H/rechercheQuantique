import os
import pickle

def charger_chaine():
  if os.path.exists("blockchain.pkl"):
    with open("blockchain.pkl", "rb") as fichier:
      return pickle.load(fichier)
  else:
    return []
