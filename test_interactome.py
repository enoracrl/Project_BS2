'''
Testing functions for the interactome.py file
'''

__authors__ = ("Enora CORLER", "Léa BEAULIEU")
__contact__ = ("enora.corler@etudiant.univ-rennes1.fr", "lea.beaulieu@etudiant.univ-rennes1.fr")
__date__ = "17/10/2022"

'''
Importation of necessary modules
'''

from calendar import c
import numpy as np
import unittest
from interactome import *

'''
Testing files
'''
file_test_1 = "toy_example.txt"           # simple file with only 6 interactions between letters
# complex file with 27276 interactions
file_test_2 = "Human_HighQuality.txt"

# a file without the number of interactions on the first line
false_file_1 = "false_file_example-1.txt"
false_file_2 = "false_file_example-2.txt"     # an empty file
false_file_2 = "false_file_example-2.txt"     # a empty file
# a file with a number of lines =/= number of interactions
false_file_3 = "false_file_example-3.txt"
# a file with a wrong number of columns
false_file_4 = "false_file_example-4.txt"


class test_results(unittest.TestCase):

    def test_is_interaction_file(self):
        file1 = Interactome(file_test_1)
        file1.__init__(file_test_1)
        self.assertTrue(file1.is_interaction_file())
        print(f"test_is_interaction_file file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.__init__(file_test_2)
        self.assertTrue(file2.is_interaction_file())
        print(f"test_is_interaction_file file_2\033[92m passed \033[0m")
        false_file1 = Interactome(false_file_1)
        false_file1.__init__(false_file_1)
        self.assertFalse(false_file1.is_interaction_file())
        print(f"test_is_interaction_file false_file_1\033[92m passed \033[0m")
        false_file2 = Interactome(false_file_2)
        false_file2.__init__(false_file_2)
        self.assertFalse(false_file2.is_interaction_file())
        print(f"test_is_interaction_file false_file_2\033[92m passed \033[0m")
        false_file3 = Interactome(false_file_3)
        false_file3.__init__(false_file_3)
        self.assertFalse(false_file3.is_interaction_file())
        print(f"test_is_interaction_file falsefile_3\033[92m passed \033[0m")
       

    def test_count_vertices(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.count_vertices(), 6)
        print(f"test_count_vertices file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.count_vertices(), 9596)
        print(f"test_count_vertices file_2\033[92m passed \033[0m")

    def test_count_edges(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.count_edges(), 6)
        print(f"test_count_edges file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.count_edges(), 27276)
        print(f"test_count_edges file_2\033[92m passed \033[0m")

    def test_get_degree(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.get_degree("A"), 2)
        print(f"test_get_degree file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.get_degree("1433B_HUMAN"), 49)
        print(f"test_get_degree file_2\033[92m passed \033[0m")
        self.assertRaises(ValueError, file1.get_degree, "G")
        print(f"test_get_degree error_file_1\033[92m passed \033[0m")

    def test_get_max_degree(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.get_max_degree(), (('B', 'D'), 3))
        print(f"test_get_max_degree file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.get_max_degree(), (('ATX1_HUMAN',), 207))
        print(f"test_get_max_degree file_2\033[92m passed \033[0m")

    def test_get_ave_degree(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.get_ave_degree(), 2.0)
        print(f"test_get_ave_degree file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.get_ave_degree(), 5.6849)
        print(f"test_get_ave_degree file_2\033[92m passed \033[0m")

    def test_count_degree(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.count_degree(2), 2)
        print(f"test_count_degree file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.count_degree(2), 1633)
        print(f"test_count_degree file_2\033[92m passed \033[0m")
        self.assertRaises(ValueError, file1.count_degree, -10)
        print(f"test_count_degree error_file_1\033[92m passed \033[0m")

    def test_histogram_degree(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        file1 = Interactome(file_test_1)
        file1.histogram_degree(1, 2)
        sys.stdout = sys.__stdout__
        print(f"test_histogram_degree file_1\033[92m passed \033[0m")
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        file2 = Interactome(file_test_2)
        file2.histogram_degree(9, 9)
        sys.stdout = sys.__stdout__
        print(f"test_histogram_degree file_1\033[92m passed \033[0m")

    def test_density(self):
        file1 = Interactome(file_test_1)
        self.assertEqual(file1.density(), 0.4)
        print(f"test_density file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        self.assertEqual(file2.density(), 0.0006)
        print(f"test_density file_2\033[92m passed \033[0m")

    def test_clustering(self):
        file1 = Interactome(file_test_1)
        file1.get_int_dict()
        self.assertEqual(file1.clustering("A"), 1.0)
        print(f"test_clustering file_1\033[92m passed \033[0m")
        file2 = Interactome(file_test_2)
        file2.get_int_dict()
        self.assertEqual(file2.clustering("1433B_HUMAN"), 0.10459183673469388)
        print(f"test_clustering file_2\033[92m passed \033[0m")
        

if __name__ == '__main__':
    unittest.main()
