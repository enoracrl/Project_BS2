#                                                       FICHIER DE TESTS SUR LE FICHIER TP.PY


'''
Importation of necessary modules
'''

import numpy as np
import unittest
from TP import *


'''
Testing files
'''
file_test_1 = "/Users/Enora/enoracrl/Project_BS2/toy_example.txt"           # simple file with only 6 interactions between letters
# complex file with 27276 interactions
file_test_2 = "/Users/Enora/enoracrl/Project_BS2/Human_HighQuality.txt"

# a file without the number of interactions on the first line
false_file_1 = "/Users/Enora/enoracrl/Project_BS2/false_file_example-1.txt"
false_file_2 = "/Users/Enora/enoracrl/Project_BS2/false_file_example-2.txt"     # a empty file
# a file with a number of lines =/= number of interactions
false_file_3 = "/Users/Enora/enoracrl/Project_BS2/false_file_example-3.txt"
# a file with a wrong number of columns
false_file_4 = "/Users/Enora/enoracrl/Project_BS2/false_file_example-4.txt"

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
        print(
            f"test_read_interaction_file_dict_is_a_dict file_1\033[92m passed \033[0m")
        # with file 2 (more complex)
        interaction_dic = read_interaction_file_dict(file_test_2)
        self.assertEqual(type(interaction_dic), dict)
        print(
            f"test_read_interaction_file_dict_is_a_dict file_2\033[92m passed \033[0m")

    def test_read_interaction_file_list_is_a_list(self):
        '''
        Verify if the function read_interaction_file_list() return a list
        '''
        # with file 1 (more simple)
        interaction_list = read_interaction_file_list(file_test_1)
        self.assertEqual(type(interaction_list), list)
        print(
            f"test_read_interaction_file_list_is_a_list file_1\033[92m passed \033[0m")
        # with file 2 (more complex)
        interaction_list = read_interaction_file_list(file_test_2)
        self.assertEqual(type(interaction_list), list)
        print(
            f"test_read_interaction_file_list_is_a_list file_2\033[92m passed \033[0m")

    def test_read_interaction_file_is_a_tuple(self):
        '''
        Verify if the function read_interaction_file() return a tuple
        '''
        # with file 1 (more simple)
        interaction_tuple = read_interaction_file(file_test_1)
        self.assertEqual(type(interaction_tuple), tuple)
        print(
            f"test_read_interaction_file_list_is_a_tuple file_1\033[92m passed \033[0m")
        # with file 2 (more complex)
        interaction_tuple = read_interaction_file(file_test_2)
        self.assertEqual(type(interaction_tuple), tuple)
        print(
            f"test_read_interaction_file_list_is_a_tuple file_2\033[92m passed \033[0m")

    def test_count_vertices_is_a_int(self):
        '''
        Verify if the function count_vertices() return an int
        '''
        # with file 1 (more simple)
        vertices_int = count_vertices(file_test_1)
        self.assertEqual(type(vertices_int), int)
        print(f"test_count_vertices_is_a_int file_2\033[92m passed \033[0m")
        # with file 2 (more complex)
        vertices_int = count_vertices(file_test_2)
        self.assertEqual(type(vertices_int), int)
        print(f"test_count_vertices_is_a_int file_2\033[92m passed \033[0m")

    def test_count_edges_is_a_int(self):
        '''
        Verify if the function count_edges() return an int
        '''
        # with file 1 (more simple)
        edges_int = count_edges(file_test_1)
        self.assertEqual(type(edges_int), int)
        print(f"test_count_edges_is_a_int file_2\033[92m passed \033[0m")
        # with file 2 (more complex)
        edges_int = count_edges(file_test_2)
        self.assertEqual(type(edges_int), int)
        print(f"test_count_edges_is_a_int file_2\033[92m passed \033[0m")

        
'''
Tests that check if functions work properly 
'''

