# import random (for random number generation)
import random
# import time (for sleep)
import time

def generatePseudoRandomNumber():
    # generate a random number between 0 and 4: (we have 5 images)
    random_number = random.randint(0, 4)
    # return the random number
    return random_number


# Check if prng-service-txt has the "run" command in it every 100 milliseconds
while True:
    # open the prng-service.txt file
    prng_text_file = open("prng-service.txt", "r")
    # read the contents of the file
    prng_text_file_contents = prng_text_file.read()
    # close the file
    prng_text_file.close()
    # check if the file contains the "run" command
    if prng_text_file_contents == "run":
        # generate a random number
        print("Generating random number")
        random_number = generatePseudoRandomNumber()
        # open the prng-service.txt file
        prng_text_file = open("prng-service.txt", "w")
        # write the random number to the file
        prng_text_file.write(str(random_number))
        # close the file
        prng_text_file.close()

    # sleep for 100 milliseconds
    time.sleep(0.1)