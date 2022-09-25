import pytest
import numpy as np

file_test = "/Users/Enora/Desktop/COURS/M2/S1/BS2/TP/toy_example.txt"

script = pytest.importorskip("TP")

def test_read_interaction_file_dict():
    '''Fonction structure 1 : la fonction doit retourner le graphe d'interaction sous forme d'un dictionnaire'''
    assert script.read_interaction_file_dict(file_test) == {'A': ['B', 'C'], 
                                                            'B': ['A', 'C', 'D'], 
                                                            'C': ['A', 'B'], 
                                                            'D': ['B', 'E', 'F'], 
                                                            'E': ['D'], 
                                                            'F': ['D']}
    
def test_read_interaction_file_list():
    '''Fonction structure 2 : la fonction doit retourner le graphe d'interaction sous forme d'une liste de couples'''
    assert script.read_interaction_file_list(file_test) == [('A', 'B'), 
                                                            ('A', 'C'), 
                                                            ('B', 'C'), 
                                                            ('B', 'D'), 
                                                            ('D', 'E'), 
                                                            ('D', 'F')]    

def test_read_interaction_file_mat():
    '''Fonction structure 3 : la fonction doit retourner le graphe d'interaction sous forme d'une matrice d'adjacence'''
    assert script.read_interaction_file_mat(file_test) == (['A', 'B', 'C', 'D', 'E', 'F'], 
                                                           np.array([[0, 1, 1, 0, 0, 0], 
                                                                     [1, 0, 1, 1, 0, 0], 
                                                                     [1, 1, 0, 0, 0, 0], 
                                                                     [0, 1, 0, 0, 1, 1], 
                                                                     [0, 0, 0, 1, 0, 0], 
                                                                     [0, 0, 0, 1, 0, 0]],dtype=object).all())
                                                           
                                                           
