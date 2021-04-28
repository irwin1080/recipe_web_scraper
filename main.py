'''
Program: Recipe Web Scrpaper
Description: A Python script that ingests a given website and turn back the desired Recipe Ingredients and Directions.
Purpose: Personal Project
Author: Irwin Dominguez
Next Items: send to google docs, auto detect site being passed in, fix function output
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

#function for Olive Magazine site. Print out key recipe items.
def createRecipeOliveMagazine(formatted_html):
    #print(formatted_html)

    #Olive Magazine - get title
    data_point = soup.select(".heading-1.template-article__title.template-article__title--image-led")
    for data in data_point:
        print(data.getText())

    #Olive Magazine - get serving
    data_point = soup.select(".heading-6.recipe-key-data__text")
    print(data_point[1].getText())


    #Olive Magazine - get items, get amount
    data_point = soup.select(".list-group__item")
    for data in data_point:
        print(data.getText())


    print("")
    #Olive Magazine - get instructions
    data_point = soup.select(".editor-content")
    for data in data_point:
        print(data.getText())

#function for Food&Wine site. Print out key recipe items.
def createRecipeFoodAndWine(formatted_html):
    #print(formatted_html)

    #Food&Wine - get title
    data_point = soup.select(".headline.heading-content")
    print(data_point[3].getText())

    #Food&Wine - get serving
    data_point = soup.select(".recipe-meta-item")
    print(data_point[2].getText())


    #Food&Wine - get items, get amount
    data_point = soup.select(".ingredients-item-name")
    for data in data_point:
        print(data.getText())


    print("")
    #Food&Wine - get instructions
    data_point = soup.select(".section-body")
    for data in data_point:
        print(data.getText())

#function for Food52 site. Print out key recipe items.
def createRecipeFood52(formatted_html):
    #print(formatted_html)


    #Food52 - get items, get amount
    data_point = soup.select(".recipe__list-qty")
    for data in data_point:
        print(data.getText())

    data_point = soup.select(".recipe__list-step  ")
    for data in data_point:
        print(data.getText())


#test sites all recipes
webiste_url = "https://www.allrecipes.com/recipe/16383/basic-crepes/"
#test sites #bon appetit
webiste_url = "https://www.bonappetit.com/recipe/chocolate-buttermilk-pie"
#test sites food52
webiste_url = "https://food52.com/recipes/11254-cappuccino-cheesecake"
#test sites food & wine
webiste_url = "https://www.foodandwine.com/recipes/balinese-grilled-chicken"
#test sites olive magazine
webiste_url = "https://www.olivemagazine.com/recipes/baking-and-desserts/coffee-and-cream-fridge-cake/"


#get the website data
website_data = requests.get(webiste_url)

#format data with bs4
soup = bs4.BeautifulSoup(website_data.text, "lxml")

#calling function to get recipe according to AllRecipes HTML standards
createRecipeAllRecipes(soup)
