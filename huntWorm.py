#!/usr/bin/env python
#coding:utf-8
from random import choice
number = range(1,21)
player_num = choice(number)
worm_num = choice(number)
while player_num == worm_num:
    player_num = choice(number)

print "welcome to this Game!"
while True:
    print "you are in cave",player_num
    if (player_num == worm_num + 1 or player_num == worm_num - 1):
        print "worm is nearby!"

    print "which the next"

    player_input = raw_input(">")
    if  (not player_input.isdigit() or int(player_input) not in number):
        print "error,input again!"

    else:
        player_num = int(player_input)
        if (player_num == worm_num):
            print "you win,you get it!"
            break
    
