
# import libraries for time counter, memory consumption and setting the recursion limit
import sys
import time
import os
import psutil

sys.setrecursionlimit(30000)        # Set the recursion limit to 30000


class Node:             # class Node to create objects
    def __init__(self, state = None, parent = None, move = None, g_n = None, h_n = None, f_n = None):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_n = g_n
        self.h_n = h_n
        self.f_n = f_n
  
 
# Initialize all lists and variables     
#goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
two_d_index = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
stack = []
visited = []
moves = []
mini, fn, goal_flag, expanded = 0, 0, 0, 0
movesp = ''

       
def main():
    ip = input("Enter the input state:")        # Take the user input for the initial state
    root_state = list(map(int, ip.split()))
    root = Node(root_state, None, None, 0, None, None)      # Create root object and calculate h(n)
    root.h_n = manhattan_distance(root.state)
    root.f_n = root.g_n + root.h_n
    idastar(root)
    
    
def idastar(root):
    global stack, mini, fn, goal_flag, expanded
    start = time.time()
    threshold = root.f_n
    while True:
        mini = 99999            # Initialize minimum to the MAX value
        # Clear the stack and visited lists
        stack.clear()
        visited.clear()
        thrs, goal_flag = search(root, threshold)       # Pass the root node to the search function
        expanded += len(visited)        # Increment the number of expanded nodes
        if goal_flag == 1:      # Print output if goal is found
            print("Goal Found!")
            print("Solution for Manhattan Heuristic of Iterative deepening for A-Star")
            print("Moves: ", movesp)
            print("Number of Nodes expanded: ", expanded)
            end = time.time()
            print("Time Taken:", end - start, "seconds")
            process = psutil.Process(os.getpid())
            print("Memory Used:", process.memory_info().rss / 1000, "kb\n\n")
            break
        threshold = thrs            # Update the threshold


def search(cur_node, threshold):
    global mini, movesp
    sib_list = []       # Initialize the sibling nodes list
    if cur_node.state == goal:      # Append moves if goal is found 
        moves.append(cur_node.move)
        parent = cur_node.parent
        while parent != None:
            for node in visited:
                if node.state == parent:
                    moves.append(node.move)
                    parent = node.parent
        del moves[len(moves)-1]
        movesp = ''.join(moves[::-1])
        return cur_node.f_n, 1
    elif cur_node.f_n > threshold:      # Return the f(n) of frontier node if it is greater than the threshold
        return cur_node.f_n, 0
    visited.append(cur_node)            # Append the current node to the visited list
    i = cur_node.state.index(0)         # Take the index of occurrence of '0'
    if i not in {0, 3, 6}:  # skips if 0 is already on extreme left
        t_node = left(cur_node, i)
        flag = 0
        for each in visited:
            if t_node.state == each.state:
                flag = 1
                break
            else:
                continue
        if flag != 1:
            sib_list.append(t_node)
    if i not in {2, 5, 8}:  # skips if 0 is already on extreme right
        t_node = right(cur_node, i)
        flag = 0
        for each in visited:
            if t_node.state == each.state:
                flag = 1
                break
            else:
                continue
        if flag != 1:
            sib_list.append(t_node)
    if i not in {0, 1, 2}:  # skips if 0 is already on extreme top
        t_node = up(cur_node, i)
        flag = 0
        for each in visited:
            if t_node.state == each.state:
                flag = 1
                break
            else:
                continue
        if flag != 1:
            sib_list.append(t_node)
    if i not in {6, 7, 8}:  # skips if 0 is already on extreme bottom
        t_node = down(cur_node, i)
        flag = 0
        for each in visited:
            if t_node.state == each.state:
                flag = 1
                break
            else:
                continue
        if flag != 1:
            sib_list.append(t_node)
    sib_list.reverse()
    for node in sib_list:
        stack.append(node)    
    while stack:        # Calls search function for child nodes while stack is not empty
        temp_node = stack.pop()
        fn, goal_flag = search(temp_node, threshold)
        if goal_flag == 1:
            return fn, goal_flag
        if fn < mini:
            mini = fn
    return mini, 0
    
    
def left(cur_node, i):   # performs left-shift operation
    child_node = Node()
    child_node.parent = cur_node.state[:]
    child_node.state = cur_node.state[:]
    child_node.state[i-1], child_node.state[i] = child_node.state[i], child_node.state[i-1]
    child_node.move = 'L'
    child_node.g_n = cur_node.g_n + 1
    child_node.h_n = manhattan_distance(child_node.state)
    child_node.f_n = child_node.g_n + child_node.h_n
    return child_node
    
    
def right(cur_node, i):   # performs right-shift operation
    child_node = Node()
    child_node.parent = cur_node.state[:]
    child_node.state = cur_node.state[:]
    child_node.state[i+1], child_node.state[i] = child_node.state[i], child_node.state[i+1]
    child_node.move = 'R'
    child_node.g_n = cur_node.g_n + 1
    child_node.h_n = manhattan_distance(child_node.state)
    child_node.f_n = child_node.g_n + child_node.h_n
    return child_node
    
    
def up(cur_node, i):   # performs up-shift operation
    child_node = Node()
    child_node.parent = cur_node.state[:]
    child_node.state = cur_node.state[:]
    child_node.state[i-3], child_node.state[i] = child_node.state[i], child_node.state[i-3]
    child_node.move = 'U'
    child_node.g_n = cur_node.g_n + 1
    child_node.h_n = manhattan_distance(child_node.state)
    child_node.f_n = child_node.g_n + child_node.h_n
    return child_node
    
    
def down(cur_node, i):   # performs down-shift operation
    child_node = Node()
    child_node.parent = cur_node.state[:]
    child_node.state = cur_node.state[:]
    child_node.state[i+3], child_node.state[i] = child_node.state[i], child_node.state[i+3]
    child_node.move = 'D'
    child_node.g_n = cur_node.g_n + 1
    child_node.h_n = manhattan_distance(child_node.state)
    child_node.f_n = child_node.g_n + child_node.h_n
    return child_node
    
    
def manhattan_distance(cur_state):  # returns the manhattan distance
    man_dist = 0
    for x in cur_state:
        if x == 0:
            continue
        i = cur_state.index(x)
        j = goal.index(x)
        temp_row = abs(two_d_index[i][0] - two_d_index[j][0])
        temp_col = abs(two_d_index[i][1] - two_d_index[j][1])
        man_dist = man_dist + temp_row + temp_col
    return man_dist


if __name__=="__main__": main()