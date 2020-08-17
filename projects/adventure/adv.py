from room import Room
from player import Player
from world import World
from util import Queue,Stack
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
opposite = {
    "n":"s",
    "s":"n",
    "e":"w",
    "w":"e"
}
traversal_graph = {player.current_room.id: {d:"?" for d in player.current_room.get_exits()}}
# Takes in a room by id and returns a list of all possible directions
def exits (room):
    directions = []
    for d in traversal_graph[room]:
        if traversal_graph[room][d] == "?":
            directions.append(d)
    return directions
# Returns possible directions in a list
# ends on a dead end
def traversal (room):
    # room.get_exits() returns [directions[n]..] 
    while len(exits(room)) > 0:
        random_direction = random.choice(exits(room))
        previous = player.current_room.id
        player.travel(random_direction)
        current = player.current_room.id
        traversal_path.append(random_direction)
        if current not in traversal_graph:
            traversal_graph[current] = {d: "?" for d in player.current_room.get_exits()}

        traversal_graph[current][opposite[random_direction]] = previous
        traversal_graph[previous][random_direction] = current
        room = current

def search_nearest (room):
    q = Queue()
    q.enqueue(room)
    visited = set()

    while q.size() > 0:
        node=q.dequeue()

        if node not in visited:
            visited.add(node)
            if len(exits(node)) >  0:
                return node
            for room in list(traversal_graph[node].values()):
                q.enqueue(room)

def back_track(room,target):
    q = Queue()
    q.enqueue([room])
    visited = set()
    something = []
    while q.size() > 0:
        node  = q.dequeue()

        if node[-1] not in visited:
            visited.add(node[-1])
            if node[-1] == target:
                something = node
                break
            for room in list(traversal_graph[node[-1]].values()):
                path_copy = list(node) + [room]
                q.enqueue(path_copy)
    final = []
    for i in range(len(something)-1):
        for direction in traversal_graph[something[i]]:
            if traversal_graph[something[i]][direction] == something[i+1]:
                final.append(direction)
    return final


while len(traversal_graph) != len(room_graph):
    traversal(player.current_room.id)
    near_target = search_nearest(player.current_room.id)
    path  = back_track(player.current_room.id,near_target)
    for directions in path:
        player.travel(directions)
        traversal_path.append(directions)
# print (player.current_room.id)        
# traversal(player.current_room.id)
# print (player.current_room.id)
# target=search_nearest(player.current_room.id)
# print (back_track(player.current_room.id,target))
# print (player.current_room.id)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
