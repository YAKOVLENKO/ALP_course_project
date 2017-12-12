import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    gr_CommonFr = ''

    def __int__(self):
        pass

    def make_friendsGraph(self, common_friends):
        try:
            self.gr_CommonFr = nx.Graph()
            self.gr_CommonFr.add_weighted_edges_from(common_friends)
            pass
        except:
            pass

    def show_friendsGraph(self):
        try:
            pos = nx.spring_layout(self.gr_CommonFr, k=1)
            nx.draw_networkx_nodes(self.gr_CommonFr, pos, node_size=1500.0, vmax=3000.0)
            nx.draw_networkx_edges(self.gr_CommonFr, pos, width=1.0, edge_color='b')
            nx.draw_networkx_labels(self.gr_CommonFr, pos, font_size=5)
            plt.savefig('..\\Other')
            plt.show()
            '''plot = figure(title="Networkx Integration Demonstration", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
                          tools="", toolbar_location=None)
            graph = from_networkx(self.gr_CommonFr, nx.spring_layout, scale=2, center=(0, 0))
            plot.renderers.append(graph)
            show(plot)'''
        except:
            pass


    def make_groupGraph(self, fname, lname, personal_card):
        try:
            edges = []
            name = fname + ' ' + lname
            self.gr_CommonFr = nx.Graph()
            for i in range(0, len(personal_card)):
                edges.append([name, personal_card[i][0], personal_card[i][2]])
            self.gr_CommonFr.add_weighted_edges_from(edges)
        except: pass


    def show_groupGraph_common(self):
        try:
            edges = self.gr_CommonFr.edges
            weights = [self.gr_CommonFr[u][v]['weight']/10 for u, v in edges]
            pos = nx.spring_layout(self.gr_CommonFr, k=1)
            '''nx.draw_networkx_nodes(self.gr_CommonFr, pos, node_size=1500.0, vmax=3000.0)
            nx.draw_networkx_edges(self.gr_CommonFr, pos, width=1.0, edge_color='b')'''
            nx.draw_networkx_labels(self.gr_CommonFr, pos, font_size=5)
            nx.draw(self.gr_CommonFr, pos, edges=edges, edge_color='grey', width=weights, node_size=500)
            plt.show()
        except: pass

    def make_groupGraphSix(self, fname, lname, personal_card):
        try:
            edges = []
            name = fname + ' ' + lname
            self.gr_CommonFr = nx.Graph()
            for i in range(0, len(personal_card)):
                edges.append([name, personal_card[i][0], personal_card[i][1]])
            self.gr_CommonFr.add_weighted_edges_from(edges)
        except: pass
