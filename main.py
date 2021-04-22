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

#function for All Recipes site. Print out key recipe items.
def createRecipeAllRecipes(formatted_html):
    step_num = 1
    #print(formatted_html)

    #all recipes - get ingredients
    data_point = soup.select(".ingredients-item-name")

    for data in data_point:
        print(data.getText())

    #all recipes  - get instructions
    print("\n")
    data_point = soup.select(".paragraph")
    for data in data_point:
        print(f"Step {step_num}: {data.getText()}")
        step_num+=1


#test sites all recipes
webiste_url = "https://www.allrecipes.com/recipe/16383/basic-crepes/"

#get the website data
website_data = requests.get(webiste_url)

#format data with bs4
soup = bs4.BeautifulSoup(website_data.text, "lxml")

#calling function to get recipe according to AllRecipes HTML standards
createRecipeAllRecipes(soup)
