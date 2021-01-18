# -*- coding: utf-8 -*-

"""Module comprenant les fonctions mathématiques nécessaires à l'utilisation rsa.

Vous devez compléter chacune des fonctions ci-dessous en respectant la documentation
fournie. Exécutez ce fichier pour lancer les tests unitaires et valider vos fonctions.

Auteur: SAWADOGO Abdoul Raouf Wendyam Issoufou
"""


def est_premier(nombre):
    """Détermine si un nombre est premier.

    Args:
        nombre (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est premier, et False autrement.

    """
    premier = True
    
    
    if nombre > 1:
        
        #boucle permettant de trouver si b a un diviseur différent de 1 et lui-meme
        for i in range(2, int(nombre**0.5)+1):
            if nombre % i == 0:
                premier = False
    
    else:
        premier = False
        
    return premier
 

def prochain_premier(nombre):
    """Trouve le plus petit nombre premier, qui est plus grand ou égal au nombre reçu en argument.

    Args:
        nombre (int): Le plus petit nombre à considérer.

    Returns:
        int: Le nombre premier trouvé.

    """
    i = nombre
    #on tilise la fonction est premier pour trouver le prochain entier premier supérieur au nombre entré
    while i >= nombre:

        if est_premier(i):
            return i
        i += 1


def facteurs_premiers(nombre):
    """Retourne la décomposition en produit de facteurs premiers du nombre reçu en argument.

    Args:
        nombre (int): Le nombre à factoriser.

    Returns:
        list: La liste des facteurs premiers, en ordre croissant.

    """
    #liste qui contiendra les facteurs trouvés
    liste_facteurs = []

    # cas ou le nombre n'est pas premier
    if not est_premier(nombre):
        # boucles permettant de trouver le plus petit diviseur du nombre et de l'inclure dans la liste de facteurs
        for i in range(2, int(nombre ** 0.5) + 1):

            while nombre % i == 0:
                liste_facteurs += [i, ]
                nombre = nombre // i
    # cas ou le nombre est premier
    if est_premier(nombre):
        liste_facteurs += [nombre, ]

    return liste_facteurs


def sont_copremiers(nombre_1, nombre_2):
    """Détermine si deux nombres sont "co-premiers", c'est-à-dire s'ils ne partagent aucun facteur premier différent de 1.
    Vous devinerez qu'il serait judicieux d'appeler deux fois la fonction facteurs_premiers (qui retourne une liste de
    facteurs), puis de comparer les deux listes reçues entre elles.

    Args:
        nombre_1 (int): Le premier nombre.
        nombre_2 (int): Le second nombre.

    Returns:
        bool: True si les deux nombres sont copremiers, False autrement.

    """
    copremiers = True
    #on recherche un facteur commun dans la décomposition en facteurs premiers des 2 nombres
    for i in facteurs_premiers(nombre_1):
        if i in facteurs_premiers(nombre_2):
            copremiers = False
    return copremiers


def sont_congruents(nombre_1, nombre_2, diviseur):
    """Détermine si deux nombres sont "congruents", c'est-à-dire si les deux nombres
    sont égaux une fois l'opération modulo appliquée (pour un certain diviseur).
    Autrement dit, les deux nombres sont congruents (modulo n) s'ils ont le même reste
    de division entière par n.

    Args:
        nombre_1 (int): Le premier nombre.
        nombre_2 (int): Le second nombre.
        diviseur (int): Le modulo à utiliser pour vérifier la congruence.

    Returns:
        bool: True si les deux nombres sont congruents (étant donné le diviseur reçu), False autrement.

    """
    return nombre_1 % diviseur == nombre_2 % diviseur


