#!/usr/bin/env python3

# Sean Reid

import numpy as np
import matplotlib.pyplot as plt
import csv


def main():

	years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

	print("\nEnter city, then state. Example: Plattsburgh city, New York\n")
	print("Note: Inputs are case sensitive\n")

	city1 = input('Enter the name of a city: ')
	city2 = input('Enter the name of another city: ')
	city3 = input('Enter a third city: ')

	with open('populations.csv', 'r') as csvfile:
		cities = list(csv.reader(csvfile))

	for row in cities:
		if row[2] == city1:
			plt.plot(years, (list(map(int,row[5:12]))),'bs-', label = city1)
		elif row[2] == city2:
			plt.plot(years, (list(map(int,row[5:12]))),'r^-', label = city2)
		elif row[2] == city3:
			plt.plot(years, (list(map(int,row[5:12]))),'go-', label = city3)

	plt.title('New York Populations From 2010-2016')
	plt.xlabel('Year')
	plt.ylabel('Population')
	plt.legend(loc = 'upper right')
	plt.show()

if __name__ == '__main__':  
	main()


