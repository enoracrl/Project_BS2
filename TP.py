#                                           Lecture d’un graphe d’interactions entre protéines

#                                                       Léa BEAULIEU - Enora CORLER
#                                                             M2 Parcours BIS


'''

Importation of necessary modules

'''

import itertools        # creating and using iterators
import numpy as np      # creation of matrix / tables


def read_interaction_file_dict(file) -> dict:
    '''
    Return a dictionary that contains all neighboring vertices of a vertex.
    Args :
        file : a tabulate file, .txt format
    Output :
        interactions_dic : dict()
    '''
    interactions_dic = {}
    with open(file, 'r') as file_reader:
        for line in file_reader.readlines()[1:]:
            int1, int2 = line.split()
            if int1 not in interactions_dic.keys():
                interactions_dic[int1] = [int2]
            else:
                interactions_dic[int1].append(int2)
            if int2 not in interactions_dic.keys():
                interactions_dic[int2] = [int1]
            else:
                interactions_dic[int2].append(int1)
    return interactions_dic

def read_interaction_file_list(file) -> list:
    '''
    Return a list that contains a tuple of neighboring vertices without duplicates.
    Args :
        file : a tabulate file, .txt format
    Output :
        interactions_list : list()
    '''
    with open(file, 'r') as file_reader:
        interactions_list = [tuple(line.split())
                             for line in file_reader.readlines()[1:]]
    return interactions_list


def read_interaction_file_mat(file):
    '''
    Return an adjacency matrix that show 1 every time there is an interaction between two vertices.
    Also return a list that contains all vertices in the order of the matrix.
    Args :
        file : a tabulate file, .txt format
    Output :
        peaks, matrix : list() and a matrix (np.ndarrays())
    '''
    dic = read_interaction_file_dict(file)
    peaks = list(dic.keys())
    matrix = np.zeros((len(peaks), len(peaks)), dtype=int)
    for i in dic:
        for j in dic[i]:
            matrix[peaks.index(i), peaks.index(j)] = 1
    return peaks, matrix

def read_interaction_file(file):
    '''
    Return a triplet, the first element is the interaction dictionnary, the second
    one is the interaction list and the last one is the ordered list of vertices.
    Args :
        file : a tabulate file, .txt format
    Output :
        d_int, l_int, m_int, l_som : dict(), list(), list() and a matrix (np.ndarrays())
    '''
    d_int = read_interaction_file_dict(file)
    l_int = read_interaction_file_list(file)
    m_int, l_som = read_interaction_file_mat(file)
    return d_int, l_int, m_int, l_som

'''
1.2.5 Question structure 5
In order not to degrade the performance of the read_interaction_file() function too much,
it would be necessary to ask what the user wants to have in output by passing it as an argument
to the read_interaction_file() function, and this would make it possible not to generate all the
data without utility.
'''

def is_interaction_file(file):
    '''
    Return a boolean that return True if all conditions (correct file format) are True and
    return False (wrong file format) if one of them is False for a specific file given in input.
    Args :
        file : a tabulate file, .txt format
    Output :
        True : if the file is the file is not empty, with a correct number of
        interactions/lines/columns
        False : if at least one of the condition above is not respected
    '''
    with open(file, "r") as file_reader:
        text = [line.split() for line in file_reader.readlines()]
    count = sum([len(elem) for elem in text[1:]])
    if text != [] and text[0][0].isnumeric() is True :
        if len(text[1:]) == int(text[0][0]) and count % 2 == 0:
            return True
    return False


def count_vertices(file) -> int:
    '''
    Return the number of vertices by counting the numbers of keys of the
    interaction dictionnary (= the number of vertices)
    Args :
        file : a tabulate file, .txt format
    Output :
        number_of_vertices : an int (number of vertices)
    '''
    interactions_dict = read_interaction_file_dict(file)
    number_of_vertices = len(interactions_dict.keys())
    return number_of_vertices


def count_edges(file) -> int:
    '''
    Return the number of edges.
    Args :
        file : a tabulate file, .txt format
    Output :
        number_of_edges : an int (number of edges)
    '''
    with open(file, "r") as file_reader:
        number_of_edges = int(file_reader.readline()[0:])
    return number_of_edges


def clean_interactome(filein, fileout):
    '''
    Return an output file that is the same file as the input file but without
    any duplicate interactions or homo-dimers.
    Args :
        filein : a tabulate file to be cleaned, .txt format
        fileout : a non-existing file, .txt format
    Output :
        fileout : a tabulate file based on the filein file, cleaned from
        all repetitions/homo-dimers
    '''
    text = read_interaction_file_list(filein)
    for i in range(1, len(text)-1):
        if text[i][0] == text[i][1]:
            del text[i]
    # we remove duplicates from our list of lists
    text = list(l for l, _ in itertools.groupby(text))
    # we modify the initial number of interactions by the newest value
    text[0] = str(len(text[1:]))
    with open(fileout, "w+") as file_writer:
        file_writer.write(text[0]+"\n")
        for i in text[1:]:
            file_writer.write(str(i[0]) + str(" ") + str(i[1])+"\n")
