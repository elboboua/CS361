# import time (for sleep)
import time

# images urls
image_urls = [
    "/images/giraffe.png",
    "/images/lion.png",
    "/images/hyena.png",
    "/images/ostrich.png",
    "/images/alligator.png"
]

while True:
    # open the image-service.txt file
    image_text_file = open("image-service.txt", "r")
    # read the contents of the file
    image_text_file_contents = image_text_file.read()
    # close the file
    image_text_file.close()

    if image_text_file_contents.isdigit():
        # get the image url
        image_url = image_urls[int(image_text_file_contents)]
        # open the image-service.txt file
        image_text_file = open("image-service.txt", "w")
        # write the image url to the file
        image_text_file.write(image_url)
        print("Generating random image")
        # close the file
        image_text_file.close()

    # sleep for 100 milliseconds
    time.sleep(0.1)