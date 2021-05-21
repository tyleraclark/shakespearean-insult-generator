#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:28:16 2019

Shakespearean insult generator

@author: Tyler Clark
"""

import numpy as np, tkinter as tk, json

#function that checks if the first letter of the first word is a vowel and returns an appropriate article
def articlechoice(firstword: str) -> str:
    #puts the whole word into lowercase, so we only have to check lowercase letters
    firstword = firstword.lower()
    #if the first letter of the first word is a vowel then we use "an"
    if firstword[0] == "a" or firstword[0] == "e" or firstword[0] == "i" or firstword[0] == "o" or firstword[0] == "u":
        article = "an"
    #if the first letter of the first word is a consonant then we use "a"
    else:
        article = "a"
    return(article)

def insult(words1: list, words2: list, words3: list) -> str:
    #a random word is taken from each list, we have three columns so three lists
    ranword1 = np.random.choice(words1)
    ranword2 = np.random.choice(words2)
    ranword3 = np.random.choice(words3)
        
    #calling function from the beginning
    article = articlechoice(ranword1)

    #return full insult in string from
    return f"\nYou're {article} {ranword1}, {ranword2} {ranword3}!\n"
        
#open JSON file containing words
f = 'words.json'
with open(f) as json_file:
    words = json.load(json_file)

#assign each list to a variable
words1= words['words1']
words2= words['words2']
words3= words['words3']

#create app
root = tk.Tk()

#Set Dimensions
root.geometry("350x200")
#Set title
root.title("Shakespearean Insult Generator")

#Make transparent with black background
root.attributes('-alpha', 0.90)
root.configure(bg = 'black')

#Make menubar black (LINUX-ONLY)
menubar = tk.Menu(root, background= 'black', fg='white')

#Make top and bottom frame, both with black backgrounds
top = tk.Frame(root, bg = 'black')
bottom = tk.Frame(root, bg = 'black')
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

#Top text in top frame
lbl1 = tk.Label(root, text = "\nWelcome to the Shakespearian Insult Generator!\n", bg = 'black', fg = 'white')
lbl1.pack(in_=top)

#Second line of text in top frame
lbl2 = tk.Label(root, text = "Would you like an insult?", bg = 'black', fg = 'white')
lbl2.pack(in_=top)

#if you click yes change the first line of text to an insult and the second a question
def click_yes():
    lbl1.config(text=insult(words1, words2, words3))
    lbl2.config(text="Do you want another?")

#Yes button in bottom frame
btn_yes = tk.Button(
    root,
    text = "Yes",
    width = 5,
    height = 1,
    command = click_yes,
    bg = 'black', fg = 'white'
)
btn_yes.pack(in_=bottom, side=tk.LEFT, padx = (120,10), pady = 40)

#No button in bottom frame
btn_no = tk.Button(
    root,
    text = "No",
    width = 5,
    height = 1,
    command = root.destroy,
    bg = 'black', fg = 'white'
)
btn_no.pack(in_=bottom, side=tk.LEFT, padx = (10, 120) )

root.mainloop()