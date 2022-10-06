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

class Interactome :
    '''
    class
    '''
    def __init__(self, file):#, int_list, int_dict, proteins):
        '''
        constructeur avec attributs d'instances
        '''
        self.file = file
        self.matrix = []
        #self.text = []
        int_dict = {}
        int_list = []
        text = []
        with open(file, 'r', encoding="utf-8") as file_reader :
            for line in file_reader.readlines()[1:] :
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
        self.int_list = int_list
        self.int_dict = int_dict
        '''count = sum([len(elem) for elem in self.text[1:]])
        if self.text != [] and self.text[0][0].isnumeric() is True :
            if len(self.text[1:]) == int(text[0][0]) and count % 2 == 0:
                return True
        return False'''

    # ACCESSEURS
    def get_int_list(self):
        '''
        ok tested
        '''
        return self.int_list

    def get_int_dict(self):
        '''
        ok tested
        '''
        return self.int_dict

    def get_mat(self):
        '''
        ok tested
        '''
        self.matrix = self.read_interaction_file_mat()[1]
        return self.matrix

    def read_interaction_file_mat(self):
        '''
        ok tested
        '''
        proteins = list(self.int_dict.keys())
        matrix = np.zeros((len(proteins), len(proteins)), dtype=int)
        for key, values in self.int_dict.items():
            for value in values:
                matrix[proteins.index(key), proteins.index(value)] = 1
        return proteins, matrix

    def read_interaction_file(self) :
        '''
        ok tested
        '''
        return (self.get_int_dict(), self.get_int_list(), self.read_interaction_file_mat()[0],
                self.get_mat())

    def is_interaction_file(self):
        '''
        ko tested maybe in constructor directly ?
        '''
        interactions = str(len(self.get_int_list()))
        self.text.insert(0, interactions)
        count = sum([len(elem) for elem in self.text[1:]])
        if self.text[0][0].isnumeric() is True :
            if len(self.text[1:]) == int(self.text[0]) and count % 2 == 0:
                return True
        return False

    def count_vertices(self) :
        '''
        ok tested
        '''
        number_of_vertices = len(self.get_int_dict().keys())
        return number_of_vertices

    def count_edges(self) :
        '''
        ok tested
        '''
        number_of_edges = len(self.get_int_list())
        return number_of_edges

    def clean_interactome(self, fileout):
        '''
        ok tested but maybe in constructor as well?
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
        ok tested
        '''
        if prot not in self.get_int_dict() :
            raise ValueError("This protein is not in this graph")
        protein_degree = len(self.get_int_dict()[prot])
        return protein_degree

    def get_max_degree(self) :
        '''
        ok tested but if only one prot --> tuple like "("prot",)"
        --> should be "("prot")" or "prot" !!!
        '''
        max_degree = max(len(item) for item in self.get_int_dict().values())
        protein = tuple(key for key, values in self.get_int_dict().items()
                        if len(values) == max_degree)
        return protein, max_degree

    def get_ave_degree(self) :
        '''
        ok tested
        '''
        sum_degree = 0
        for prot in self.get_int_dict() :
            sum_degree += len(self.get_int_dict()[prot])
        count_prot = len(self.get_int_dict())
        mean_degree = round(sum_degree/count_prot, 4)
        return mean_degree

    def count_degree(self, deg):
        '''
        ok tested
        '''
        if deg < 0 :
            raise ValueError("You must choose a positive degree")
        same_degree_prot = 0
        for prot in self.get_int_dict() :
            if len(self.get_int_dict()[prot]) == deg :
                same_degree_prot += 1
        return same_degree_prot

    def histogram_degree(self, dmin, dmax):
        '''
        ok tested
        inclus : ]dmin, dmax[
        '''
        count_prot = 0
        deg_int = {}
        for deg in range(dmin, dmax+1):
            if deg not in deg_int.keys():
                deg_int[deg] = self.count_degree(deg)
            else:
                count_prot += self.count_degree(deg)
        for nb_deg, nb_prot in deg_int.items():
            print(str(nb_deg), nb_prot*"*", sep=" ")

if __name__ == "__main__":
    interactome1 = Interactome("toy_example.txt")   # objet de la classe Interactome
    interactome2 = Interactome("Human_HighQuality.txt")
    #false_interactome1 = Interactome("false_file_example-1.txt")
    #false_interactome2 = Interactome("false_file_example-2.txt")
    #false_interactome3 = Interactome("false_file_example-3.txt")
    #false_interactome4 = Interactome("false_file_example-4.txt")
    interactome_to_clean = Interactome("toy_example_to_clean.txt")
    print(interactome2.get_mat())