class Test_Results(unittest.TestCase):
    def test_read_interaction_file_dict(self):
        # Fonction structure 1 : la fonction doit retourner le graphe d'interaction sous forme d'un dictionnaire
        assert read_interaction_file_dict(file_test_1) == {'A': ['B', 'C'],
                                                           'B': ['A', 'C', 'D'],
                                                           'C': ['A', 'B'],
                                                           'D': ['B', 'E', 'F'],
                                                           'E': ['D'],
                                                           'F': ['D']}
        print(f"test_read_interaction_file_dict file_1\033[92m passed \033[0m")

    def test_read_interaction_file_list(self):
        # Fonction structure 2 : la fonction doit retourner le graphe d'interaction sous forme d'une liste de couples
        assert read_interaction_file_list(file_test_1) == [('A', 'B'),
                                                           ('A', 'C'),
                                                           ('B', 'C'),
                                                           ('B', 'D'),
                                                           ('D', 'E'),
                                                           ('D', 'F')]
        print(f"test_read_interaction_file_list file_1\033[92m passed \033[0m")

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
        print(f"test_is_interaction_file file_1\033[92m passed \033[0m")
        assert is_interaction_file(file_test_2) == True
        print(f"test_is_interaction_file file_2\033[92m passed \033[0m")
        assert is_interaction_file(false_file_1) == False
        print(f"test_is_interaction_file false_file_1\033[92m passed \033[0m")
        assert is_interaction_file(false_file_2) == False
        print(f"test_is_interaction_file false_file_2\033[92m passed \033[0m")
        assert is_interaction_file(false_file_3) == False
        print(f"test_is_interaction_file false_file_3\033[92m passed \033[0m")
        assert is_interaction_file(false_file_4) == False
        print(f"test_is_interaction_file false_file_4\033[92m passed \033[0m")

    def test_count_vertices(self):
        assert count_vertices(file_test_1) == 6
        print(f"test_count_vertices file_1\033[92m passed \033[0m")
        assert count_vertices(file_test_2) == 9596
        print(f"test_count_vertices file_2\033[92m passed \033[0m")

    def test_count_edges(self):
        assert count_edges(file_test_1) == 6
        print(f"test_count_edges file_1\033[92m passed \033[0m")
        assert count_edges(file_test_2) == 27276
        print(f"test_count_edges file_2\033[92m passed \033[0m")

    def test_clean_interactome(self):
        pass
    
    def test_get_degree(self):
        assert get_degree(file_test_1, "A") == 2
        print(f"test_get_degree file_1\033[92m passed \033[0m")
        assert get_degree(file_test_2, "1433B_HUMAN") == 49
        print(f"test_get_degree file_2\033[92m passed \033[0m")
        self.assertRaises(ValueError, get_degree, file_test_1, "G")
        print(f"test_get_degree file_1\033[92m passed \033[0m")

    def test_get_max_degree(self):
        assert get_max_degree(file_test_1) == (('B', 'D'), 3)
        print(f"test_get_max_degree file_1\033[92m passed \033[0m")
        assert get_max_degree(file_test_2) == (('ATX1_HUMAN',), 207)
        print(f"test_get_max_degree file_2\033[92m passed \033[0m")
    
    def test_get_ave_degree(self):
        assert get_ave_degree(file_test_1) == 2.0
        print(f"test_get_ave_degree file_1\033[92m passed \033[0m")
        assert get_ave_degree(file_test_2) == 5.6849
        print(f"test_get_ave_degree file_2\033[92m passed \033[0m")
    
    def test_count_degree(self):
        assert count_degree(file_test_1, 2) == 2
        print(f"test_count_degree file_1\033[92m passed \033[0m")
        assert count_degree(file_test_2, 2) == 1633
        print(f"test_count_degree file_2\033[92m passed \033[0m")

def test_histogram_degree(self):
        assert histogram_degree(file_test_1, 1, 2) == "1 **\n2 **\n"
        print(f"test_histogram_degree file_1\033[92m passed \033[0m")
        assert histogram_degree(file_test_2, 9, 9) == "9 *********************************************************************************************************************************************************************************************************************\n"
        print(f"test_histogram_degree file_2\033[92m passed \033[0m")


    
if __name__ == '__main__':
    unittest.main()
