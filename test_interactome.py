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
        self.assertTrue(Interactome.is_interaction_file(file_test_1))
        print(f"test_is_interaction_file file_1\033[92m passed \033[0m")
        """assert Interactome(file_test_2) == True
        print(f"test_is_interaction_file file_2\033[92m passed \033[0m")
        assert Interactome(false_file_1) == False
        print(f"test_is_interaction_file false_file_1\033[92m passed \033[0m")
        assert Interactome(false_file_2) == False
        print(f"test_is_interaction_file false_file_2\033[92m passed \033[0m")
        assert Interactome(false_file_3) == False
        print(f"test_is_interaction_file false_file_3\033[92m passed \033[0m")
        assert Interactome(false_file_4) == False
        print(f"test_is_interaction_file false_file_4\033[92m passed \033[0m")"""

    def test_count_vertices(self):
        self.assertEqual(Interactome.count_vertices(file_test_1), 6)
        #print(f"test_count_vertices file_1\033[92m passed \033[0m")
        self.assertEqual(Interactome.count_vertices(file_test_2), 9596)
        #print(f"test_count_vertices file_2\033[92m passed \033[0m")
        

if __name__ == '__main__':
    unittest.main()
