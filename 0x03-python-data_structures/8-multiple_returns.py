#!/usr/bin/python3
def multiple_returns(sentence):
    for char in sentence:
        print("length:{:d} - First character {}".format(len(char), char[0]))
