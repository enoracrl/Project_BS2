#                       Lecture d’un graphe d’interactions entre protéines


'''
1.2 Structure de données pour stocker le graphe

Cette section a pour objectif de comparer différentes stratégies pour représenter un graphe d’interactions.
Une première manière de stocker ce graphe est d’utiliser un dictionnaire où les clés sont les sommets et 
les valeurs associées aux clés sont les voisins des sommets. On peut aussi imaginer de stocker ce graphe 
dans une liste de couples (X,Y) qui représentent toutes les interactions.


    1.2.1 Question structure 1

Écrire une fonction qui lise un graphe d’interactions entre protéines dans un fichier tabulé et le stocke 
dans un dictionnaire. Le nom de la fonction sera read_interaction_file_dict et la fonction prendra en
unique argument le nom du fichier à lire. Le dictionnaire créé sera retourné par la fonction.

'''

        
def read_interaction_file_dict(file):
    dic = {}
    with open(file, 'r') as file_reader :
        for line in file_reader.readlines()[1:]:
            int1, int2  = line.split()
            if int1 not in dic:
                dic[int1] = list(int2)
            else:
                dic[int1].append(int2)
            if int2 not in dico:
                dic[int2] = list(int1)
            else:
                dic[int2].append(int1)
    return dic

'''
        1.2.2 Question structure 2

Écrire une fonction qui lise un graphe d’interactions entre protéines dans un fichier et le stocke 
dans une liste de couples. Le nom de la fonction sera read_interaction_file_list et la fonction prendra 
en unique argument le nom du fichier à lire. La liste créée sera retournée par la fonction.

'''

#liste de listes ou liste de tuples ?
def read_interaction_file_list(file):
    list_int = []
    with open(file, 'r') as file_reader :
        list_int = [tuple(line.split()) for line in file_reader.readlines()[1:]]
    return list_int
 
'''
    1.2.3 Question structure 3

Écrire une fonction qui lise un graphe d’interactions entre protéines dans un fichier et le stocke dans 
une matrice d’adjacence (vous pouvez utiliser numpy pour les matrices en python, et wikipédia pour la 
définition de matrice d’adjacence). Le nom de la fonction sera read_interaction_file_mat et la fonction 
prendra en unique argument le nom du fichier à lire. La matrice créée sera retournée par la fonction, 
ainsi que la liste ordonnée des sommets (parce que, évidemment, l’ordre des sommets est crucial pour 
lire correctement la matrice d’adjacence !).

'''

import numpy as np

def read_interaction_file_mat(file):
    dic = read_interaction_file_dict(file)
    peaks = list(dic.keys())
    matrix = np.zeros((len(peaks), len(peaks)), dtype=int)
    for i in dic:
        for j in dic[i]:
            matrix[peaks.index(i), peaks.index(j)] = 1
    return peaks, matrix


'''
    1.2.4 Question structure 4

Écrire une fonction nommée read_interaction_file, qui a partir d’un fichier d’interactions, retourne un triplet (d_int, l_int, m_int, l_som) dont le 
premier élément est le dictionnaire représentant le graphe, le second élément est la liste d’interactions représentant le même graphe, le troisième 
élément est la matrice d’ajacence correspondant à ce graphe, et le dernier élément est la liste ordonnée des sommets.

'''

def read_interaction_file(file):
    d_int = read_interaction_file_dict(file)
    l_int = read_interaction_file_list(file)
    m_int, l_som = read_interaction_file_mat(file)
    return d_int, l_int, m_int, l_som



'''
    1.2.5 Question structure 5

Pour un gros graphe d’interactions, quelle(s) stratégie(s) adopteriez-vous pour ne pas trop dégrader les performances de la fonction read_interaction_file ?

'''

# Pour ne pas trop dégrader les performances de la fonction read_interaction_file(), il faudrait ...


'''
    1.2.6 Question test des structures 1

Il est fondamental de tester le bon comportement de vos fonctions de lecture avant de poursuivre plus avant dans l’étude des réseaux d’interactions 
protéine-protéine. Vos fonctions ne sont pas utilisables si nous n’avons pas moyen de nous assurer qu’elles font effectivement ce pour quoi elles 
ont été conçues. Dans un fichier à part, pour lequel vous choisirez un nom explicite, préparez toute une série de tests unitaires pour vérifier que 
vos fonctions ont le comportement que nous attendons d’elles. C’est le moment de vous souvenir des tests unitaires que nous avons employés l’an dernier 1.

'''


'''

    1.2.7 Question test des structures 2

Écrire une fonction nommée is_interaction_file dont l’objectif est de vérifier que le fichier est bien au format attendu pour être lu correctement. 
Cette fonction prend en argument un fichier d’interaction, et renvoie le booléen true is le format est correct et false sinon. Travaillez à partir de 
plusieurs fichiers tests, certains respectant les spécifications du format demandés, d’autres non. 

Par exemple :
    1. fichier ne comportant pas la première ligne qui compte le nombre d’interactions ; 
    2. fichier vide ;
    3. fichier dont la première ligne contient un nombre qui n’est pas le nombre d’interactions ;
    4. fichier contenant une ligne qui ne comporte pas le bon nombre de colonnes...
    
'''

def is_interaction_file(file):
    with open(file, "r") as file_reader:
        text = [line.split() for line in file_reader.readlines()]
    count = sum([len(elem) for elem in text[1:]])
    if text != [] and text[0][0].isnumeric() == True and len(text[1:]) == int(text[0][0]) and count%2 ==0:
        return True
    else:
        return False
