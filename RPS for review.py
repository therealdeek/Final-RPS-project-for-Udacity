#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']


class Player:

    my_move = random.choice(moves)
    their_move = random.choice(moves)
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input('rock, paper, or scissors: ').lower()
            print()
            if move in moves:
                return move
            print("wrong choice, please enter the correct choice")


class AlwaysRock(Player):
    pass


class ReflectPlayer(Player):

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            index = moves.index(self.my_move) + 1
            if index == len(moves):
                index = 0
            return moves[index]

    def learn(self, my_move, their_move):
        self.my_move = my_move

# player that always chooses rock


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # sets starting scoring
        self.score_p1 = 0
        self.score_p2 = 0

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f" Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.score_p1 += 1
            print("Player 1 wins! ")
            print()
        elif beats(move2, move1) is True:
            self.score_p2 += 1
            print("Player 2 wins! ")
            print()
        else:
            print("No winners, because it's a tie! ")
        print(f'Player 1 score: {self.score_p1} ',
              f'Player 2 score: {self.score_p2} ')
        print()

    def play_game(self):
        print("Game start!")
        self.rounds = 7
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        if self.score_p1 > self.score_p2:
            print()
            print('Player 1 wins as usual, get better Player 2! ')
            print()
            print("Game over! Come on back now, you hear!?!?!?")
            print()
        elif self.score_p2 > self.score_p1:
            print()
            print("Player 2 won this time, Player 1 are you okay!?!? ")
            print()
            print("Game over! Come on back now, you hear!?!?!?")
            print()
        else:
            print("The game is a TIE! Stalemate! ")
            print()
            print("Game over! Come on back now, you hear!?!?!?")
            print()

        print(f'The final score is:  '
              f'Player 1 final score: {self.score_p1} ',
              f'Player 2 final score: {self.score_p2} ')


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
