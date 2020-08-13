from graph import Graph
from util import Queue
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for nums in ancestors:
        g.add_vertex(nums[0])

    for nums in ancestors:
        g.add_vertex(nums[1])
    
    for nums in ancestors:
        g.add_edge(nums[1],nums[0])
    print(g.vertices)
    path = g.dft(starting_node)

    return path[-1][-1]

print(earliest_ancestor(test_ancestors,6),"last ancestor")