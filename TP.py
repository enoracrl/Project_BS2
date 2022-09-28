#                                           Lecture d’un graphe d’interactions entre protéines

#                                                       Léa BEAULIEU - Enora CORLER
#                                                             M2 Parcours BIS


'''

            Importation des modules nécessaires

'''


import numpy as np      # creation de matrices / tableaux
import itertools        # creating and using iterators




'''

1.2 Structure de données pour stocker le graphe

    1.2.1 Question structure 1
    
'''

        
def read_interaction_file_dict(file):
    '''
    Return a dictionary that contains all neighboring vertices of a vertex.
    '''
    interactions_dic = {}
    with open(file, 'r') as file_reader :
        for line in file_reader.readlines()[1:]:
            int1, int2  = line.split()
            if int1 not in interactions_dic.keys():
                interactions_dic[int1] = [int2]
            else:
                interactions_dic[int1].append(int2)
            if int2 not in interactions_dic.keys():
                interactions_dic[int2] = [int1]
            else:
                interactions_dic[int2].append(int1)
    return interactions_dic
      
'''
        1.2.2 Question structure 2
        
'''

#liste de listes ou liste de tuples ?
def read_interaction_file_list(file):
    '''
    Return a list that contains a tuple of neighboring vertices without duplicates.
    '''
    with open(file, 'r') as file_reader :
        interactions_list = [tuple(line.split()) for line in file_reader.readlines()[1:]]
    return interactions_list
 
'''
    1.2.3 Question structure 3

'''

def read_interaction_file_mat(file):
    '''
    Return an adjacency matrix that show 1 every time there is an interaction between two vertices. 
    Also return a list that contains all vertices in the order of the matrix.
    '''
    dic = read_interaction_file_dict(file)
    peaks = list(dic.keys())
    matrix = np.zeros((len(peaks), len(peaks)), dtype=int)
    for i in dic:
        for j in dic[i]:
            matrix[peaks.index(i), peaks.index(j)] = 1
    return peaks, matrix


'''
    1.2.4 Question structure 4
    
'''

def read_interaction_file(file):
    '''
    Return a triplet, the first element is the interaction dictionnary, the second one is the interaction list 
    and the last one is the ordered list of vertices.
    '''
    d_int = read_interaction_file_dict(file)
    l_int = read_interaction_file_list(file)
    m_int, l_som = read_interaction_file_mat(file)
    return d_int, l_int, m_int, l_som


'''
    1.2.5 Question structure 5

'''

# Pour ne pas trop dégrader les performances de la fonction read_interaction_file(), il faudrait ...


'''
    1.2.6 Question test des structures 1

'''

# -> Voir fichier test.py

'''

    1.2.7 Question test des structures 2

'''

def is_interaction_file(file):
    '''
    Return a boolean that return True if all conditions are True and return False if one of them is False.
    '''
    with open(file, "r") as file_reader:
        text = [line.split() for line in file_reader.readlines()]
    count = sum([len(elem) for elem in text[1:]])
    if text != [] and text[0][0].isnumeric() == True and len(text[1:]) == int(text[0][0]) and count%2 ==0:
        return True
    else:
        return False

#                                                                        --------------
#                                                                       |  CHAPITRE 2  |
#                                                                        --------------

#                                           Semaine 2 : Exploration du graphe d’interactions protéine-protéine
#                                           ---------   ------------------------------------------------------



'''

2.1 Exploration du graphe global

    2.1.1 Question exploration 1
    
'''

def count_vertices(file) :
    '''
    Return the number of vertices by counting the numbers of keys of the interaction dictionnary (= the number of vertices)
    '''
    interactions_dict = read_interaction_file_dict(file)
    number_of_vertices = len(interactions_dict.keys())
    return number_of_vertices
    
    
'''
    2.1.2 Question exploration 2

'''

def count_edges(file):
    ''' 
    Return the number of edges. 
    '''
    with open(file, "r") as file_reader :
        number_of_edges = int(file_reader.readline()[0:])
    return number_of_edges


'''
    
    2.1.3 Question nettoyage

'''


def clean_interactome(filein, fileout):
    ''' 
    Return an output file that is the same file as the input file but without any duplicate interactions or homo-dimers.
    '''
    text = read_interaction_file_list(filein)
    for i in range(1,len(text)-1) :
        if text[i][0] ==  text[i][1] :
           del text[i]
    text = list(l for l, _ in itertools.groupby(text)) # we remove duplicates from our list of lists 
    text[0] = str(len(text[1:])) # we modify the initial number of interactions by the newest value
    with open(fileout, "w+") as file_writer :
        file_writer.write(text[0]+"\n")
        for i in text[1:]:
            file_writer.write(str(i[0]) + str(" ") + str(i[1])+"\n")
    
'''

    2.1.4 Question test
    
'''

# -> Voir fichier test.py
