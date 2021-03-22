# coding=utf-8
import os
import re
import csv

path = "C:/Users/jsyzdlf/Desktop/"
csv_name = "test.csv"
csvFile = open(path + csv_name, 'w')


def csv_lines():
    return len(csvFile.readlines()) - 1

