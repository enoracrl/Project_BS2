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

import numpy as np

with open ("toy_example.txt", "r") as fh:
        lines = fh.readlines()
        #for line in lines[1:]:
print(lines)

class Interactome :
    '''
    class 
    '''
    
    
    def __init__(self, file):#, int_list, int_dict, proteins):
        '''
        constructeur avec attributs d'instances
        '''
        #self.test="test"
        self.file = file
        self.int_list = self.read_interaction_file_list()
        
        self.int_dict = self
        self.proteins = []
    
    
    # ACCESSEURS
    
    def get_int_list(self):
        return self.int_list
    
    def get_int_dict(self):
        return self.int_dict
    
    def get_proteins(self):
        return self.proteins
    
    def get_mat(self):
        return self.matrix
    
    def read_interaction_file_dict(self):
        self.int_dict = {}
        with open(file, 'r', encoding="utf-8") as file_reader:
            for line in file_reader.readlines()[1:]:
                int1, int2 = line.split()
                if int1 not in interactions_dic:
                    interactions_dic[int1] = [int2]
                else:
                    interactions_dic[int1].append(int2)
                if int2 not in interactions_dic:
                    interactions_dic[int2] = [int1]
                else:
                    interactions_dic[int2].append(int1)
        return interactions_dic
    
    def read_interaction_file_list(self):
        with open(self.file, 'r', encoding="utf-8") as file_reader:
            return [tuple(line.split()) for line in file_reader.readlines()[1:]]
        
    
    def read_interaction_file_mat(self):
        '''
        ok
        '''
        self.proteins = list(self.int_dict.keys())
        self.matrix = np.zeros((len(self.proteins), len(self.proteins)), dtype=int)
        for key, values in self.int_dict.items():
            for value in values:
                self.matrix[self.proteins.index(key), self.proteins.index(value)] = 1
        return self.proteins, self.matrix
    
    
    def read_interaction_file(self):
        '''
        ok
        '''
        return (self.get_int_dict(), self.get_int_list(), self.get_mat(), self.get_proteins())
    
    

if __name__ == "__main__":
    interactome1 = Interactome("toy_example.txt")
    interactome2 = Interactome("Human_HighQuality.txt")
    print(interactome1)
    print(interactome2)
    #print(interactome1.read_interaction_file_list())
    #print(interactome2.read_interaction_file_list())
    print(interactome1.read_interaction_file_mat())
    #list_interaction_file = read_interaction_file_list()
    #print(interactome.int_list)