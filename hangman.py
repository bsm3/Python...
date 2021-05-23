#!/usr/bin/env python3

import random
import time
import sys
import os


text = ".words"
k = 0
limit = 7

def hangman(k):
	time.sleep(0.7)
	os.system("clear")
	if k == 1:
		print("Wrong guess. " + str(limit - k) + " guesses remaining")
		print("  ____ ")
		print(" |    |")
		print(" |    |")
		print(" |     ")
		print(" |     ")
		print(" |     ")
		print(" |     \n")
		
	elif k == 2:
		print("Wrong guess. " + str(limit - k) + " guesses remaining")
		print("  ____  ")
		print(" |    | ")
		print(" |    | ")
		print(" |    O ")
		print(" |      ")
		print(" |      ")
		print(" |      \n")
		
	elif k == 3:
		print("Wrong guess. " + str(limit - k) + " guesses remaining")
		print("  ____ ")
		print(" |    |")
		print(" |    |")
		print(" |    O")
		print(" |    | ")
		print(" |     ")
		print(" |     \n")
		
	elif k == 4:
		print("Wrong guess. " + str(limit - k) + " guesses remaining")
		print("  ____ ")
		print(" |    |")
		print(" |    |")
		print(" |    O")
		print(" |   /|")
		print(" |     ")
		print(" |      \n")
		
	elif k == 5:
		print("Wrong guess. " + str(limit - k) + " guesses remaining")
		print("  ____ ")
		print(" |    |")
		print(" |    |")
		print(" |    O")
		print(" |   /|\\")
		print(" |      ")
		print(" |      \n")
		
	elif k == 6:
		print("Wrong guess. " + str(limit - k) + " guesses remaining")
		print("  ____ ")
		print(" |    |")
		print(" |    |")
		print(" |    O")
		print(" |   /|\\")
		print(" |   /  ")
		print(" |      \n")
	elif k == 7:
		print("  ____ ")
		print(" |    |")
		print(" |    |")
		print(" |    O")
		print(" |   /|\\")
		print(" |   / \\ ")
		print(" |      \n")
		


def hang(word, string, cpy):
	global k
	if word == '_' * len(word):
		return string
	if k == limit:
		return 0
	print("Missed characters: {}".format(cpy))
	char = input(" {}  Enter your guess: ". format(" ".join(string))).strip()
	if len(char) == 0 or len(char) > 1 or char <= "9" or char in cpy:
		print()
		hang(word, string, cpy)
	elif char in word:
		index = word.find(char)
		word = word[:index] + "_" + word[index+1:]
		string = string[:index] + list(char) + string[index+1:]
		print()
		while char in word:
			index = word.find(char)
			word = word[:index] + "_" + word[index+1:]
			string = string[:index] + list(char) + string[index+1:]

		time.sleep(0.7)
	else:
		k += 1
		cpy.append(char)
		hangman(k)
	return hang(word, string, cpy)

def start():
	word = ""
	cpy = []
	rand = random.randint(1, 7)
	rand = str(rand)
	with open(text, "r") as f:
		i = f.read(1)
		while i:
			if i == rand:
				f.read(1)
				word = f.readline()
				break
			f.readline()
			i = f.read(1)
	word = word[:len(word)-1]
	string = ['_'] * len(word)
	end = hang(word, string, cpy)

	if end:
		print("{}\n".format("".join(end)))
		print("Congrats! You have guessed the word correctly!\n")
		ch = input("Do You want to play again? (y)yes/(n)no: ")
		while ch not in ["Y", "y", "N", "n"]:
			ch = input("Do You want to play again? (y)yes/(n)no: ")
		if ch == 'y':
			os.system("clear")
			main()
		elif ch == 'n':
			exit()
	else:
		print("Wrong guess. You are hanged!!!\n")
		ch = input("Do You want to play again? (y)yes/(n)no: ")
		while ch not in ["Y", "y", "N", "n"]:
			ch = input("Do You want to play again? (y)yes/(n)no")
		if ch.lower() == 'y':
			os.system("clear")
			main()
		elif ch.lower() == 'n':
			exit()


def main():
	j = 0
	print("Welcome to Hangman game\n")
	name = input("Enter your name: ")
	print("Hello {}! Best of Luck!".format(name.capitalize()))
	time.sleep(2)
	os.system("clear")
	print("Let's play Hangman")
	time.sleep(1)
	os.system("clear")
	
	while j < 2:
		print("Loading ", end = "")
		for i in range(4):
			sys.stdout.flush()
			time.sleep(0.7)
			print(".", end = "")
		print()
		j += 1
		os.system("clear")	
	print()
	start()
	main()

main()

