# -*- coding: utf-8 -*-
""" Fonctions pour chiffrer et déchiffrer des fichiers textes.

Notez que nous ne fournissons pas de tests unitaires pour ces fonctions, car il
est fastidieux d'écrire de tels tests pour des fonctions de haut niveau impliquant
la lecture et l'écriture de fichiers. Le programme inclus dans principal.py permettra
de tester ces fonctions.

Auteur: SAWADOGO Abdoul Raouf Wendyam Issoufou
"""

import convertisseurs
import rsa


def chiffrer_fichier(nom_fichier_entree, nom_fichier_sortie, cle_publique):
    """À l'aide d'une clé de chiffrement (clé publique), ouvre un fichier texte, chiffre le contenu,
    puis écrit le résultat (liste de nombres) dans un autre fichier. Notez que cette fonction ne
    retourne rien: son résultat est l'écriture d'un fichier sur le disque.

    Étapes à suivre:
        1. Ouvrir le fichier d'entrée et en lire le contenu.
        2. Convertir le contenu (chaîne) en liste d'entiers, en utilisant la fonction chaine_a_liste_entiers.
        3. Pour chaque entier de cette liste, chiffrer le nombre à l'aide de la clé publique.
        4. Écrire dans le fichier de sortie chacun des nombres. Utilisez une ligne différente pour écrire
            ces nombres.

    Args:
        nom_fichier_entree (str): Le nom du fichier contenant le texte à chiffrer.
        nom_fichier_sortie (str): Le nom du fichier où écrire le résultat du chiffrement.
        cle_publique (list): Une liste de deux nombres: le module de chiffrement et l'exposant de chiffrement.

    """
    #on ouvre le fichier à chiffrer et on lit son contenu
    with open(nom_fichier_entree, "r") as file:

        #on crée une variable 'chaine' a laquelle on affecte les caractères contenus dans le fichier
        chaine = file.read()    
    
    #on créé une liste d'entier 'liste_entiers' en convertissant les caractère contenus dans la variable 'chaine'
    liste_entiers = convertisseurs.chaine_a_liste_entiers(chaine)
    
    #on initialise une liste qui contiendra les entiers chiffré
    liste_entiers_chiffres = []
    
    #boucle permettant de chiffrer les entiers
    for entier in liste_entiers:
        #on utilise la fonction chiffrer du module rsa pour transformer ces entiers
        entier_chiffre = rsa.chiffrer(entier, cle_publique)
        #on convertis ces entiers en caractère afin de pouvoir les enregistrer ligne par ligne dans la liste via la fonction append
        liste_entiers_chiffres.append(str(entier_chiffre)+ "\n")
   
    #on ouvre le fichier de sortie et on écrit la liste d'entiers chiffrés    
    with open(nom_fichier_sortie, "w") as file:
        
        file.writelines(liste_entiers_chiffres)


def dechiffrer_fichier(nom_fichier_entree, cle_privee):
    """À l'aide de la clé de déchiffrement (clé privée), déchiffrer le contenu d'un fichier (préalablement chiffré à
    l'aide de la fonction chiffrer_fichier) et retourner la chaîne résultante.

    Étapes à suivre:
        1. Ouvrir le fichier contenant le message codé, et en lire le contenu. Chaque ligne devrait contenir un entier.
        2. Pour chacune de ces lignes (chiffres), déchiffrer le nombre en utilisant la clé privée. Récupérer le
            dans une liste de nombres déchiffrés.
        3. Transformer cette liste en chaîne de caractères, en utilisant la fonction liste_entiers_a_chaine.
        4. Retourner cette chaîne.

    Args:
        nom_fichier_entree (str): Le nom du fichier où lire le message chiffré.
        cle_privee (list): Une liste de deux entiers: le module de chiffrement et l'exposant de déchiffrement.

    Returns:
        str: La chaîne de caractères déchiffrée.

    """
    #on ouvre le fichier contenant le message chiffré
    with open(nom_fichier_entree, "r") as file:
        #on enregistre ces entiers dans une liste
        liste_entiers_chiffres = file.readlines()
    
    #on créé une liste pour contenir les entiers déchiffrés    
    liste_entiers_dechiffres = []
    #boucle permettant de dechiffreer les entiers
    for entier in liste_entiers_chiffres:
        #on utilise la fonction déchiffrer du module rsa afin de déchiffrer chaque entier
        entiers_dechiffres = rsa.dechiffrer(int(entier), cle_privee)
        #on enregistre cet entier dans la liste
        liste_entiers_dechiffres.append(entiers_dechiffres)
    
    #on converti cette liste d'entier en caractères et on les enregistre dans la variable chaine    
    chaine = convertisseurs.liste_entiers_a_chaine(liste_entiers_dechiffres)
    
    #on affiche le contenu de la chaine de caractère
    return chaine

