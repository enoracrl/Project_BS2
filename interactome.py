"""Docstring d'une ligne décrivant brièvement ce que fait le programme. 2

Usage:

======
python nom_de_ce_super_script.py argument1 argument2

argument1: un entier signifiant un truc
argument2: une chaîne de caractères décrivant un bidule
"""

__authors__ = ("Enora CORLER", "Léa BEAULIEU")
__contact__ = ("enora.corler@etudiant.univ-rennes1.fr", "lea.beaulieu@etudiant.univ-rennes1.fr")
__date__ = "05/10/2022"

import itertools
import numpy as np
from fractions import Fraction
import networkx as nx
import matplotlib.pyplot as plt

class Interactome :
    '''
    A class to explore the interactome.

    Methods :
        We read the file for a reasonable number of times to construct the object,
        and then manipulate the data structure as we want
    '''
    def __init__(self, file) :
        '''
        Construct all the necessary attributes for the interactome object.

        Args :
            a tabulate file, .txt format

        Attributes :
            int_list : the list of all interactions
            int_dic : a dictionnary that regroups all the interactions
            self.matrix : the adjacency matrix of the interactions

        Parameters :
            int_list : the list of all interactions
            int_dic : a dictionnary that regroups all the interactions
            self.matrix : the adjacency matrix of the interaction
        '''
        self.file = file
        self.matrix = []
        int_dict = {}
        int_list = []
        text = []
        number_interactions = ""
        with open(file, 'r', encoding="utf-8") as file_reader :
            text = file_reader.readlines()
            if text != [] :
                number_interactions = text[0][0]
                for line in text[1:] :
                    text.append(line.split())
                    int_list.append(tuple(line.split()))
                    int1, int2 = line.split()
                    if int1 not in int_dict :
                        int_dict[int1] = [int2]
                    else :
                        int_dict[int1].append(int2)
                    if int2 not in int_dict :
                        int_dict[int2] = [int1]
                    else :
                        int_dict[int2].append(int1)
        self.text = text
        self.number_interactions = number_interactions
        self.int_list = int_list
        self.int_dict = int_dict

    # ACCESSEURS
    def get_int_list(self) :
        '''
        Return the instance variable of the list of interactions.
        '''
        return self.int_list

    def get_int_dict(self) :
        '''
        Return the instance variable of the dictionnary of interactions.
        '''
        return self.int_dict

    def get_mat(self) :
        '''
        Return the instance variable of the matrix of interactions
        '''
        self.matrix = self.read_interaction_file_mat()[1]
        return self.matrix

    # METHODS OF THE CLASS
    def is_interaction_file(self) :
        '''
        Return a boolean that return True if all conditions (correct file format) are True and
        return False (wrong file format) if one of them is False for a specific file given.

        Output :
            True : if the file is not empty, with a correct number of interactions/lines/columns
            False : if at least one of the condition above is not respected
        '''
        count = sum([len(elem) for elem in self.text[1:]])
        if self.number_interactions.isnumeric() is True :
            if len(self.text[1:]) == int(self.number_interactions) and count % 2 == 0 :
                return True
        return False

    def read_interaction_file_mat(self) :
        '''
        Return an adjacency matrix that show 1 every time there is an interaction between
        two vertices. Also return a list that contains all vertices in the order of the matrix.

        Output :
            proteins : a list with all proteins in the order of the matrix
            matrix : a matrix (np.ndarrays())
        '''
        proteins = list(self.int_dict.keys())
        matrix = np.zeros((len(proteins), len(proteins)), dtype=int)
        for key, values in self.int_dict.items():
            for value in values:
                matrix[proteins.index(key), proteins.index(value)] = 1
        return proteins, matrix

    def read_interaction_file(self) :
        '''
        Return a triplet, the first element is the interaction dictionnary, the second
        one is the interaction list and the last one is the ordered list of vertices.

        Output :
            d_int, l_int, l_som, m_int : dict(), list(), list() and a matrix (np.ndarrays())
        '''
        return (self.get_int_dict(), self.get_int_list(), self.read_interaction_file_mat()[0],
                self.get_mat())

    def count_vertices(self) :
        '''
        Return the number of vertices by counting the numbers of keys of the
        interaction dictionnary (= the number of vertices)

        Output :
            number_of_vertices : an int (number of vertices)
        '''
        number_of_vertices = len(self.get_int_dict().keys())
        return number_of_vertices

    def count_edges(self) :
        '''
        Return the number of edges.

        Output :
            number_of_edges : an int (number of edges)
        '''
        number_of_edges = len(self.get_int_list())
        return number_of_edges

    def clean_interactome(self, fileout) :
        '''
        Return an output file that is the same file as the input file but without
        any duplicate interactions or homo-dimers.

        Args :
            fileout : the path of a file which will be written in output, .txt format

        Output :
            fileout : a tabulate file based on the filein file, cleaned from
            all repetitions/homo-dimers
        '''
        # remove homo-dimers : ok
        for i in range(1, len(self.get_int_list())-1):
            if self.get_int_list()[i][0] == self.get_int_list()[i][1]:
                del self.get_int_list()[i]
        # we remove duplicates from our list of lists
        clean_text = list(l for l, _ in itertools.groupby(self.get_int_list()))
        for i in clean_text:
            for j in reversed(clean_text):
                if i ==tuple(reversed(j)) :
                    clean_text.remove(j)
        # we modify the initial number of interactions by the newest value : ok
        clean_text.insert(0,str(len(clean_text)))
        # we write into a new tabulated file the modifications
        with open(fileout, "w+", encoding="utf-8") as file_writer:
            file_writer.write(clean_text[0]+"\n")
            for i in clean_text[1:]:
                file_writer.write(str(i[0]) + "\t" + str(i[1])+"\n")

    def get_degree(self, prot) :
        '''
        Return the protein degree.

        Args :
            prot : the name of a protein existing in the file
        Output :
            protein_degree : an int (number of vertices that are linked to the protein)
        '''
        if prot not in self.get_int_dict() :
            raise ValueError("This protein is not in this graph")
        protein_degree = len(self.get_int_dict()[prot])
        return protein_degree

    def get_max_degree(self) :
        '''
        Return the maximum degree of the file.

        Output :
            proteins : a str (name of the protein(s) that have the maximum degree)
            max_degree : an int (maximum degree of the file)
        '''
        max_degree = max(len(item) for item in self.get_int_dict().values())
        protein = tuple(key for key, values in self.get_int_dict().items()
                        if len(values) == max_degree)
        return protein, max_degree

    def get_ave_degree(self) :
        '''
        Return the mean degree of the file.

        Output :
            mean_degree : an int (mean degree of the file)
        '''
        sum_degree = 0
        for prot in self.get_int_dict() :
            sum_degree += len(self.get_int_dict()[prot])
        count_prot = len(self.get_int_dict())
        mean_degree = round(sum_degree/count_prot, 4)
        return mean_degree

    def count_degree(self, deg) :
        '''
        Return the number of proteins that have the same degree as the one in the argument.

        Args :
            deg : the degree we want to explore
        Output :
            same_degree_prot : an int (number of proteins that have the same degree)
        '''
        if deg < 0 :
            raise ValueError("You must choose a positive degree")
        same_degree_prot = 0
        for prot in self.get_int_dict() :
            if len(self.get_int_dict()[prot]) == deg :
                same_degree_prot += 1
        return same_degree_prot

    def histogram_degree(self, dmin, dmax) :
        '''
        Print for a given range [dmin, dmax] the number of proteins that have the degree d.

        Args :
            dmin : the minimum degree of the range
            dmax : the maximum degree of the range
        Output :
            print histogram_degree() : print a "*" for every proteins that have the degree nb_deg
        '''
        count_prot = 0
        deg_int = {}
        for deg in range(dmin, dmax+1):
            if deg not in deg_int :
                deg_int[deg] = self.count_degree(deg)
            else:
                count_prot += self.count_degree(deg)
        for nb_deg, nb_prot in deg_int.items():
            print(str(nb_deg), nb_prot*"*", sep=" ")
    
    def density(self) :
        '''
        density : number of edges in the interactome / maximal number of edges that the interactome
        could have
        ok
        0.4 --> toy_example
        '''
        max_edges = self.count_vertices()*(self.count_vertices()-1)/2   # n*(n-1)/2
        density = round(self.count_edges() / max_edges, 4)              # edges / max_edges
        return density

    def clustering(self, prot) :
        '''
        C_A = 1/1 = 1 ; C_B = 1/3 ; C_C = 1/3 ; C_D = 0/3 = 0 ; C_E = 0/0 = 0 ; C_F = 0/0 = 0
        '''
        max_degree_prot = self.get_degree(prot)*(self.get_degree(prot)-1)/2
        if max_degree_prot == 0:
            coeff_clustering = float(0)
        else:
            count = 0
            for i in self.get_int_dict()[prot]:
                for j in self.get_int_dict()[i]:
                    if j in self.get_int_dict()[prot]:
                        count+=1
            if count >0:
                count -= 1
            coeff_clustering = count/max_degree_prot
        return coeff_clustering
    
    def ER_graph(self):
        '''
        GENERATING ERDÖS-RÉNYI RANDOM GRAPHS G(n, M) where n = number of vertices, and M = number of edges
        P(k)=ck^y
        '''
        G = nx.Graph()
        #G.add_nodes_from(self.get_int_list())
        G.add_edges_from(self.get_int_list())
        return G
    
    def barabasi_graph(self, n, m):
        '''
        GENERATING BARABASI RANDOM GRAPHS 
        '''
        pass
    
if __name__ == "__main__" :
    interactome1 = Interactome("toy_example.txt")   # objet de la classe Interactome
    interactome2 = Interactome("Human_HighQuality.txt")
    print(interactome1.ER_graph())
    #false_interactome1 = Interactome("false_file_example-1.txt")
    #false_interactome2 = Interactome("false_file_example-2.txt")
    #false_interactome3 = Interactome("false_file_example-3.txt")
    #false_interactome4 = Interactome("false_file_example-4.txt")
    #interactome_to_clean = Interactome("toy_example_to_clean.txt")
