import networkx as nx
import matplotlib.pyplot as plt
import numpy
import numpy as np
import pylab

class Graph:

    gr_CommonFr = ''
    gr_Group = ''
    gr_GroupSix = ''
    friends = []
    last_add = ''

    def __init__(self,pers_obj, api, token):
        self.pers_obj = pers_obj
        self.api = api
        self.token = token
        pass

    def onClick(self,event):
       # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              #('double' if event.dblclick else 'single', event.button,
               #event.x, event.y, event.xdata, event.ydata))

        counter = 0
        for key, value in self.pos.items():
            if ((event.xdata-value[0])**2 + (event.ydata-value[1])**2) < 0.004:
                print(self.friends[counter],((event.xdata-value[0])**2 + (event.ydata-value[1])**2))
                friends_list = self.pers_obj.get_commonFriends(self.api, self.token,id=self.friends[counter])

                self.gr_CommonFr.clear()
                for x in range(len(friends_list[0])):
                    friends_list[0][x][0] = key

                self.last_add[0] = self.last_add[0] + friends_list[0]#[:10]
                self.last_add[1] = self.last_add[1] + friends_list[1]

                #print(friends_list[0])
                #print(friends_list[1])

                self.gr_CommonFr.clear()
                plt.gcf().clear()
                plt.gcf()
                plt.close()
                for x in self.last_add[0]:
                    self.gr_CommonFr.add_node(x[0])
                    self.gr_CommonFr.add_node(x[1])
                    self.gr_CommonFr.add_edge(x[0], x[1])

                self.pos = nx.spring_layout(self.gr_CommonFr)
                nx.draw_networkx_nodes(self.gr_CommonFr, self.pos, node_size=1500.0, vmax=3000.0)
                nx.draw_networkx_edges(self.gr_CommonFr, self.pos, width=1.0, edge_color='b')
                nx.draw_networkx_labels(self.gr_CommonFr, self.pos, font_size=5)

                fig = plt.gcf()
                #print(fig)
                fig.canvas.mpl_connect('button_press_event', self.onClick)

                #print(self.gr_CommonFr.node_dict_factory())
                plt.show()

                return 0
            counter+=1

    def make_friendsGraph(self, common_friends):
        try:
            self.friends = common_friends[1]
            self.gr_CommonFr = nx.Graph()
            self.last_add = common_friends
            self.gr_CommonFr.add_weighted_edges_from(common_friends[0])
            pass
        except:
            pass

    def show_friendsGraph(self):
        try:
            self.pos = nx.spring_layout(self.gr_CommonFr, k=1)
            nx.draw_networkx_nodes(self.gr_CommonFr, self.pos, node_size=1500.0, vmax=3000.0)
            nx.draw_networkx_edges(self.gr_CommonFr, self.pos, width=1.0, edge_color='b')
            nx.draw_networkx_labels(self.gr_CommonFr, self.pos, font_size=5)

            fig = plt.gcf()
            print(fig)
            fig.canvas.mpl_connect('button_press_event', self.onClick)

            print(self.gr_CommonFr.node_dict_factory())
            plt.show()
        except:
            pass


    def make_groupGraph(self, fname, lname, personal_card):
        try:
            edges = []
            name = fname + ' ' + lname
            self.gr_Group = nx.Graph()
            for i in range(0, len(personal_card)):
                edges.append([name, personal_card[i][0], personal_card[i][2]])
            self.gr_Group.add_weighted_edges_from(edges)
        except: pass


    def show_groupGraph(self):
        try:
            edges = self.gr_Group.edges
            weights = [self.gr_Group[u][v]['weight']/10 for u, v in edges]
            pos = nx.spring_layout(self.gr_Group, k=1)
            nx.draw_networkx_labels(self.gr_Group, pos, font_size=5)
            nx.draw(self.gr_Group, pos, edges=edges, edge_color='grey', width=weights, node_size=500)
            plt.show()
        except: pass

    def show_groupGraphSix(self):
        try:
            edges = self.gr_GroupSix.edges
            weights = [self.gr_GroupSix[u][v]['weight']/10 for u, v in edges]
            pos = nx.spring_layout(self.gr_GroupSix, k=1)
            nx.draw_networkx_labels(self.gr_GroupSix, pos, font_size=5)
            nx.draw(self.gr_GroupSix, pos, edges=edges, edge_color='grey', width=weights, node_size=500)
            plt.show()
        except: pass

    def make_groupGraphSix(self, fname, lname, personal_card):
        try:
            edges = []
            name = fname + ' ' + lname
            self.gr_GroupSix = nx.Graph()
            for i in range(0, len(personal_card)):
                edges.append([name, personal_card[i][0], personal_card[i][1]])
            self.gr_GroupSix.add_weighted_edges_from(edges)
        except: pass
