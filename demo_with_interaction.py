from interactome import *

if __name__ == "__main__" :
    names = ["toy_example.txt", 
             "false_file_example-1.txt",  
             "false_file_example-2.txt",  
             "false_file_example-3.txt",  
             "toy_example_to_clean.txt",
             "toy_example_graph.txt",
             "toy_example_with_3_CC.txt"]
    interactomes = [Interactome(names[0]),
                    Interactome(names[1]),
                    Interactome(names[2]),
                    Interactome(names[3]),
                    Interactome(names[4]),
                    Interactome(names[5]),
                    Interactome(names[6])]
    Demo = ["DEMO OF OUR PYTHON PROJECT ABOUT BIOLOGICAL NETWORKS", #0
            "Presented by : Léa BEAULIEU and Enora CORLER",
            str("Lists of interactions of "+names[0]),
            interactomes[0].get_int_list(),
            str("Dictionnary of interactions of "+names[0]),
            interactomes[0].get_int_dict(),                         #5
            str("Matrix of interactions of "+names[0]),
            interactomes[0].get_mat(),
            str("Is "+names[0]+" an interaction file ?"),
            interactomes[0].is_interaction_file(),
            str("Is "+names[1]+" an interaction file ? (A file without a number of interactions)"),           #10
            interactomes[1].is_interaction_file(),
            str("Is "+names[2]+" an interaction file ? (An empty file)"),
            interactomes[2].is_interaction_file(),
            str("Is "+names[3]+" an interaction file ? (A file with a number of lines different than the number of interactions is a correct file) "),
            interactomes[3].is_interaction_file(),                  #15
            str("Proteins and matrix of interactions of "+names[0]),
            interactomes[0].read_interaction_file_mat(),
            str("Triplets of interactions of "+names[0]),
            interactomes[0].read_interaction_file(),
            str("Number of vertices of "+names[0]),                 #20
            interactomes[0].count_vertices(),                       
            str("Number of edges of "+names[0]),
            interactomes[0].count_edges(),
            str("List of interactions of "+names[4]+ " which needs to be cleaned up :"),
            interactomes[4].get_int_list(),                         #25
            str("List of interactions of "+ names[4]+ " which is now cleaned :"),
            Interactome("toy_example_cleaned.txt").get_int_list(),
            str("Number of degrees of the protein A in"+names[0]),
            interactomes[0].get_degree("A"),                        
            str("Maximum degree of "+names[0]),                     #30
            interactomes[0].get_max_degree(),
            str("Average degree of "+names[0]),                     
            interactomes[0].get_ave_degree(),
            str("Number of degrees that are equals to 2 in "+names[0]),
            interactomes[0].count_degree(2),                        #35
            str("Number of proteins that have degrees between 2 and 4 in "+names[0]),
            str("Density of "+names[0]),                           
            interactomes[0].density(),
            str("Local clustering coefficient of protein A in "+names[0]), 
            interactomes[0].clustering("A"),                                #40
            str("Erdos-Renyi random graph of "+names[5]+" with p=0.5"),
            str("Barabasi-Albert random graph of "+names[5]+" with m_max=10"),
            str("All connected nodes of "+names[5]),
            interactomes[6].find_CC(),
            str("Number of connected components of "+names[6]),             #45
            interactomes[6].count_CC(),
            str("Writing a file which contains the different connected components of the graph "+names[6]),
            str("Number of proteins in the same connected component than protein A in "+names[6]),
            interactomes[6].extract_CC("A"),
            str("List of all the proteins and their appartenances to a connected component for "+names[6]),
            interactomes[6].compute_CC()]
    for i in range(len(Demo)) :
        print(Demo[i]) 
        input()
        if i != 7 :
            if i == 36  :
                interactomes[0].histogram_degree(2,4)
                input()
            elif i == 41 :
                erdos_renyi = interactomes[6].graph_ER(0.5)
                print(erdos_renyi)
                input()
                ax = plt.gca()
                ax.set_title('Erdos-Renyi random graph with p=0.5')
                nx.draw(erdos_renyi,  node_color="green", ax=ax)
                plt.show()
                input()
            elif i == 42:
                barabasi_albert = interactomes[6].graph_BA(10)
                print(barabasi_albert)
                input()
                ax = plt.gca()
                ax.set_title('Barabasi-Albert random graph with m_max=10')
                nx.draw(barabasi_albert, node_color="red")
                plt.show()
                input()
            elif i == 26 :
                interactomes[4].clean_interactome("toy_example_cleaned.txt")
            elif i == 47:
                interactomes[6].write_CC()
                with open("connected_components.txt", "r", encoding="utf-8") as file_reader:
                    for line in file_reader :
                        print(line)