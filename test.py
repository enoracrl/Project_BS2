import pytest
import numpy as np
import unittest  
#from Project_BS2 import *
from TP import *


'''
Fichiers de test
'''
file_test_1 = "/Users/Enora/enoracrl/Project_BS2/toy_example.txt"
#file_test_2 = "/Users/Enora/enoracrl/Project_BS2/Human_HighQuality.txt"


#script = pytest.importorskip("TP")

class TestStructure(unittest.TestCase):
    def test_read_interaction_file_dict_is_a_dict(self):
        dic = read_interaction_file_dict(file_test_1)
        self.assertEqual(type(dic), dict)
        #dic = read_interaction_file_dict(file_test_2)
        #self.assertEqual(type(dic), dict)

class Test_Results(unittest.TestCase):
    def test_read_interaction_file_dict(self):
        #Fonction structure 1 : la fonction doit retourner le graphe d'interaction sous forme d'un dictionnaire
        assert read_interaction_file_dict(file_test_1) == {'A': ['B', 'C'], 
                                                           'B': ['A', 'C', 'D'], 
                                                           'C': ['A', 'B'], 
                                                           'D': ['B', 'E', 'F'], 
                                                           'E': ['D'], 
                                                           'F': ['D']}
    def test_read_interaction_file_list(self):
    #Fonction structure 2 : la fonction doit retourner le graphe d'interaction sous forme d'une liste de couples
        assert read_interaction_file_list(file_test_1) == [('A', 'B'), 
                                                           ('A', 'C'),
                                                           ('B', 'C'), 
                                                           ('B', 'D'), 
                                                           ('D', 'E'), 
                                                           ('D', 'F')]    
    '''def test_read_interaction_file_mat(self):
        #Fonction structure 3 : la fonction doit retourner le graphe d'interaction sous forme d'une matrice d'adjacence
        assert read_interaction_file_mat(file_test_1) == (['A', 'B', 'C', 'D', 'E', 'F'], 
                                                        np.array([[0, 1, 1, 0, 0, 0], 
                                                                  [1, 0, 1, 1, 0, 0], 
                                                                  [1, 1, 0, 0, 0, 0], 
                                                                  [0, 1, 0, 0, 1, 1], 
                                                                  [0, 0, 0, 1, 0, 0], 
                                                                  [0, 0, 0, 1, 0, 0]]))'''
                                                           
                                                           

if __name__ == '__main__':
    unittest.main()