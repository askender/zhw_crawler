# -*- coding: utf-8 -*-
import csv


def get_list(fname):
    words = []
    with open(fname) as f:
        for word in f:
            word = word.decode('utf-8')
            word = word.replace('\n', '')
            if word:
                words.append(word)
    return words


def get_numlist(fname):
    words = []
    with open(fname) as f:
        for word in f:
            word = word.decode('utf-8')
            word = word.replace('\n', '')
            if word:
                words.append(int(word))
    return words


def read_csv(fname):
    tags = []
    for i in csv.DictReader(open(fname), delimiter=','):
        tags.append(i)
    return tags
