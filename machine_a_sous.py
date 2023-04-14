import random

MISE_MAX = 100
MISE_MIN = 0

LIGNE_MIN = 1
LIGNE_MAX = 3


valeurs = {'1' : 'A',
           '2' : 'B',
           '3' : 'C',
           '4' : 'D'}




def limite():
    """Cette fonction sert à demander au joueur à partir de quel gain souhaite t'il arrêter de jouer.

    Returns:
        limite -> int : Gain à partir duquel le joueur souhaite arrêter le jeu
    """

    while True:
        limite = input('A quel montant souhaitez vous vous retirer? --> ')

        if limite.isdigit() == True:
            limite = int(limite)

            if limite > 0:
                break
            else:
                print('Veuillez entrer une limite supérieure à 0.')
            
        else:
            print('La limite doit être un nombre')
        
    return print(limite)







def mise(nb_lignes):
    """Cette fonction permet de demander au joueur quelle somme souhaite t'il miser. La fonction pondère ensuite cette somme par le nombre de lignes choisis précédemment par le joueur.

    Args:
        nb_lignes (int): nb_lignes corresponds au nombre de lignes sur lequel le joueur à miser. Cette variable provient de la fonction du même nom nb_lignes.

    Returns:
        mise_tot -> int : La fonction retourne la mise totale du joueur pour ce tour, pondérée par le nombre de lignes.
    """

    while True:
        mise = input('Quelle somme souhaitez vous miser? --> ')

        if mise.isdigit() == True:
            mise = int(mise)

            if MISE_MIN <= mise <= MISE_MAX:
                mise_tot = mise * (nb_lignes*nb_lignes)
                break
                
            else:
                print(f'Veuillez entrer une mise comprise entre {MISE_MIN} et {MISE_MAX}.')
            
        else:
            print('La mise doit être un nombre.')
        
    return print(f'Votre mise totale est de {mise_tot}')









def nb_lignes():
    """Cette fonction permet de demander au joueur sur quel nombre de ligne il souhaite miser : 1 au minimm.

    Returns:
        nb_lignes: Le nombre de lignes sur lequel le joueur souhaite miser ce tour
    """
    while True:

        nb_lignes = input('Sur quel nombre de lignes souhaitez vous miser? --> ')

        if nb_lignes.isdigit() == True:
            nb_lignes = int(nb_lignes)

            if LIGNE_MIN <= nb_lignes <= LIGNE_MAX:
                break
            else:
                print(f'Le nombre de lignes sur lequel vous misez doit être compris entre {LIGNE_MIN} et {LIGNE_MAX}.')

        else:
            print('Le nombre de lignes doit être un nombre.')
        
    return nb_lignes





def economie():
    """Cette fonction donne l'argent détenue par le joueur à l'instant T.

    Returns:
        eco -> int : Argent disponible au joueur
    """

    while True:
        eco = input('Avec quelle somme entrez vous en jeu? --> ')

        if eco.isdigit() == True:
            eco = int(eco)

            if eco > 0:
                break
            else:
                print('Veuillez entrer une somme supérieure à 0.')
            
        else:
            print('La somme doit être un nombre.')
        
    return print(eco)



def plateau(liste):
    """Cette fonction permet d'afficher les trois lignes de la machine à sous.

    Args:
        liste (list): Liste de 9 lettres comprises entre A et D inclu, correspondant aux trois valeurs de chacunes des trois lignes du jeu. Elle provient de la fonction 'jeu'.

    Returns:
        plateau -> NoneType: Visualisation de l'écran de la machine à sous
    """

    a1 = str(liste[0])
    a2 = str(liste[1])
    a3 = str(liste[2])
    b1 = str(liste[3])
    b2 = str(liste[4])
    b3 = str(liste[5])
    c1 = str(liste[6])
    c2 = str(liste[7])
    c3 = str(liste[8])

    plateau = print(' ' + a1 + ' ' + '|' + ' ' + a2 + ' ' + '|' + ' ' + a3 + ' \n' +
                 '___________\n' +
                 '\n' +
                 ' ' + b1 + ' ' + '|' + ' ' + b2 + ' ' + '|' + ' ' + b3 + ' \n' +
                 '___________\n' +
                 '\n' +
                 ' ' + c1 + ' ' + '|' + ' ' + c2 + ' ' + '|' + ' ' + c3 + ' ')

    return plateau




def jeu(valeurs):
    """En quelque sorte le coeur du jeu. L'équivalent du levier sur lequel on appuie pour jouer sur une vraie machine à sous.
    Lorsqu'elle est appelée, cette fonction remplie alétoirement une liste initialement vide de 9 chiffres, tous compris entre 1 et 4 inclus.
    La dimension aléatoire est assurée par le fonction randint du module random.

    Args:
        valeurs (dict): Il s'agit d'un dictionnaire de taille 4. Dedans, aux 4 permiers entiers sont associés leur lettre dans l'alphabet (1 -> A, 2 -> B ...), 
        le but étant que se soit des lettres et non des chiffres qui soient affichés sur l'écran de la machine à sous. (-> décision purement esthétique)

    Returns:
        liste: Liste de 9 lettres comprises entre A et D inclu, correspondant aux trois valeurs de chacunes des trois lignes du jeu. 
    """
    while True:
        liste = []

        for i in range(9):
            liste.append(valeurs[str(random.randint(1,4))])
        
        return liste


def check_win(liste, nb_lignes):
    while True: 
        # ligne_1_checked = False
        # ligne_2_checked = False
        # ligne_3_checked = False

        result = [False for i in range(3)]

        if liste[0] == liste[1] == liste[2]:
            result[0] = True
        elif liste[3] == liste[4] == liste[5]:
            result[1] = True
        elif liste[6] == liste[7] == liste[8]:
            result[2] = True

        nb_true = result.count(True)

        if nb_lignes == nb_true :
            print("C'est gagné !")

            signal = 1
            return signal
        
        else: 
            print("C'est perdu !")
            signal = 0
            return signal 






    
    


# if __name__ == '__main__':
#     limite()
#     nb = nb_lignes()
#     mise(nb)
    
#     plateau(jeu(valeurs))
#     check_win(jeu(valeurs), nb_lignes())


help(jeu)