# python3
#Leons Jūlijs Strupītis 13. gr. Apl. nr. 221RDB402

import sys
import threading
import numpy as np


def compute_height(n, parents):
    # Tukša koka izveide, masīvs
    nodes = [[] for _ in range(n)]
    # Saknes atrašana
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            # Mezgla pievienošana vecākam
            nodes[parent].append(i)
    # Maksimālā koka dziļuma atrašana
    max_height = dfs_height(nodes, root)
    return max_height

def dfs_height(nodes, root):
    # Ja mezglam nav pēctaču atgriež 1 
    if not nodes[root]:
        return 1
    # Maksimālā dziļuma atrašana starp mezgla pēctačiem
    max_child_height = 0
    for child in nodes[root]:
        child_height = dfs_height(nodes, child)
        if child_height > max_child_height:
            max_child_height = child_height
    return max_child_height + 1


def main():
    # Ievades lasīšana
    text = input()
    if "a" not in text:
        if "I\r" in text:
            n = int(input())
            parents = np.fromstring(input(), dtype=int, sep=' ')
            # Koka dziļuma aprēķināšana
            max_height = compute_height(n, parents)
    
            #Rezultāta izvade
            print(max_height)
        if "F\r" in text:
            text = "test/" + input()
            with open(text, 'r') as f:
                n = int(f.readline().strip())
                parents = np.fromstring(f.readline().strip(), dtype=int, sep=' ')
                # Koka dziļuma aprēķināšana
                max_height = compute_height(n, parents)
    
                #Rezultāta izvade
                print(max_height)
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
