'''
Testing functions for the interactome.py file
'''

__authors__ = ("Enora CORLER", "Léa BEAULIEU")
__contact__ = ("enora.corler@etudiant.univ-rennes1.fr", "lea.beaulieu@etudiant.univ-rennes1.fr")
__date__ = "17/10/2022"

'''
Importation of necessary modules
'''

import numpy as np
import unittest
import io
import sys
from interactome import *
import networkx.algorithms.isomorphism as iso

'''
Testing files
'''


false_file_1 = "false_file_example-1.txt"   # a file without the number of interactions on the first line
false_file_2 = "false_file_example-2.txt"   # an empty file  
false_file_3 = "false_file_example-3.txt"   # a file with a number of lines =/= number of interactions
false_file_4 = "false_file_example-4.txt"   # a file with a wrong number of columns


class test_results(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        "Initiation of Class Interactome with our 2 tests files."
        super(test_results, self).__init__(*args, **kwargs)
        self.file1 = Interactome("toy_example.txt")
        self.file2 = Interactome("Human_HighQuality.txt")

    def test_instance(self):
        "Tests if self.file is an object of Interactome and has been correctly initiated."
        self.assertTrue(isinstance(self.file1, Interactome))
        print(f"test_instance file_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2, Interactome))
        print(f"test_instance file_2\033[92m passed \033[0m")

    def test_file_is_a_str(self):
        "Tests if the file we use is a string file."
        self.assertTrue(isinstance(self.file1.file, str))
        print(f"test_file_is_a_str file_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.file, str))
        print(f"test_file_is_a_str file_2\033[92m passed \033[0m")

    def test_int_list_is_a_list(self):
        "Tests if file.int_list is a list."
        self.assertTrue(isinstance(self.file1.int_list, list))
        print(f"test_int_list_is_a_list file_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.int_list, list))
        print(f"test_int_list_is_a_list file_2\033[92m passed \033[0m")

    def test_int_list(self):
        "Tests if it returns the right list for the first test file."
        self.assertEqual(self.file1.int_list, [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('D', 'E'), ('D', 'F')])
        print(f"test_int_list file_1\033[92m passed \033[0m")

    def test_int_dict_is_a_dict(self):
        "Tests if file.int_dict is a dictionnary."
        self.assertTrue(isinstance(self.file1.int_dict, dict))
        print(f"test_int_dict_is_a_dict file_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.int_dict, dict))
        print(f"test_int_dict_is_a_dict file_2\033[92m passed \033[0m")

    def test_int_dict(self):
        "Tests if it returns the right dictionnary for the first test file."
        self.assertEqual(self.file1.int_dict, {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B'], 'D': ['B', 'E', 'F'], 'E': ['D'], 'F': ['D']})
        print(f"test_int_dict file_1\033[92m passed \033[0m")

    '''def test_mat_is_a_mat(self):
        "Tests if file.mat is a matrix"
        self.assertTrue(isinstance(self.file1.get_mat, np.ndarray))
        print(f"test_int_list_is_a_list file_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.get_mat, np.ndarray))
        print(f"test_int_list_is_a_list file_2\033[92m passed \033[0m")
 
    def test_mat(self):
        "Tests if it returns the right dictionnary for the first test file."
        self.assertEqual(self.file1.get_mat, [[0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]])
        print(f"test_mat file_1\033[92m passed \033[0m")'''

    def test_is_interaction_file(self):
        "Tests if is_interaction_file returns True and not None with the right file."
        self.assertTrue(self.file1.is_interaction_file())
        self.assertIsNotNone(self.file1.is_interaction_file())
        print(f"test_is_interaction_file file_1\033[92m passed \033[0m")
        self.assertTrue(self.file2.is_interaction_file())
        self.assertIsNotNone(self.file2.is_interaction_file())
        print(f"test_is_interaction_file file_2\033[92m passed \033[0m")

    def test_is_not_interaction_file(self):
        "Tests if is_interaction_file returns False and not None when the file contains an error."
        false_file1 = Interactome(false_file_1)
        false_file1.__init__(false_file_1)
        self.assertFalse(false_file1.is_interaction_file())
        self.assertIsNotNone(false_file1.is_interaction_file())
        print(f"test_is_not_interaction_file false_file_1\033[92m passed \033[0m")
        false_file2 = Interactome(false_file_2)
        false_file2.__init__(false_file_2)
        self.assertFalse(false_file2.is_interaction_file())
        self.assertIsNotNone(false_file2.is_interaction_file())
        print(f"test_is_not_interaction_file false_file_2\033[92m passed \033[0m")
        false_file3 = Interactome(false_file_3)
        false_file3.__init__(false_file_3)
        self.assertFalse(false_file3.is_interaction_file())
        self.assertIsNotNone(false_file3.is_interaction_file())
        print(f"test_is_not_interaction_file falsefile_3\033[92m passed \033[0m")
       
    def test_count_vertices(self):
        "Tests if the function count_vertices return the right number and not None."
        self.assertEqual(self.file1.count_vertices(), 6)
        self.assertIsNotNone(self.file1.count_vertices())
        print(f"test_count_vertices file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.count_vertices(), 9596)
        self.assertIsNotNone(self.file2.count_vertices())
        print(f"test_count_vertices file_2\033[92m passed \033[0m")

    def test_count_edges(self):
        "Tests if the function count_edges return the right number and not None."
        self.assertEqual(self.file1.count_edges(), 6)
        self.assertIsNotNone(self.file1.count_edges())
        print(f"test_count_edges file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.count_edges(), 27276)
        self.assertIsNotNone(self.file2.count_edges())
        print(f"test_count_edges file_2\033[92m passed \033[0m")

    def test_get_degree(self):
        "Tests if the function get_degree return the right number and not None and raise an ValueError."
        self.assertEqual(self.file1.get_degree("A"), 2)
        self.assertIsNotNone(self.file1.get_degree("A"))
        print(f"test_get_degree file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.get_degree("1433B_HUMAN"), 49)
        self.assertIsNotNone(self.file2.get_degree("1433B_HUMAN"))
        print(f"test_get_degree file_2\033[92m passed \033[0m")
        self.assertRaises(ValueError, self.file1.get_degree, "G")
        print(f"test_get_degree error_file_1\033[92m passed \033[0m")

    def test_get_max_degree(self):
        "Tests if the function get_max_degree return the right number and not None."
        self.assertEqual(self.file1.get_max_degree(), (('B', 'D'), 3))
        self.assertIsNotNone(self.file1.get_max_degree())
        print(f"test_get_max_degree file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.get_max_degree(), (('ATX1_HUMAN',), 207))
        self.assertIsNotNone(self.file2.get_max_degree())
        print(f"test_get_max_degree file_2\033[92m passed \033[0m")

    def test_get_ave_degree(self):
        "Tests if the function ave_degree return the right number and not None."
        self.assertEqual(self.file1.get_ave_degree(), 2.0)
        self.assertIsNotNone(self.file1.get_ave_degree())
        print(f"test_get_ave_degree file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.get_ave_degree(), 5.6849)
        self.assertIsNotNone(self.file2.get_ave_degree())
        print(f"test_get_ave_degree file_2\033[92m passed \033[0m")

    def test_count_degree(self):
        "Tests if the function count_degree return the right number and not None and raise a ValueError."
        self.assertEqual(self.file1.count_degree(2), 2)
        self.assertIsNotNone(self.file1.count_degree(2))
        print(f"test_count_degree file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.count_degree(2), 1633)
        self.assertIsNotNone(self.file2.count_degree(2))
        print(f"test_count_degree file_2\033[92m passed \033[0m")
        self.assertRaises(ValueError, self.file1.count_degree, -10)
        print(f"test_count_degree error_file_1\033[92m passed \033[0m")

    def test_histogram_degree(self):
        "Tests if the function histogram_degree print the right thing and returns None."
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sys.stdout = sys.__stdout__
        self.assertIsNone(self.file1.histogram_degree(1, 2))
        print(f"test_histogram_degree file_1\033[92m passed \033[0m")
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sys.stdout = sys.__stdout__
        self.assertIsNone(self.file2.histogram_degree(9, 9))
        print(f"test_histogram_degree file_1\033[92m passed \033[0m")

    def test_density(self):
        "Tests if the function test_density return the right number and not None."
        self.assertEqual(self.file1.density(), 0.4)
        self.assertIsNotNone(self.file1.density())
        print(f"test_density file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.density(), 0.0006)
        self.assertIsNotNone(self.file2.density())
        print(f"test_density file_2\033[92m passed \033[0m")

    def test_clustering(self):
        "Tests if the function test_clustering return the right number and not None."
        self.assertEqual(self.file1.clustering("A"), 1.0)
        self.assertIsNotNone(self.file1.clustering("A"))
        print(f"test_clustering file_1\033[92m passed \033[0m")
        self.assertEqual(self.file2.clustering("1433B_HUMAN"), 0.027210884353741496)
        self.assertIsNotNone(self.file2.clustering("1433B_HUMAN"))
        print(f"test_clustering file_2\033[92m passed \033[0m")

    def test_graph_ER(self):
        "Tests if the function graph_ER return correct graphs and not None."
        self.assertIsNotNone(self.file1.graph_ER(0.81))
        G1 = self.file1.graph_ER(0.81)
        G2 = self.file1.graph_ER(1)
        G3 = self.file1.graph_ER(0.81)
        nx.add_path(G1, [1,2,3,4], weight = 1)
        nx.add_path(G2, [10,20,30,40], weight = 2)
        nx.add_path(G3, [1,2,3,4], weight = 1)
        em = iso.numerical_edge_match('weight', 1)
        self.assertFalse(nx.is_isomorphic(G1, G2))
        self.assertTrue(nx.is_isomorphic(G1, G1, edge_match = em))
        print(f"test_graph_ER file_1\033[92m passed \033[0m")
        

if __name__ == '__main__':
    unittest.main()