def chiffrer(nombre, cle_publique):
    """Chiffre (encrypte) un nombre à l'aide une clé publique, en utilisant la méthode RSA.
    Voir l'énoncé pour connaître les opérations mathématiques à faire ici.
    
    Notez que vous pouvez grandement accélérer le calcul en faisant appel à la fonction Python «pow».
    Exécutez la commande «help(pow)» ou  «pow?» dans la console IPython pour obtenir plus d'informations.
    
    Args:
        nombre (int): Le nombre à chiffrer.
        cle_publique (tuple): Une liste de deux entiers: le module de chiffrement et l'exposant de chiffrement.

    Warning:
        Le nombre ne peut pas être plus grand que le module de chiffrement, sinon l'algorithme RSA ne fonctionnera pas.
        Vous pouvez utiliser l'instruction assert pour vous en assurer, mais lors de la correction nous n'utiliserons
        que des nombres/clés compatibles.

    Returns:
        int: L'entier chiffré.

    """
    #on s'assure que le nombre est inférieur au module de chiffrement
    assert nombre < cle_publique[0]
    
    from builtins import pow
    
    #on retourne l'entier chiffré
    return pow(nombre, cle_publique[1], cle_publique[0])


def dechiffrer(nombre, cle_privee):
    """ Déchiffre (décrypte) un nombre à l'aide une clé privée, en utilisant la méthode RSA.
    Voir l'énoncé pour connaître les opérations mathématiques à faire ici.

    Notez que vous pouvez grandement accélérer le calcul en faisant appel à la fonction Python «pow».
    Exécutez la commande «help(pow)» ou  «pow?» dans la console IPython pour obtenir plus d'informations.

    Args:
        nombre (int): Le nombre à déchiffrer.
        cle_privee (tuple): Une liste de deux entiers: le module de déchiffrement et l'exposant de déchiffrement.

    Warning:
        Le nombre ne peut pas être plus grand que le module de déchiffrement, sinon l'algorithme RSA ne fonctionnera pas.
        Vous pouvez utiliser l'instruction assert pour vous en assurer, mais lors de la correction nous n'utiliserons
        que des nombres/clés compatibles.

    Returns:
        int: L'entier déchiffré.

    """
    #on s'assure que le nombre est inférieur au module de déchiffrement
    assert nombre < cle_privee[0]
    
    from builtins import pow
    
    #on retourne la valeur du nombre déchiffré
    return pow(nombre, cle_privee[1], cle_privee[0])
    

def generer_paire_de_cles(minimum_premier_1=1000, minimum_premier_2=2000):
    """Cette fonction, dont le code vous est fourni, permet de générer deux clés: une clé de chiffrement
    (clé publique), et une clé de déchiffrement (clé privée). Cette fonction utilise d'autres fonctions que vous
    avez à programmer, il est donc normal qu'elle ne fonctionne pas tant que vos propres fonctions soient terminées.
    Exécutez les tests unitaires (fournis) pour tester vos propres fonctions d'abord, avant de tenter d'utiliser
    la présente fonction.

    Rendez-vous sur la page Wikipédia de la cryptographie RSA pour plus d'informations sur ces étapes!

    Warning:
        Dans la vraie vie, il faudrait utiliser des nombres premiers BEAUCOUP plus grands, et rendre ce processus
        aléatoire (on ne veut pas générer plusieurs fois la même clé).

    Args:
        minimum_premier_1 (int, optional): Le plus petit nombre à considérer comme premier nombre premier.
        minimum_premier_2 (int, opitonal): Le plus petit nombre à considérer comme second nombre premier.

    Returns:
        tuple: Clé publique
        tuple: Clé privée 
        
        Récupérez le résultat de cette fonction comme suit :
            cle_privee, cle_publique = generer_paire_de_cles()

    """

    # On choisit deux "grands" nombres premiers.
    p = prochain_premier(minimum_premier_1)
    q = prochain_premier(minimum_premier_2)

    # On calcule le module de chiffrement n, puis l'indicatrice d'Euler de p et q.
    module = p * q
    indicatrice = (p - 1) * (q - 1)

    # On cherche un exposant de chiffrement e tel que e et l'indicatrice sont copremiers. On commence avec une valeur
    # suffisamment petite (17), et si celle-ci ne fonctionne pas, on continue la recherche.
    exposant_chiffrement = 17
    while not sont_copremiers(exposant_chiffrement, indicatrice):
        exposant_chiffrement += 1
        assert exposant_chiffrement < indicatrice, "Erreur: impossible de trouver un nombre copremier."

    # On cherche un exposant de déchiffrement d qui tel que d * e est congruent à 1, modulo l'indicatrice.
    exposant_dechiffrement = 2
    while not sont_congruents(exposant_dechiffrement * exposant_chiffrement, 1, indicatrice):
        exposant_dechiffrement += 1
        assert exposant_dechiffrement < indicatrice, "Erreur: impossible de trouver un nombre congruent."

    # On crée les clés publique et privée avec nos nombres, et on les retourne.
    cle_publique = (module, exposant_chiffrement)
    cle_privee = (module, exposant_dechiffrement)

    return cle_privee, cle_publique


