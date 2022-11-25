'''
Testing functions for the interactome.py file
'''

__authors__ = ("Enora CORLER", "Léa BEAULIEU")
__contact__ = ("enora.corler@etudiant.univ-rennes1.fr", "lea.beaulieu@etudiant.univ-rennes1.fr")
__date__ = "25/11/2022"

'''
Importation of necessary modules :
    - numpy : used to test matrix
    - unittest : used for all the tests
    - interactome : give us access to all methods from the object Interactome of the module
    - unittest.mock : allows to substitutes and imitates a real object (used to tests print output)
    - patch : means that the mock object is going to take the place of our object
'''

import unittest
from mock import patch
from interactome import Interactome, np

FILE_1 = "Examples/toy_example.txt"
FILE_2 = "Examples/Human_HighQuality.txt"
FILE_3 = "Examples/toy_example_with_3_CC.txt"

# a file without the number of interactions on the first line
FALSE_FILE_1 = "Examples/false_file_example-1.txt"
# an empty file
FALSE_FILE_2 = "Examples/false_file_example-2.txt"
# a file with a number of lines =/= number of interactions
FALSE_FILE_3 = "Examples/false_file_example-3.txt"
# a file with a wrong number of columns
FALSE_FILE_4 = "Examples/false_file_example-4.txt"
# a file to clean
FILE_TO_CLEAN = "Examples/toy_example_to_clean.txt"

