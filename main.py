'''
Program: Recipe Web Scrpaper
Description: A Python script that ingests a given website and turn back the desired Recipe Ingredients and Directions.
Purpose: Personal Project
Author: Irwin Dominguez
'''
#import necessary modules
#to make get requests to desired websites
import requests
#to convert request data into text
import bs4
website_url = input("What recipe would you like to extract? ")
print(website_url)

website_data = requests.get(website_url)
print(website_data)
