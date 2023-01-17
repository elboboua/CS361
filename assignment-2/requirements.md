# Requirements

1. UI must either have a button (if UI is graphical) or be able to receive a user command (if UI is text-based)
1. Each of the three programs must run in a different process
1. Programs must NOT call each other directly (e.g., do not import one program into another)
1. As the communication pipe, use text files as follows:
    - UI calls PRNG Service by writing the word "run" to prng-service.txt
    - PRNG Service reads prng-service.txt, erases it, and writes a pseudo-random number to it
    - UI reads prng-service.txt to get the pseudo-random number
    - UI writes the pseudo-random number to image-service.txt
    - Image Service reads image-service.txt, erases it, and writes an image path to it
    - UI reads image-service.txt then displays the image (or path) to the user
1. Create a short video (5 minutes or less) demonstrating you have satisfied the require- ments.
