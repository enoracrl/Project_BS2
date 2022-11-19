from interactome import *

'''
Testing files
'''

file_test_1 = "toy_example.txt"         # simple file with only 6 interactions between letters
file_test_2 = "Human_HighQuality.txt"   # complex file with 27276 interactions
file_test_3 = "/Users/Enora/Downloads/ex.txt"
file_test_4 = "/Users/Enora/Downloads/ex2.txt"

false_file_1 = "false_file_example-1.txt"   # file without the number of interactions on the first line
false_file_2 = "false_file_example-2.txt"   # empty file
false_file_3 = "false_file_example-3.txt"   # file with a number of lines =/= number of interactions
false_file_4 = "false_file_example-4.txt"   # file with a wrong number of columns

file_to_clean = "toy_example_to_clean.txt"
file_cleaned = "toy_example_cleaned.txt"

file_CC = "toy_example_with_3_CC.txt"

if __name__ == "__main__" :
    interactome1 = Interactome(file_test_1)   # objet de la classe Interactome
    interactome2 = Interactome(file_test_2)
    false_interactome_1 = Interactome(false_file_1)
    false_interactome_2 = Interactome(false_file_2)
    false_interactome_3 = Interactome(false_file_3)
    interactome_to_clean = Interactome(file_to_clean)
    interactome_CC = Interactome(file_CC)
    #false_interactome_4 = Interactome(false_file_4)
    print("List of interactions of toy_example : ", interactome1.get_int_list(), 
          "List of interactions of Human_HighQuality (beginning) :", interactome2.get_int_list()[:4], 
          sep="\n")
    print('\n')
    print("Dictionnary of interactions of toy_example : ", interactome1.get_int_dict(), 
          "Dictionnary of interactions of Human_HighQuality (1433B_HUMAN) :", list(interactome2.get_int_dict().items())[0],
          sep="\n")
    print('\n')
    print("Matrix of interactions of toy_example : ", interactome1.get_mat(), 
          "Matrix of interactions of Human_HighQuality (beginning) :", interactome2.get_mat(), 
          sep="\n")
    print('\n')
    print("Toy_example is a correct file : ", interactome1.is_interaction_file(), 
          "Human_HighQuality is a correct file :", interactome2.is_interaction_file(), 
          "A file without a number of interactions is a correct file :", false_interactome_1.is_interaction_file(), 
          "An empty file is a correct file :", false_interactome_2.is_interaction_file(), 
          "A file with a number of lines different than the number of interactions is a correct file :", false_interactome_3.is_interaction_file(), 
          #"A file with a wrong number of columns is a correct file :", false_interactome_4.is_interaction_file(), 
          sep="\n")
    print('\n')
    print("List of proteins and the matrix of interactions of toy_example : ", interactome1.read_interaction_file_mat(), 
          "List of proteins and the matrix of interactions of Human_HighQuality :", (interactome2.read_interaction_file_mat()[0][:10],interactome2.read_interaction_file_mat()[1]), 
          sep="\n")
    print('\n')
    print("Triplets of the dictionnary, list and the matrix of interactions of toy_example : ", interactome1.read_interaction_file(), 
          #"Triplets of the dictionnary, list and the matrix of interactions of Human_HighQuality : ", interactome1.read_interaction_file()(0), 
          sep="\n")
    print('\n')
    print("Number of vertices of toy_example : ", interactome1.count_vertices(), 
          "Number of vertices of Human_HighQuality : ", interactome2.count_vertices(), 
          sep="\n")
    print('\n')
    print("Number of edges of toy_example : ", interactome1.count_edges(), 
          "Number of edges of Human_HighQuality : ", interactome2.count_edges(), 
          sep="\n")
    print('\n')
    print("Interactions of a file which needs to be cleaned up :", interactome_to_clean.get_int_list(), sep="\n")
    print("Interactions of the cleaned up file :")
    interactome_to_clean.clean_interactome(file_cleaned)
    interactome_cleaned = Interactome("toy_example_cleaned.txt")
    print(interactome_cleaned.get_int_list())
    print('\n')
    print("Degrees of the protein A toy_example : ", interactome1.get_degree("A"), 
          "Degrees of the protein 1433B_HUMAN Human_HighQuality : ", interactome2.get_degree("1433B_HUMAN"), 
          sep="\n")
    print('\n')
    print("Maximum degree of toy_example : ", interactome1.get_max_degree(), 
          "Maximum degree of Human_HighQuality : ", interactome2.get_max_degree(), 
          sep="\n")
    print('\n')
    print("Average degree of toy_example : ", interactome1.get_ave_degree(), 
          "Average degree of Human_HighQuality : ", interactome2.get_ave_degree(), 
          sep="\n")
    print('\n')
    print("Number of proteins that have the same degree as 2 in toy_example : ", interactome1.count_degree(2), 
          "Number of proteins that have the same degree as 20 in Human_HighQuality : ", interactome2.count_degree(20), 
          sep="\n")
    print('\n')
    print("Number of proteins that have a degree between 2 and 4 in toy_example : ")
    interactome1.histogram_degree(2, 4)
    print("Number of proteins that have a degree between 10 and 20 in Human_HighQuality : ")
    interactome2.histogram_degree(10,20)
    print('\n')
    print("Density of toy_example :", interactome1.density(), 
          "Density of Human_HighQuality :", interactome2.density(), 
          sep="\n" )
    print('\n')
    print("Local clustering coefficient of the protein A toy_example :", interactome1.clustering("A"), 
          "Local clustering coefficient of the protein 1433B_HUMAN of Human_HighQuality :", interactome2.clustering("1433B_HUMAN"), 
          sep="\n" )
    print("test :", interactome_CC.find_CC())
    print("test :", interactome_CC.count_CC())
    print("test :", interactome_CC.write_CC())
    print("test :", interactome_CC.extract_CC("A"))
    print("test :", interactome_CC.extract_CC("D"))
    print("test :", interactome_CC.extract_CC("H"))
    print("test :", interactome_CC.compute_CC())
    
    
    

    
