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
      
      print("\n","DEMO OF OUR PYTHON PROJECT ABOUT BIOLOGICAL NETWORKS", "\n")
      input()
      print("Presented by : Léa BEAULIEU and Enora CORLER", "\n")
      input()
      print("* CHAPTER 1 : READING A INTERACTIONS GRAPH BETWEEN PROTEINS *", "\n")
      input()
      print("Lists of interactions of :")
      input()
      print("toy_example : ", interactome1.get_int_list(), "\n",
            "Human_HighQuality (beginning) :", interactome2.get_int_list()[:4], 
            sep="\n", end="\n")
      input()
      
      print("\n", "Dictionnary of interactions of :")
      input()
      print("toy_example : ", interactome1.get_int_dict(), "\n",
            "Human_HighQuality (1433B_HUMAN) :", list(interactome2.get_int_dict().items())[0],
            sep="\n", end="\n")
      input()

      print("\n", "Matrix of interactions of :")
      input()
      print("toy_example : ", interactome1.get_mat(), "\n",
            "Human_HighQuality (beginning) :", interactome2.get_mat(), 
            sep="\n", end="\n")    
      input()

      print("\n", "Is this file correct ? :")
      input()
      print("toy_example : ", interactome1.is_interaction_file(), "\n",
            "Human_HighQuality :", interactome2.is_interaction_file(), "\n",
            "A file without a number of interactions :", false_interactome_1.is_interaction_file(), "\n",
            "An empty file :", false_interactome_2.is_interaction_file(), "\n",
            "A file with a number of lines different than the number of interactions is a correct file :", false_interactome_3.is_interaction_file(),
            #"A file with a wrong number of columns is a correct file :", false_interactome_4.is_interaction_file(),
            sep="\n", end="\n")
      input()
      
      print("\n", "Lists of proteins and the matrix of interactions of :")
      input()
      print("toy_example : ", interactome1.read_interaction_file_mat(), "\n",
            "Human_HighQuality :", (interactome2.read_interaction_file_mat()[0][:10],interactome2.read_interaction_file_mat()[1]), 
            sep="\n", end="\n")
      input()
      
      print("\n", "Triplets of the dictionnary, list and the matrix of interactions of ... :")
      input()
      print("toy_example : ", interactome1.read_interaction_file(), 
            #"Triplets of the dictionnary, list and the matrix of interactions of Human_HighQuality : ", interactome1.read_interaction_file()(0), 
            end='\n')
      input()
      
      print("\n","* CHAPTER 2 : EXPLORATION OF AN INTERACTIONS GRAPH BETWEEN PROTEINS *", "\n")
      input()
      
      print("Number of vertices of :")
      input()
      print("toy_example : ", interactome1.count_vertices(), "\n", 
            "Human_HighQuality : ", interactome2.count_vertices(), 
            end='\n')
      input()
      
      print("Number of edges of ... :")
      input()
      print("toy_example : ", interactome1.count_edges(), "\n",
            "Human_HighQuality : ", interactome2.count_edges(), 
            end='\n')
      input()
      
      print("Cleaning up file :")
      input()
      print("Interactions of a file which needs to be cleaned up :", interactome_to_clean.get_int_list())
      print("Interactions of the cleaned up file :")
      interactome_to_clean.clean_interactome(file_cleaned)
      interactome_cleaned = Interactome("toy_example_cleaned.txt")
      print(interactome_cleaned.get_int_list(), end="\n")
      input()
      
      print("Degrees of the protein ... :")
      input()
      print("A in toy_example : ", interactome1.get_degree("A"), "\n",
            "1433B_HUMAN in Human_HighQuality : ", interactome2.get_degree("1433B_HUMAN"), 
            end="\n")
      input()
      
      print("Maximum degree of ... :")
      input()
      print("toy_example : ", interactome1.get_max_degree(), "\n",
            "Human_HighQuality : ", interactome2.get_max_degree(), 
            end="\n")
      input()
      
      print("Average degree of ... :")
      input()
      print("toy_example : ", interactome1.get_ave_degree(), "\n",
            "Human_HighQuality : ", interactome2.get_ave_degree(), end="\n")
      input()
      
      print("Number of proteins that have the same degree as ... :")
      input()
      print("2 in toy_example : ", interactome1.count_degree(2), "\n",
            "20 in Human_HighQuality : ", interactome2.count_degree(20),
            end="\n")
      input()
      
      print("Representation of the number of proteins that have a degree between ... :")
      input()
      print("2 and 4 in toy_example : ", interactome1.histogram_degree(2, 4), "\n",
            "10 and 20 in Human_HighQuality : ", interactome2.histogram_degree(10,20), 
            end="\n")
      input()
      
      print("* CHAPTER 3 : MODIFICATIONS OF SPECIFICATIONS, OOP *")
      input()
      
      print("\n", "Density of ... :")
      input()
      print("toy_example :", interactome1.density(), "\n",
            "Human_HighQuality :", interactome2.density(), 
            end="\n" )
      input()
      
      print("\n", "Local clustering coefficient of the protein ... :")
      input()
      print("A in toy_example :", interactome1.clustering("A"), "\n",
            "1433B_HUMAN in Human_HighQuality :", interactome2.clustering("1433B_HUMAN"), 
            end="\n" )
      input()
      
      print("\n","* CHAPTER 4 : RANDOM GRAPHS *", "\n")
      input()
      erdos_renyi = interactome1.graph_ER(0.5)
      print(erdos_renyi)
      input()
      ax = plt.gca()
      ax.set_title('Erdos-Renyi random graph with p=0.5')
      nx.draw(erdos_renyi,  node_color="green", ax=ax)
      plt.show()
      barabasi_albert = interactome1.graph_BA(12)
      print(barabasi_albert)
      input()
      ax = plt.gca()
      ax.set_title('Barabasi-Albert random graph with m_max=12')
      nx.draw(barabasi_albert, node_color="red")
      plt.show()
      
      print("\n","* CHAPTER 5 : CALCULATION OF THE CONNECTED COMPONENTS OF A PROTEIN INTERACTION GRAPH *", "\n")
      input()
      
      print("interactome_CC is a interactome based on toy_example with", len(interactome_CC.get_int_dict()), "nodes", sep=' ', end="\n")
      input()
      
      print("How many connected components are in this graph ?")
      input()
      print(interactome_CC.count_CC(), " nodes", end="\n")
      input()
      
      print("Writing a file which contains the different connected components of a given graph :")
      input()
      interactome_CC.write_CC()
      with open("connected_components.txt", "r", encoding="utf-8") as file_reader:
            for line in file_reader :
                  print(line)
      input()
      
      print("\n", "All the vertices of the same connected component as ... :")
      input()
      print("protein A :", interactome_CC.extract_CC("A"), "\n", 
            "protein D :", interactome_CC.extract_CC("D"), "\n", 
            "protein H :", interactome_CC.extract_CC("H"), 
            end="\n")
      input()
      print("Number of connected components for interactome_CC :", interactome_CC.compute_CC())
      
      input()
      
      
      

      