class TestResults(unittest.TestCase):
    '''
    A class to test the Interactome object with different files.
    '''
    def __init__(self, *args, **kwargs):
        "Initiation of Class Interactome with our 2 tests files."
        super(TestResults, self).__init__(*args, **kwargs)
        self.file1 = Interactome(FILE_1)
        self.file2 = Interactome(FILE_2)
        self.file3 = Interactome(FILE_3)
        self.file_clean = Interactome(file=FILE_TO_CLEAN,
                                 fileout="Examples/toy_example_to_clean_cleaned.txt")
        self.false_file1 = Interactome(FALSE_FILE_1)
        self.false_file2 = Interactome(FALSE_FILE_2)
        self.false_file3 = Interactome(FALSE_FILE_3)

    def test_instance(self):
        "Tests if self.file is an object of Interactome and has been correctly initiated."
        self.assertTrue(isinstance(self.file1, Interactome))
        print(f"test_instance FILE_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2, Interactome))
        print(f"test_instance file2\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file3, Interactome))
        print(f"test_instance file3\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file_clean, Interactome))
        print(f"test_instance file_clean\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.false_file1, Interactome))
        print(f"test_instance false_file1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.false_file2, Interactome))
        print(f"test_instance false_file2\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.false_file3, Interactome))
        print(f"test_instance false_file3\033[92m passed \033[0m")

    def test_file_is_a_str(self):
        "Tests if the file we use is a string file."
        self.assertTrue(isinstance(FILE_1, str))
        print(f"test_file_is_a_str FILE_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(FILE_2, str))
        print(f"test_file_is_a_str FILE_2\033[92m passed \033[0m")
        self.assertTrue(isinstance(FILE_3, str))
        print(f"test_file_is_a_str FILE_3\033[92m passed \033[0m")
        self.assertTrue(isinstance(FILE_TO_CLEAN, str))
        print(f"test_file_is_a_str FILE_TO_CLEAN\033[92m passed \033[0m")
        self.assertTrue(isinstance(FALSE_FILE_1, str))
        print(f"test_file_is_a_str FALSE_FILE_1\033[92m passed \033[0m")
        self.assertTrue(isinstance(FALSE_FILE_2, str))
        print(f"test_file_is_a_str FALSE_FILE_2\033[92m passed \033[0m")
        self.assertTrue(isinstance(FALSE_FILE_3, str))
        print(f"test_file_is_a_str FALSE_FILE_3\033[92m passed \033[0m")

    def test_clean_interactome(self):
        "Tests if the function clean_interactome write the right file."
        with open("Examples/toy_example_to_clean_cleaned.txt", "r",
                  encoding="utf-8") as file_reader:
            text = file_reader.read()
            self.assertEqual(text, "6\nA\tB\nA\tC\nB\tC\nB\tD\nD\tE\nD\tF\n")
        print(f"test_clean_interactome file1\033[92m passed \033[0m")

    def test_int_list_is_a_list(self):
        "Tests if file.int_list is a list."
        self.assertTrue(isinstance(self.file1.get_int_list(), list))
        print(f"test_int_list_is_a_list file1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.get_int_list(), list))
        print(f"test_int_list_is_a_list file2\033[92m passed \033[0m")

    def test_int_list(self):
        "Tests if it returns the right list for the first test file."
        self.assertEqual(self.file1.get_int_list(), [('A', 'B'),
                                                     ('A', 'C'),
                                                     ('B', 'C'),
                                                     ('B', 'D'),
                                                     ('D', 'E'),
                                                     ('D', 'F')])
        print(f"test_int_list file1\033[92m passed \033[0m")

    def test_int_dict_is_a_dict(self):
        "Tests if file.int_dict is a dictionnary."
        self.assertTrue(isinstance(self.file1.get_int_dict(), dict))
        print(f"test_int_dict_is_a_dict file1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.get_int_dict(), dict))
        print(f"test_int_dict_is_a_dict file2\033[92m passed \033[0m")

    def test_int_dict(self):
        "Tests if it returns the right dictionnary for the first test file."
        self.assertEqual(self.file1.get_int_dict(), {'A': ['B', 'C'],
                                                     'B': ['A', 'C', 'D'],
                                                     'C': ['A', 'B'],
                                                     'D': ['B', 'E', 'F'],
                                                     'E': ['D'],
                                                     'F': ['D']})
        print(f"test_int_dict file1\033[92m passed \033[0m")

    def test_mat_is_a_mat(self):
        "Tests if file.mat is a matrix"
        self.assertTrue(isinstance(self.file1.get_mat(), np.ndarray))
        print(f"test_int_list_is_a_list file1\033[92m passed \033[0m")
        self.assertTrue(isinstance(self.file2.get_mat(), np.ndarray))
        print(f"test_int_list_is_a_list file2\033[92m passed \033[0m")

    def test_mat(self):
        "Tests if it returns the right dictionnary for the first test file."
        np.testing.assert_equal(self.file1.get_mat(), [[0,1,1,0,0,0],
                                                       [1,0,1,1,0,0],
                                                       [1,1,0,0,0,0],
                                                       [0,1,0,0,1,1],
                                                       [0,0,0,1,0,0],
                                                       [0,0,0,1,0,0]])
        print(f"test_mat file1\033[92m passed \033[0m")

    def test_count_vertices(self):
        "Tests if the function count_vertices return the right number and not None."
        self.assertEqual(self.file1.count_vertices(), 6)
        self.assertIsNotNone(self.file1.count_vertices())
        print(f"test_count_vertices file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.count_vertices(), 9596)
        self.assertIsNotNone(self.file2.count_vertices())
        print(f"test_count_vertices file2\033[92m passed \033[0m")

    def test_count_edges(self):
        "Tests if the function count_edges return the right number and not None."
        self.assertEqual(self.file1.count_edges(), 6)
        self.assertIsNotNone(self.file1.count_edges())
        print(f"test_count_edges file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.count_edges(), 27276)
        self.assertIsNotNone(self.file2.count_edges())
        print(f"test_count_edges file2\033[92m passed \033[0m")

    def test_get_degree(self):
        "Tests if get_degree() return the right number, not None and raise an ValueError."
        self.assertEqual(self.file1.get_degree("A"), 2)
        self.assertIsNotNone(self.file1.get_degree("A"))
        print(f"test_get_degree file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.get_degree("1433B_HUMAN"), 49)
        self.assertIsNotNone(self.file2.get_degree("1433B_HUMAN"))
        print(f"test_get_degree file2\033[92m passed \033[0m")
        self.assertRaises(ValueError, self.file1.get_degree, "G")
        print(f"test_get_degree error_file1\033[92m passed \033[0m")

    def test_get_max_degree(self):
        "Tests if the function get_max_degree return the right number and not None."
        self.assertEqual(self.file1.get_max_degree(), (('B', 'D'), 3))
        self.assertIsNotNone(self.file1.get_max_degree())
        print(f"test_get_max_degree file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.get_max_degree(), (('ATX1_HUMAN',), 207))
        self.assertIsNotNone(self.file2.get_max_degree())
        print(f"test_get_max_degree file2\033[92m passed \033[0m")

    def test_get_ave_degree(self):
        "Tests if the function ave_degree return the right number and not None."
        self.assertEqual(self.file1.get_ave_degree(), 2.0)
        self.assertIsNotNone(self.file1.get_ave_degree())
        print(f"test_get_ave_degree file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.get_ave_degree(), 5.6849)
        self.assertIsNotNone(self.file2.get_ave_degree())
        print(f"test_get_ave_degree file2\033[92m passed \033[0m")

    def test_count_degree(self):
        "Tests if count_degree() return the right number, not None and raise a ValueError."
        self.assertEqual(self.file1.count_degree(2), 2)
        self.assertIsNotNone(self.file1.count_degree(2))
        print(f"test_count_degree file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.count_degree(2), 1633)
        self.assertIsNotNone(self.file2.count_degree(2))
        print(f"test_count_degree file2\033[92m passed \033[0m")
        self.assertRaises(ValueError, self.file1.count_degree, -10)
        print(f"test_count_degree error_file1\033[92m passed \033[0m")

    @patch('builtins.print')
    def test_histogram_degree(self, mock_print):
        "Tests if histogram_degree() print the right thing and returns None."
        self.file1.histogram_degree(1, 1)
        mock_print.assert_called_with('1','**', sep = ' ')
        self.assertIsNone(self.file1.histogram_degree(1, 2))
        print(f"test_histogram_degree file1\033[92m passed \033[0m")
        self.file2.histogram_degree(9, 9)
        mock_print.assert_called_with('9',
                                      '*********************************************************************************************************************************************************************************************************************', sep = ' ')
        self.assertIsNone(self.file2.histogram_degree(9, 9))
        print(f"test_histogram_degree file1\033[92m passed \033[0m")

    def test_density(self):
        "Tests if the function test_density return the right number and not None."
        self.assertEqual(self.file1.density(), 0.4)
        self.assertIsNotNone(self.file1.density())
        print(f"test_density file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.density(), 0.0006)
        self.assertIsNotNone(self.file2.density())
        print(f"test_density file2\033[92m passed \033[0m")

    def test_clustering(self):
        "Tests if the function test_clustering return the right number and not None."
        self.assertEqual(self.file1.clustering("A"), 1.0)
        self.assertIsNotNone(self.file1.clustering("A"))
        print(f"test_clustering file1\033[92m passed \033[0m")
        self.assertEqual(self.file2.clustering("1433B_HUMAN",18), 0.027210884353741496)
        self.assertIsNotNone(self.file2.clustering("1433B_HUMAN"))
        print(f"test_clustering file2\033[92m passed \033[0m")

    def test_graph_er(self):
        "Tests if the function graph_er return correct list and not None."
        self.assertIsNotNone(self.file1.graph_er(0.3))
        self.assertTrue(isinstance(self.file1.graph_er(0.3), list))
        print(f"test_graph_er file1\033[92m passed \033[0m")

    def test_graph_ba(self):
        "Tests if the function graph_ba return correct list and not None."
        self.assertIsNotNone(self.file1.graph_ba(10))
        self.assertTrue(isinstance(self.file1.graph_ba(10), list))
        print(f"test_graph_ba file1\033[92m passed \033[0m")

    def test_find_cc(self):
        "Tests if the function find_cc return the right list and not None."
        self.assertEqual(self.file1.find_cc(), [['A', 'B', 'C', 'D', 'E', 'F']])
        self.assertIsNotNone(self.file1.find_cc())
        print(f"test_find_cc file1\033[92m passed \033[0m")
        self.assertEqual(self.file3.find_cc(), [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H']])
        self.assertIsNotNone(self.file3.find_cc())
        print(f"test_find_cc file3\033[92m passed \033[0m")

    def test_count_cc(self):
        "Tests if the function count_cc return the right int and not None."
        self.assertEqual(self.file1.count_cc(), 1)
        self.assertIsNotNone(self.file1.count_cc())
        print(f"test_count_cc file1\033[92m passed \033[0m")
        self.assertEqual(self.file3.count_cc(), 3)
        self.assertIsNotNone(self.file3.count_cc())
        print(f"test_count_cc file3\033[92m passed \033[0m")

    def test_write_cc(self):
        "Tests if the function write_cc return None."
        self.assertIsNone((self.file1).write_cc())
        print(f"test_write_cc file1\033[92m passed \033[0m")
        self.assertIsNone((self.file3).write_cc())
        print(f"test_write_cc file3\033[92m passed \033[0m")

    def test_extract_cc(self):
        "Tests if the function extract_cc return the right list and not None."
        self.assertEqual(self.file1.extract_cc("A"), ['A', 'B', 'C', 'D', 'E', 'F'])
        self.assertIsNotNone(self.file1.extract_cc("A"))
        print(f"test_extract_cc file1\033[92m passed \033[0m")
        self.assertEqual(self.file3.extract_cc("D"), ['D', 'E', 'F'])
        self.assertIsNotNone(self.file3.extract_cc("D"))
        print(f"test_extract_cc file3\033[92m passed \033[0m")

    def test_compute_cc(self):
        "Tests if the function extract_cc return the right list and not None."
        self.assertEqual(self.file1.compute_cc(), [1, 1, 1, 1, 1, 1])
        self.assertIsNotNone(self.file1.compute_cc())
        print(f"test_compute_cc file1\033[92m passed \033[0m")
        self.assertEqual(self.file3.compute_cc(), [1, 1, 1, 2, 2, 2, 3, 3])
        self.assertIsNotNone(self.file3.compute_cc())
        print(f"test_compute_cc file3\033[92m passed \033[0m")

if __name__ == '__main__':
    unittest.main()
