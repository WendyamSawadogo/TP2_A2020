# -*- coding: utf-8 -*-
"""Ce module contient des fonctions utilitaires permettant de convertir des chaînes de caractères en entier, et
vice-versa. Vous n'avez pas à modifier ces fonctions, mais elles vous seront utiles pour programmer vos fonctions
d'encryption et de décryption de messages.

Auteur: Jean-Francis Roy
"""


def chaine_a_liste_entiers(chaine, taille_des_blocs=2, taille_octets=256):
    """Convertit une chaîne de caractères quelconque en une liste d'entiers, pouvant ensuite être encryptés par
    l'algorithme RSA. Une fois les entiers encryptés, ceux-ci peuvent être re-convertis en chaîne de caractères avec la
    fonction liste_entier_a_chaine.

    Notons que nous avons mis des valeurs par défaut pour la taille de blocs et le nombre d'octets (8 bits) utilisés
    pour la conversion. Dans la «vraie vie», si ces valeurs sont trop petites (comme c'est le cas ici), le code
    peut plus facilement être «craqué».

    Args:
        chaine (str): La chaîne à convertir.
        taille_des_blocs (int, optional): La taille en octets de chaque bloc. La valeur par défaut est 2, ce qui est
            suffisant pour ce TP car nous n'utilisons pas des grandes clés RSA, mais pas dans la «vraie vie».
        taille_octets (int, optional): Le nombre d'octets utilisés pour encoder les caractères. La valeur par défaut
            est 256, et vous n'avez pas besoin de modifier cette valeur.

    Warning:
        Pour simplifier le codage/décodage en liste d'entiers, nous ajoutons des espaces à la fin de la chaîne pour
        obtenir une chaîne d'une longueur qui est un multiple de la taille des blocs.

    Warning:
        Pour utiliser cette fonction avec des caractères provenant de d'autres langages que l'anglais/français, il faut
        utiliser un plus grand nombre pour le paramètre taille_octets.

    Returns:
        list of ints: La liste d'entiers résultante.

    """
    assert len(chaine) > 0, "La chaîne à convertir ne doit pas être vide."

    # On ajoute des espaces à la fin pour avoir une chaîne de longueur compatible avec la taille des blocs.
    chaine = chaine + ' ' * (taille_des_blocs - len(chaine) % taille_des_blocs)

    blocs_entiers = []
    # Pour chaque bloc...
    for debut_bloc in range(0, len(chaine), taille_des_blocs):
        # Calcul de l'entier pour ce bloc de texte.
        bloc = 0
        for i in range(debut_bloc, debut_bloc + taille_des_blocs):
            bloc += ord(chaine[i]) * (taille_octets ** (i % taille_des_blocs))

        blocs_entiers.append(bloc)

    return blocs_entiers


def liste_entiers_a_chaine(liste_entiers, taille_des_blocs=2, taille_octets=256):
    """Convertit une liste d'entiers en une chaîne de caractères. À utiliser une fois un message numérique encrypté
    ou décrypté pour obtenir le message en texte résultant.

    Args:
        liste_entiers (list of ints): La liste d'entiers à convertir.
        taille_des_blocs (int, optional): La taille en octets de chaque bloc. Utiliser la même valeur qu'utilisée lors
            de la conversion de la chaîne originale.
        taille_octets (int, optional): Le nombre d'octets utilisés pour décoder chaque caractère. La valeur par défaut
            est 256, et vous n'avez pas besoin de modifier cette valeur.

    Warning:
        Pour simplifier le codage/décodage en liste d'entiers, nous retirons les espaces à la fin de la chaîne
        retournée, qui ont possiblement été ajoutés pendant l'encodage.

    Returns:
        str: La chaîne de caractères résultante.

    """
    assert len(liste_entiers) >= 0, "La liste d'entiers ne doit pas être vide."

    message = []
    for entier in liste_entiers:
        message_du_bloc = []
        for i in range(taille_des_blocs - 1, -1, -1):
            valeur_ascii = entier // (taille_octets ** i)
            entier = entier % (taille_octets ** i)
            message_du_bloc = [chr(valeur_ascii)] + message_du_bloc
        message += message_du_bloc
    return ''.join(message).rstrip()



def test_chaine_a_entier():
    assert chaine_a_liste_entiers('A') == [8257]
    assert chaine_a_liste_entiers('B') == [8258]
    assert chaine_a_liste_entiers('Z') == [8282]
    assert chaine_a_liste_entiers('a') == [8289]
    assert chaine_a_liste_entiers('b') == [8290]
    assert chaine_a_liste_entiers('z') == [8314]
    assert chaine_a_liste_entiers('ab') == [25185, 8224]

    ma_liste = [25185, 25699, 26213, 26727, 27241, 27755, 28269, 28783, 29297, 29811, 30325, 30839, 31353, 8224]
    assert chaine_a_liste_entiers('abcdefghijklmnopqrstuvwxyz') == ma_liste


def test_entier_a_chaine():
    assert liste_entiers_a_chaine([8257]) == 'A'
    assert liste_entiers_a_chaine([8258]) == 'B'
    assert liste_entiers_a_chaine([8282]) == 'Z'
    assert liste_entiers_a_chaine([8289]) == 'a'
    assert liste_entiers_a_chaine([8290]) == 'b'
    assert liste_entiers_a_chaine([8314]) == 'z'
    assert liste_entiers_a_chaine([25185, 8224]) == 'ab'

    ma_liste = [25185, 25699, 26213, 26727, 27241, 27755, 28269, 28783, 29297, 29811, 30325, 30839, 31353, 8224]
    assert liste_entiers_a_chaine(ma_liste) == 'abcdefghijklmnopqrstuvwxyz'


def test_chaine_a_entier_a_chaine():

    chaine_originale = "Bonjour"
    assert liste_entiers_a_chaine(chaine_a_liste_entiers(chaine_originale)) == chaine_originale

    chaine_originale = "Quelques$caractères&*spéciaux!@"
    assert liste_entiers_a_chaine(chaine_a_liste_entiers(chaine_originale)) == chaine_originale

    chaine_originale = "Test\nAvec\nPlusieurs\nLignes!"
    assert liste_entiers_a_chaine(chaine_a_liste_entiers(chaine_originale)) == chaine_originale


if __name__ == '__main__':

    print("Exécution des tests unitaires...")
    
    test_chaine_a_entier()
    test_entier_a_chaine()
    test_chaine_a_entier_a_chaine()

    print("Tests réussis!")

