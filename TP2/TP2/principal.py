# -*- coding: utf-8 -*-
"""Voici le point d'entrée principal du programme. Nous utilisons les fonctions que vous devez programmer,
il est donc normal que ce code ne fonctionne pas tant que vous n'avez pas complété ces fonctions.
Exécutez d'abord les tests unitaires du module rsa fournis pour tester la programmation de vos fonctions 
au fur et à mesure.

Auteur: SAWADOGO Abdoul Raouf Wendyam Issoufou
"""

from chiffrement_fichiers import dechiffrer_fichier

#on affecte a la séquence clé_privée les valeurs données dans l'énoncé du TP
cle_privee=(82304707819, 17)

#on annonce le début du déchiffrement
print("Déchiffrement en cours...\n")

#on utilise la fonction dechiffrer_fichier avec comme argument le texte secret et la clé définie plus haut
message = dechiffrer_fichier('secret.txt', cle_privee)

#affichage du message
print("Message déchiffré:")
print("---------------------------------------------------------------------")
print(message)
print("---------------------------------------------------------------------")


