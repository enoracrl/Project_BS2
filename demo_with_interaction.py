'''
Demo of our methods from the object Interactome for some files examples.

Usage: Visualization and manipulation of graphs
'''

__authors__ = ("Enora CORLER", "Léa BEAULIEU")
__contact__ = ("enora.corler@etudiant.univ-rennes1.fr", "lea.beaulieu@etudiant.univ-rennes1.fr")
__date__ = "25/11/2022"

'''
Importation of necessary modules :
    - networkx : allows to use matplolib module ;
    - matplotlib.pyplot : allows to visualize graphs ;
    - interactome : give us access to all methods from the object Interactome of the module
'''
import networkx as nx
import matplotlib.pyplot as plt
from interactome import Interactome

if __name__ == "__main__" :
    file = "Examples/toy_example_with_3_CC.txt"
    interactome = Interactome(file)
    Demo = ["DEMO OF OUR PYTHON PROJECT ABOUT BIOLOGICAL NETWORKS",
            "Presented by : Léa BEAULIEU and Enora CORLER",
            "Lists of interactions :",
            interactome.get_int_list(),
            "Dictionnary of interactions :",
            interactome.get_int_dict(),
            "Matrix of interactions :",
            interactome.get_mat(),
            "Proteins and matrix of interactions :",
            interactome.read_interaction_file_mat(),
            "Triplets of interactions :",
            interactome.read_interaction_file(),
            "Number of vertices :",
            interactome.count_vertices(),
            "Number of edges ",
            interactome.count_edges(),
            "Number of degrees of the protein A :",
            interactome.get_degree("A"),
            "Maximum degree :",
            interactome.get_max_degree(),
            "Average degree of :",
            interactome.get_ave_degree(),
            "Number of degrees that are equals to 2 :",
            interactome.count_degree(2),
            "Number of proteins that have degrees between 2 and 4 :",
            "Density :",
            interactome.density(),
            "Local clustering coefficient of protein A :",
            interactome.clustering("A"),
            "Erdos-Renyi random graph with p=0.5 :",
            "Barabasi-Albert random graph with m_max=10 :",
            "All connected nodes :",
            interactome.find_cc(),
            "Number of connected components :",
            interactome.count_cc(),
            "Writing a file which contains the different connected components of the graph :",
            "Number of proteins in the same connected component than protein A : ",
            interactome.extract_cc("A"),
            "List of all the proteins and their appartenance to a connected component :",
            interactome.compute_cc()]
    for i in range(len(Demo)) :
        print(Demo[i], sep="\n")
        if i != 7 :
            if Demo[i] == "Number of proteins that have degrees between 2 and 4 :" :
                interactome.histogram_degree(2,4)
            elif Demo[i] == "Erdos-Renyi random graph with p=0.5 :":
                erdos_renyi = nx.Graph(interactome.graph_er(0.5))
                print(erdos_renyi)
                ax = plt.gca()
                ax.set_title('Erdos-Renyi random graph with p=0.5')
                nx.draw(erdos_renyi, node_color="green", ax=ax)
                plt.show()
            elif Demo[i] == "Barabasi-Albert random graph with m_max=10 :":
                barabasi_albert = nx.Graph(interactome.graph_ba(10))
                print(barabasi_albert)
                ax = plt.gca()
                ax.set_title('Barabasi-Albert random graph with m_max=10')
                nx.draw(barabasi_albert, node_color="red")
                plt.show()
            elif Demo[i] == "Writing a file containing the different CC of the graph :":
                interactome.write_cc()
                with open("Examples/toy_example_with_3_cc_cc.txt", "r",
                        encoding="utf-8") as file_reader:
                    for line in file_reader :
                        print(line)
        print("\n")
