#Ryland Bruce
#Stile Task
#The Product Team
#January 2023

import re
import PySimpleGUI as sg
import os

#Functions
#Turn paragraphs into sentences
def sentences(text):
    text = text.replace("\n"," ")
    end = re.compile('[.!?]')
    sentences = end.split(text)
    return sentences

#Display Images
def show_image(img):
    dirname, filename = os.path.split(os.path.abspath(__file__))
    pathname = os.path.join(dirname ,img)

    sg.theme("lightblue")  
    layout = [[sg.Image(pathname)]]
    window = sg.Window('Bakr.io').Layout(layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()
        

#Get file name from user
breadfile = input("Please enter text file name: ")

#Get user bread suggestions
print("This program will search the text file for any indications or links to bread.")
print("Please enter any specific types of bread to search for seperated by a comma.")
Suggestions = input("Suggestions: ")

#Create list of Suggestions
Suggestions = Suggestions.split(',')
if Suggestions == ['']:
    Suggestions = []

#Open file
with open(breadfile, 'r') as file:
    text = file.read()

#Determine if file has bread in it
if "bread" in text:
    HasBread = True
    print("This text has bread!") 
else:
    HasBread = False
    print("This text doesn't have bread:(")

#Bread Count
textlow = text.lower()
textlist = textlow.split()

breadcount = 0

for item in textlist:
    if "bread" in item:
        breadcount += 1

if HasBread == True:
    if breadcount == 1:
        print("This text has one mention of 'bread'")
    else:
        print("This text has " + str(breadcount) + " mentions of 'bread'")

#Split text into sentences
Sentences = sentences(text)

#Compile sentences with bread in them
BreadSentences = []
for item in Sentences:
    if "bread" in item.lower():
        BreadSentences.append(item)

#Print bread sentences and highlight bread
if HasBread == True:
    print("Bread is referenced in the following sentences:")
    for item in BreadSentences:
        line = item
        if line[0] == " ":
            line = line[1:]
        if "bread" in line:
            line = line.replace("bread","/bread/")
        if "Bread" in line:
            line = line.replace("Bread","/Bread/")
        if "BREAD" in line:
            line = line.replace("BREAD","/BREAD/")
        print(line+".")

#Fing types of Bread mentioned
#Bread list inspired by lists from https://restaurantclicks.com/types-of-bread/ and https://www.purewow.com/stories/types-of-bread-all-home-bakers-should-know/
BreadTypesPool = {"Sourdough":"sourdough.png",
    "Baguette":"baguette.png",
    "Brioche":"brioche.png",
    "Focaccia":"focaccia.png",
    "Ciabatta":"ciabatta.png",
    "Pita":"pita.png",
    "Challah":"challah.png",
    "Naan":"naan.png",
    "Pumpernickel":"pumpernickel.png",
    "Cornbread":"cornbread.png",
    "Matzo":"matzo.png",
    "Matzoh":"matzo.png",
    "Matza":"matzo.png",
    "Matzah":"matzo.png",
    "Flatbread":"flatbread.png"}
BreadTypes = []
for item in BreadTypesPool:
    if item.lower() in text.lower():
        BreadTypes.append(item)

SuggestedBread = []
for item in Suggestions:
    if item in text:
        if item not in SuggestedBread:
            SuggestedBread.append(item)
#The following bread terms are only counted as Bread realted if they appear in a sentence with bread.        
BreadAdjsPool = {
    "Rye":"rye.png",
    "Multigrain":"multigrain.png",
    "Whole Grain":"wholegrain.png", 
    "Soda":"soda.png",
    "Sprouted":"sprouted.png",
    "Potato":"potato.png",
    "Rice":"rice.png"}
BreadAdjs = []
for item in BreadAdjsPool:
    for i in BreadSentences:
        if item.lower() in i.lower():
            if item not in BreadAdjs:
                BreadAdjs.append(item)


breads = SuggestedBread+BreadTypes+BreadAdjs
if breads != ['']:
    if len(breads)==1:
        print("A bread related term in this text was", end=" ")
        for i in breads:
            print(i+'.')
    elif len(breads) > 1:
        print("Bread realated terms in this text were", end=" ")
        for i in breads:
            if i != breads[-1]:
                print(i, end=", ")
        print("and " + breads[-1]+'.')

#Select Bread image
Breads = {"Sourdough":"sourdough.png",
    "Baguette":"baguette.png",
    "Brioche":"brioche.png",
    "Focaccia":"focaccia.png",
    "Ciabatta":"ciabatta.png",
    "Pita":"pita.png",
    "Challah":"challah.png",
    "Naan":"naan.png",
    "Pumpernickel":"pumpernickel.png",
    "Cornbread":"cornbread.png",
    "Matzo":"matzo.png",
    "Matzoh":"matzo.png",
    "Matza":"matzo.png",
    "Matzah":"matzo.png",
    "Flatbread":"flatbread.png",
    "Rye":"rye.png",
    "Multigrain":"multigrain.png",
    "Whole Grain":"wholegrain.png", 
    "Soda":"soda.png",
    "Sprouted":"sprouted.png",
    "Potato":"potato.png",
    "Rice":"rice.png"}

MentionedBreads = BreadTypes+BreadAdjs
if HasBread == False and len(BreadTypes+BreadAdjs) == 0:
    image = "nobread.png"
elif len(BreadTypes+BreadAdjs) == 0:
    image = "bread.png"
elif len(BreadTypes+BreadAdjs) == 1:
    image = Breads[MentionedBreads[0]]
else:
    image = "breads.png"

#Display Image
show_image(image)