def test_est_premier():
    """Vérifie la fonction est_premier() avec quelques valeurs."""
    assert est_premier(2)
    assert est_premier(3)
    assert est_premier(5)
    assert est_premier(7)
    assert est_premier(13)
    assert est_premier(1009)

    assert not est_premier(-10)
    assert not est_premier(0)
    assert not est_premier(1)
    assert not est_premier(4)
    assert not est_premier(9)
    assert not est_premier(1001)


def test_prochain_premier():
    """Vérifie la fonction prochain_premier() avec quelques valeurs."""
    assert prochain_premier(2) == 2
    assert prochain_premier(3) == 3
    assert prochain_premier(4) == 5
    assert prochain_premier(10) == 11
    assert prochain_premier(1000) == 1009
    assert prochain_premier(-1) == 2


def test_facteurs_premiers():
    """Vérifie la fonction facteurs_premiers() avec quelques valeurs."""
    assert facteurs_premiers(2) == [2]
    assert facteurs_premiers(5) == [5]
    assert facteurs_premiers(10) == [2, 5]
    assert facteurs_premiers(999) == [3, 3, 3, 37]


def test_sont_copremiers():
    """Vérifie la fonction sont_copremiers() avec quelques valeurs."""
    assert sont_copremiers(6, 35)
    assert not sont_copremiers(6, 27)


def test_sont_congruents():
    """Vérifie la fonction sont_congruents() avec quelques valeurs."""
    assert sont_congruents(32, 11, 7)
    assert not sont_congruents(32, 11, 6)


def test_chiffrer():
    """Vérifie l'encryption à l'aide de chiffrer()"""
    # Exemple provenant de Wikipédia.
    p = 61
    q = 53
    modulo_de_chiffrement = p * q
    exposant_chiffrement = 17
    cle_publique = (modulo_de_chiffrement, exposant_chiffrement)

    assert chiffrer(65, cle_publique) == 2790


def test_dechiffrer():
    """Vérifie la décryption à l'aide de dechiffrer()"""
    # Exemple provenant de Wikipédia
    p = 61
    q = 53
    modulo_de_chiffrement = p * q
    exposant_dechiffrement = 2753
    cle_privee = (modulo_de_chiffrement, exposant_dechiffrement)

    assert dechiffrer(2790, cle_privee) == 65


def test_chiffrer_dechiffrer():
    """Vérifie que nous sommes capables de chiffrer puis de déchiffrer un message avec une paire de clés, afin de
    récupérer le message original.
    """
    p = 61
    q = 53
    modulo_de_chiffrement = p * q
    exposant_chiffrement = 17
    exposant_dechiffrement = 2753
    cle_publique = (modulo_de_chiffrement, exposant_chiffrement)
    cle_privee = (modulo_de_chiffrement, exposant_dechiffrement)

    message = 1234
    message_encrypte = chiffrer(message, cle_publique)
    message_decrypte = dechiffrer(message_encrypte, cle_privee)
    assert message_decrypte == message

    message = 1
    message_encrypte = chiffrer(message, cle_publique)
    message_decrypte = dechiffrer(message_encrypte, cle_privee)
    assert message_decrypte == message

    message = 42
    message_encrypte = chiffrer(message, cle_publique)
    message_decrypte = dechiffrer(message_encrypte, cle_privee)
    assert message_decrypte == message

    message = 999
    message_encrypte = chiffrer(message, cle_publique)
    message_decrypte = dechiffrer(message_encrypte, cle_privee)
    assert message_decrypte == message


if __name__ == '__main__':
    print("Exécution des tests unitaires...")

    test_est_premier()
    test_prochain_premier()
    test_facteurs_premiers()
    test_sont_copremiers()
    test_sont_congruents()
    test_chiffrer()
    test_dechiffrer()
    test_chiffrer_dechiffrer()

    print("Tests réussis!")