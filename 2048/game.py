import random
import copy
import pygame
import utils


class Game_2048:
    def __init__(self, file_path, matrix_size = (4, 4)):
        self.matrix_size = matrix_size
        self.file_path = file_path
        self.initialize ()

    def initialize(self):
        self.game_matrix = [['null' for i in range(self.matrix_size[0])] for i in range(self.matrix_size[1])]
        self.score = 0
        self.max_score = utils.read_max_score(self.file_path)
        self.direction = None
        self.randomGenerateNumber()
        self.randomGenerateNumber()
        print(self.game_matrix)

    def randomGenerateNumber(self):
        #generate a number in an empty position
        empty_pos = []
        for i in range(len(self.game_matrix)):
            for j in range(len(self.game_matrix[0])):
                if self.game_matrix[i][j] == 'null':
                    empty_pos.append((i, j))

        i, j = random.choice(empty_pos)
        self.game_matrix[i][j] = 2 if random.random() > 0.2 else 4

    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        #collape the same numbers
        #randomly generate a new number

        if self.direction == None:
            return

        if self.direction == "UP":
            for j in range(self.matrix_size[1]):
                #extract every col, merge the same numbers
                col = []
                for i in range(self.matrix_size[0]):
                    number = self.game_matrix[i][j]
                    if number != 'null':
                        col.append(number)
                # combine numbers
                col = self.merge(col)

                # put the col back to the matrix
                col += ['null'] * (self.matrix_size[0] - len(col))
                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j] = col[i]

        elif self.direction == "DOWN":
            for j in range(self.matrix_size[1]):
                # extract every col, merge the same numbers
                col = []
                for i in range(self.matrix_size[0]):
                    number = self.game_matrix[i][j]
                    if number != 'null':
                        col.append(number)
                # combine numbers
                col = self.merge(col)

                # put the col back to the matrix
                col = ['null'] * (self.matrix_size[0] - len(col)) + col
                for i in range(self.matrix_size[0]):
                    self.game_matrix[i][j] = col[i]
                print(self.game_matrix)

        elif self.direction == "RIGHT":
            for i in range(self.matrix_size[0]):
                # extract every col, merge the same numbers
                row = []
                for j in range(self.matrix_size[1]):
                    number = self.game_matrix[i][j]
                    if number != 'null':
                        row.append(number)
                # combine numbers
                row = self.merge(row)

                # put the col back to the matrix
                row = ['null'] * (self.matrix_size[0] - len(row)) + row
                for j in range(self.matrix_size[1]):
                    self.game_matrix[i][j] = row[j]
                print(self.game_matrix)

        elif self.direction == "LEFT":
            for i in range(self.matrix_size[0]):
                # extract every col, merge the same numbers
                row = []
                for j in range(self.matrix_size[1]):
                    number = self.game_matrix[i][j]
                    if number != 'null':
                        row.append(number)
                # combine numbers
                row = self.merge(row)

                # put the col back to the matrix
                row += ['null'] * (self.matrix_size[0] - len(row))
                for j in range(self.matrix_size[1]):
                    self.game_matrix[i][j] = row[j]
                print(self.game_matrix)

        self.direction = None


    def merge(self,lst):
        if len(lst) < 2:
            return lst
        for i in range(len(lst) - 1):
            numb1 = lst[i]
            if numb1 == 'null':
                break
            numb2 = lst[i+1]
            if numb1 == numb2:
                lst[i] *=2
                lst.pop(i+1)
                lst.append('null')
                self.score += lst[i]
        return self.extract(lst)

    def extract(self, lst):
        new_lst = []
        for i in lst:
            if i !='null':
                new_lst.append(i)
        return new_lst


    def update(self):
        game_matrix_before = copy.deepcopy(self.game_matrix)
        self.move()
        if game_matrix_before != self.game_matrix:
            self.randomGenerateNumber()
        if self.score > self.max_score:
            self.max_score = self.score

    def is_gameover(self):
        for i in range(len(self.game_matrix)):
            for j in range(len(self.game_matrix[0])):
                if self.game_matrix[i][j] == 'null':
                    return False
                elif (i == self.matrix_size[0]-1) and (j ==self.matrix_size[1] - 1):
                    return True
                elif (i == self.matrix_size[0] - 1):
                    if (self.game_matrix[i][j] == self.game_matrix[i][j+1]):
                        return False
                elif (j == self.matrix_size[1] - 1):
                    if (self.game_matrix[i][j] == self.game_matrix[i+1][j]):
                        return False
                else:
                    if (self.game_matrix[i][j] == self.game_matrix[i + 1][j]) or (
                            self.game_matrix[i][j] == self.game_matrix[i][j + 1]):
                        return False
        return True







