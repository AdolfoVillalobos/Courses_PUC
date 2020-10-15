import os
import math
import numpy as np
import random
from menus import BeginMenu, GameMenu
from tablero import print_tablero
from parametros import PROB_LEGO, POND_PUNT

class LegoSweeper(object):


    def __init__(self):

        print("#######   Welcome to Lego Sweeper!! ####### \n")
        self.current_board = []
        self.end_game = False
        self.current_menu = None
        self.user_name = 'adolf'

        self.begin_menu_options = {
            0: self.exit_game,
            1: self.new_game,
            2: self.load_game,
            3: self.visualize_ranking
        }

        self.game_menu_options = {
            0: self.exit_game
        }

        self.bm = BeginMenu(available_options=list(self.begin_menu_options.keys()))
        self.gm = GameMenu(available_options=list(self.game_menu_options.keys()))

    def start(self):
        self.current_menu = self.bm
        while not self.end_game:
            self.current_menu.display_menu()
            user_action = self.current_menu.get_input()
            self.begin_menu_options[user_action]()

    ### Main Functions

    def load_game(self):
        user_name = input('Write the User Name: ')
        path = '{}.txt'.format(user_name)
        if path in os.listdir('partidas/'):
            print("I found a match!... Loading {}'s game\n".format(user_name))
            N, M, L, real_table, user_table, score = self._load_board(path)
            self._play_game(N, M, L, real_table, user_table)
        else:
            print("I did not found a match D: ....\n")

    def visualize_ranking(self):
        with open('puntajes.txt', 'r+') as f:
            lines = [line.replace('\n', '').split(',') for line in f.readlines()]
            lines = sorted(lines, key=lambda x: int(x[1]), reverse=True)
            print(" ")
            print("  User -  Score:")
            print("  --------------")
            for i, (user_name, user_score) in enumerate(lines):
                print('{}: {} - {}'.format(i+1, user_name, user_score))
            print('\n')

    def exit_game(self):
        print('Exiting...')
        self.end_game = True

    def new_game(self):
        self.user_name = input('Write the User Name: ')
        N, M, L, real_table, user_table = self._generate_tables()
        self._play_game(N, M, L, real_table, user_table)
        return real_table, user_table

    def _play_game(self, N, M, L, real_table, user_table):
        print("The Game Has started\n")
        turn = 0
        available_cells = N*M-L
        discovered_cells = self._discovered_cells(user_table)
        while discovered_cells<available_cells:
            print("Turn: {} --- Nº of Legos: {} --- Cells Left: {} ".format(turn, L, available_cells-discovered_cells))
            print_tablero(real_table)
            print_tablero(user_table)
            x = int(self.bm._receive_numeric_input('X coordinate: ', range(0, N)))
            y = int(self.bm._receive_numeric_input('Y coordinate: ', range(0, M)))
            out  = self._cell_discovery(x,y,real_table, user_table, discovered_cells, N, M, L)
            if out == None:
                break
            else:
                discovered_cells = out
            turn += 1

        if discovered_cells == available_cells:
            score = self._calculate_score(L, discovered_cells)
            self._save_game(N, M, L, real_table, user_table, score)
            print("You win!!... You got a score of {}".format(score))
            with open('puntajes.txt', 'a') as f:
                f.write('{},{}\n'.format(self.user_name, score))

    def _cell_discovery(self, x, y, real_table, user_table, discovered_cells, N, M, L):
        value = real_table[x][y]
        if value == 'L':
            score = self._calculate_score(L, discovered_cells)
            self._save_game(N, M, L, real_table, user_table, score)
            user_table[x][y] = value
            return None
        else:
            if user_table[x][y] != ' ':
                print('Your already discovered this cell!!')

            else:
                if value != 0:
                    user_table[x][y] = value
                    discovered_cells += 1
                else:
                    discovered_cells  += self._cascade_discovery(x,y,real_table, user_table, N,M)
            return discovered_cells

    def _cascade_discovery(self, x, y, real_table, user_table, N, M):
        done_zeros = []
        done_non_zeros = []
        stack = [(x,y)]
        while stack:
            zero = stack.pop(0)
            neighboors =self._get_neighboors(zero[0], zero[1], N, M)
            print(zero, neighboors)
            user_table[zero[0]][zero[1]] = 0
            for p, q in neighboors:
                if ((p,q) not in done_non_zeros) and (user_table[p][q] == ' '):
                    value = real_table[p][q]
                    user_table[p][q] = value
                    done_non_zeros.append((p,q))
                    if value == 0 and ((p,q) not in done_zeros):
                        stack.append((p,q))
                        done_zeros.append(zero)
        return len(done_non_zeros)+len(done_zeros)

    ## Auxiliar

    def _check_cell(self, real_table, i, j):
        try:
            if real_table[i][j] == 'L':
                return 1
            else:
                return 0
        except IndexError:
            return 0

    def _save_game(self, N, M, L, real_table, user_table, score):
        with open('partidas/{}.txt'.format(self.user_name), 'w') as f:
            f.write("{},{},{},{}\n".format(N,M,L,score))
            f.write("%s \n" % 'real_game')
            for row in real_table:
                    f.write("%s\n"% ','.join(list(map(str, row))))

            f.write("%s\n" % 'user_game')
            for row in user_table:
                    f.write("%s\n"% ','.join(list(map(str, row))))

    def _calculate_score(self,L, discovered_cells):
        return L*discovered_cells*POND_PUNT

    def _discovered_cells(self, user_table):
        d_cells = 0
        for row in user_table:
            for col in row:
                if col not in [' ', 'L']:
                    d_cells += 1
        return d_cells

    def _generate_tables(self):
        print("Creating New Game. You need to specify the board's dimensions:")
        N = int(self.bm._receive_numeric_input('N parameter: ', range(3,15)))
        M = int(self.bm._receive_numeric_input('M parameter: ', range(3,15)))
        L = math.ceil(N*M*PROB_LEGO)
        real_table = [[0 for _ in range(M)] for _ in range(N)]
        user_table = [[' ' for _ in range(M)] for _ in range(N)]
        real_table = self._fill_table(N=N, M=M, L=L, real_table=real_table)
        return N, M, L, real_table, user_table

    def _fill_table(self, N, M, L, real_table):
        for _ in range(L):
            a = random.randint(0, N-1)
            b = random.randint(0, M-1)
            real_table[a][b] = 'L'
            while real_table[a][b] != 'L':
                a = random.randint(0, N-1)
                b = random.randint(0, M-1)
                real_table[a][b] != 'L'
        for i in range(N):
            for j in range(M):
                if real_table[i][j] != 'L':
                    candidate_cells = self._get_neighboors(i,j,N,M)
                    neighbor_legos = 0
                    for (cell_i, cell_j) in candidate_cells:
                        neighbor_legos += self._check_cell(real_table, cell_i, cell_j)
                    real_table[i][j] = neighbor_legos
        return real_table

    def _get_neighboors(self, i, j, N, M):
        candidates = [(p,q) for (p,q) in [(i+k, j+l) for k in range(-1,2) for l in range(-1,2)] if (p in range(0,N) )and (q in range(0,M)) and ((p,q) != (i,j))]
        return candidates

    def _load_board(self, path):
        with open('partidas/{}'.format(path), 'r') as f:
            lines = list(f.readlines())
            N, M, L, score = map(int, lines[0].split(','))
            real_table = [row.replace('\n',"").split(',') for row in lines[2:N+2]]
            user_table = [row.replace('\n',"").split(',') for row in lines[N+3:2*N+3]]
        return N, M, L, real_table, user_table, score