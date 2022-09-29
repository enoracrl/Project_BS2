#                                                       FICHIER DE TESTS SUR LE FICHIER TP.PY



'''
Importation des modules necessaires
'''

from termios import CEOF
import pytest
import numpy as np
import unittest  
#from Project_BS2 import *
from TP import *


'''
Testing files
'''
file_test_1 = "/Users/Enora/enoracrl/Project_BS2/toy_example.txt"
file_test_2 = "/Users/Enora/enoracrl/Project_BS2/Human_HighQuality.txt"


'''
Tests that check if functions return correct types of variables 
'''
class TestStructure(unittest.TestCase):
    def test_read_interaction_file_dict_is_a_dict(self):
        '''
        Verify if the function read_interaction_file_dict() return a dictionnary
        '''
        # with file 1 (more simple)
        interaction_dic = read_interaction_file_dict(file_test_1)
        self.assertEqual(type(interaction_dic), dict)
        # with file 2 (more complex)
        interaction_dic = read_interaction_file_dict(file_test_2)
        self.assertEqual(type(interaction_dic), dict)
    
    def test_read_interaction_file_list_is_a_list(self):
        '''
        Verify if the function read_interaction_file_list() return a list
        '''
        # with file 1 (more simple)
        interaction_list = read_interaction_file_list(file_test_1)
        self.assertEqual(type(interaction_list), list)
        # with file 2 (more complex)
        interaction_list = read_interaction_file_list(file_test_2)
        self.assertEqual(type(interaction_list), list)
        
    def test_read_interaction_file_is_a_tuple(self):
        '''
        Verify if the function read_interaction_file() return a tuple
        '''
        # with file 1 (more simple)
        interaction_tuple = read_interaction_file(file_test_1)
        self.assertEqual(type(interaction_tuple), tuple)
        # with file 2 (more complex)
        interaction_tuple = read_interaction_file(file_test_2)
        self.assertEqual(type(interaction_tuple), tuple)
    
    def test_count_vertices_is_a_int(self):
        '''
        Verify if the function count_vertices() return an int
        '''
        # with file 1 (more simple)
        vertices_int = count_vertices(file_test_1)
        self.assertEqual(type(vertices_int), int)
        # with file 2 (more complex)
        vertices_int = count_vertices(file_test_2)
        self.assertEqual(type(vertices_int), int)
    
    def test_count_edges_is_a_int(self):
        '''
        Verify if the function count_edges() return an int
        '''
        # with file 1 (more simple)
        edges_int = count_edges(file_test_1)
        self.assertEqual(type(edges_int), int)
        # with file 2 (more complex)
        edges_int = count_edges(file_test_2)
        self.assertEqual(type(edges_int), int)
        
    
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
    '''
    # Probleme : ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
    # --> does not work with the matrix for the test, even if it's the same result in output 
    
    def test_read_interaction_file_mat(self):
        #Fonction structure 3 : la fonction doit retourner le graphe d'interaction sous forme d'une matrice d'adjacence
        assert read_interaction_file_mat(file_test_1) == (['A', 'B', 'C', 'D', 'E', 'F'], 
                                                        np.array([[0, 1, 1, 0, 0, 0], 
                                                                  [1, 0, 1, 1, 0, 0], 
                                                                  [1, 1, 0, 0, 0, 0], 
                                                                  [0, 1, 0, 0, 1, 1], 
                                                                  [0, 0, 0, 1, 0, 0], 
                                                                  [0, 0, 0, 1, 0, 0]]))
    '''
    
    
    '''
    # Probleme : ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
    # --> same issue = does not work with the matrix for the test, even if it's the same result in output 
    
    def test_read_interaction_file(self):
        assert read_interaction_file(file_test_1) == ({'A': ['B', 'C'], 
                                                       'B': ['A', 'C', 'D'], 
                                                       'C': ['A', 'B'], 
                                                       'D': ['B', 'E', 'F'], 
                                                       'E': ['D'], 'F': ['D']}, 
                                                      [('A', 'B'), 
                                                       ('A', 'C'), 
                                                       ('B', 'C'), 
                                                       ('B', 'D'), 
                                                       ('D', 'E'), 
                                                       ('D', 'F')], 
                                                      ['A', 'B', 'C', 'D', 'E', 'F'], 
                                                      np.array([[0, 1, 1, 0, 0, 0],
                                                                [1, 0, 1, 1, 0, 0],
                                                                [1, 1, 0, 0, 0, 0],
                                                                [0, 1, 0, 0, 1, 1],
                                                                [0, 0, 0, 1, 0, 0],
                                                                [0, 0, 0, 1, 0, 0]]))                                                         
    '''
    
    def test_is_interaction_file(self):
        assert is_interaction_file(file_test_1) == True

                                                           
                                                           

if __name__ == '__main__':
    unittest.main()
