import os
from random import randint
from maze import Maze
import algorithms as a
import time
from interface import Interface
import interface
from heuristics import manhattan_distance, euclidean_distance

# List of block positions to make a random boards
b5x5 = [[],[(0,2),(0,3),(2,4)],[(0,0),(0,1),(2,2),(3,2)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0)],[(0,0),(0,1),(2,2)]]
b6x6 = [[],[(0,0),(1,0),(2,0)],[(1,5),(3,1),(3,2)],[(4,1),(5,1),(1,3)],[(0,4)],[(2,2),(3,4),(3,5)],[(3,1),(4,3),(4,4)],[(2,0),(2,1),(1,3),(2,3),(3,3)],[(0,0),(1,0),(2,0)]]
b7x7 = [[(0,3),(1,1)],[(5,3),(3,3),(3,4),(6,1)],[(2,0),(2,1),(4,0),(4,1)],[(2,0),(3,0),(3,2),(4,2)],[(2,5),(3,3),(6,5),(6,6)],[(0,0),(0,2),(0,4)],[(4,4),(4,5),(6,6)]]

def main() -> None:
    """Play maze"""

    game_mode = select_game_mode()
    game_size = int(input("Escolha o Size Board:\n 1: 5x5 \n 2: 6x6 \n 3: 7x7 \n"))

    if game_size == 1: 
        rows,columns=5,5
        block_positions = [(0,0),(0,1),(2,2),(3,2)] # b5x5[randint(0,len(b5x5)-1)]
    elif game_size == 2: 
        rows,columns=6,6
        block_positions = b6x6[randint(0,len(b6x6)-1)]
    elif game_size == 3:
        rows,columns=7,7
        block_positions = b7x7[randint(0,len(b7x7)-1)]

    maze = create_game(rows, columns, block_positions)
    maze = solve_maze(game_mode, maze)
    interface.create_interface(maze, rows, columns)


def create_game(rows, columns, block_positions) -> Maze:
    """Create initial board maze"""
    return Maze(rows, columns, block_positions)

def select_game_mode() -> int:
    """Print interface to choose game mode"""
    game_modes = {1: "BFS", 2: "DFS", 3: "Iterative DFS", 4: "Greedy" , 5: "A*", 6: "Weighted A*"}
    while True:
        os.system('clear')
        print("\nEscolha um modo de resolução:")
        for mode, description in game_modes.items():
            print(f"{mode} - {description}")
        game_mode = int(input("\nDigite o número correspondente ao modo desejado: "))
        if game_mode in game_modes: 
            return game_mode            
        print("Por favor, digite um número correspondente a um modo de resolução válido.\n")


def solve_maze(game_mode: int, maze: Maze) -> Maze:
    """Chose the algorithm to play"""
    response = None
    if game_mode == 1: maze = a.breadth_first_search(maze)
    if game_mode == 2: maze = a.depth_first_search(maze)
    if game_mode == 3: maze = a.iterative_deeppening_search(maze)
    if game_mode == 4: maze = a.greedy_search(maze, euclidean_distance, weight=0)
    if game_mode == 5: maze = a.greedy_search(maze, euclidean_distance ,cost=True)
    if game_mode == 6: maze = a.greedy_search(maze, euclidean_distance ,cost=True, weight=2)
    return maze