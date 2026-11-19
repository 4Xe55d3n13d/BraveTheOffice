# Brave The Office. By allaccessdenied (@4Xe55d3n13d on GitHub)
# NO AI WAS USED TO MAKE THIS GAME.
A simple, Earthbound inspired tower climb battle RPG where you have to survive wacky office hijinks on the way to deliver a report to your boss.
# 
# Installation:
# !!MAKE SURE YOU HAVE PYTHON 3.10 OR LATER INSTALLED!!
You can either install this by downloading all the files in the file list below into a folder or unzipping BraveTheOffice.zi, after which a folder with all the necessary files will populate.
# File List:
Make sure that the following files are present within the folder you unzip BraveTheOffice.zip in:
- enemies.csv
- game_test.py
- game.py
- item.py
- main.py
If any of these are missing, the game won't run.
#
# How to Play:
To play the game, run the following in your terminal while cd'ed into the folder with the game files inside:
python3 main.py

For help with the command, run the following in your terminal while cd'ed into the folder with the game files inside:
python3 main.py -help

This game has command line arguments you can pass in to modify the experience, the help command has all the directions you need from there.
#
# Test Script:
This game comes with a test script. To run the test script, run the following in your terminal with pytest installed:
pytest game_test.py