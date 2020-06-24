#!/usr/bin/python3
# reddit checker
# big thanks to https://github.com/crock for his helpful code
# from https://twitter.com/c0rtepentest and updated to python3

import configparser
import requests
import time
import os

config = configparser.ConfigParser()
config.read('config.ini')

def check(name):
	ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.3"
	headers = {"user-agent": ua}
	params = {"user": name}
	
	request = requests.get('https://www.reddit.com/api/username_available.json', params=params, headers=headers)
	text = request.text
	if text == "true":
		print("The reddit", name, "is avaliable")
		file = open(output(), 'a')
		file.write("%s\n" % (name))
		file.close()
	else:
		print("The reddit", name, "is not avaliable")
	
def read():
	words = []
	path = os.path.join("word_lists", config.get('default','wordList'))
	if path is not None:
		file = open(path, 'r', encoding='utf-8-sig')
		words = file.read().split('\n')
		file.close()
	else:
		print("Word list not found.")
	
	for i in range(len(words)):
		name = words[i]
		check(name)
	print("All done")
	input("Press enter to exit...")

def output():
	return config.get('default', 'output', fallback="AVAILABLE.txt")
	
def main():
	print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+  ___ ___ __  __  _ _____   _  _   __  ___ ___    ____  _ ___ ____  _____ ___  +
+ | _ \ __| _\| _\| |_   _| | || |/' _/| __| _ \  / _/ || | __/ _/ |/ / __| _ \ +
+ | v / _|| v | v | | | |   | \/ |`._`.| _|| v / | \_| >< | _| \_|   <| _|| v / +
+ |_|_\___|__/|__/|_| |_|    \__/ |___/|___|_|_\  \__/_||_|___\__/_|\_\___|_|_\ +
+                                                                               +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Make sure to read the config.ini and README.md on github
''')
	print("1 = Enter username manually\n2 = Read a list of usernames from the word_lists folder")
	set = ["1", "2"]
	option = input("Select your option: ")
	while True:
		if str(option) in set:
			if option == set[0]:
				name = input("Enter a username: ")
				check(name)
			else:
				read()
				break
		else:
			option = input("1 or 2 ... Please!: ")
main()
# recoded by https://github.com/jnoc

