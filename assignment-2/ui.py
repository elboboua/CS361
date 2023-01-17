# import tkinter (GUI library)
from tkinter import *
from os import getcwd

# get random number from prng-service.txt
def getRandomNumber():
    # write the "run" command to the prng-service.txt file
    prng_text_file = open("prng-service.txt", "w")
    prng_text_file.write("run")
    prng_text_file.close()
    # wait for the prng-service.py to write the random number to the prng-service.txt file
    while True:
        # open the prng-service.txt file
        prng_text_file = open("prng-service.txt", "r")
        # read the contents of the file
        prng_text_file_contents = prng_text_file.read()
        # close the file
        prng_text_file.close()
        # check if the file contains a number
        if prng_text_file_contents.isdigit():
            # return the random number
            return prng_text_file_contents

def getRandomImageUrl():
    random_number = getRandomNumber()
    
    # write the random number to the image-service.txt file
    image_text_file = open("image-service.txt", "w")
    # write the random number to the file
    image_text_file.write(random_number)
    # close the file
    image_text_file.close()
    # wait for the image-service.py to write the image url to the image-service.txt file
    while True:
        # open the image-service.txt file
        image_text_file = open("image-service.txt", "r")
        # read the contents of the file
        image_text_file_contents = image_text_file.read()
        # close the file
        image_text_file.close()
        # check if the file contains a url
        if not image_text_file_contents.isdigit() and image_text_file_contents != "":
            # return the image url
            return image_text_file_contents
 
# create root window
root = Tk()
 
# set window title
root.title("Assignment 2 - Random Safari Animal Generator")
# set window size
root.geometry('600x400')
 
# widgets
# image widget centered
image_label = Label(root)
image_label.place(relx=.5, rely=.5,anchor= CENTER)

def generateRandomAnimal():
    print("Changing image to a random animal")
    # change the image to a random animal
    new_image_url = getRandomImageUrl()
    new_file = getcwd() + new_image_url
    new_image = PhotoImage(file=new_file)
    image_label.configure(image=new_image)
    image_label.image = new_image
    


randomImageButton = Button(root, text="Generate Random Animal", pady=5, command=generateRandomAnimal) 
randomImageButton.pack(pady=10)

# Execute Tkinter
root.mainloop()