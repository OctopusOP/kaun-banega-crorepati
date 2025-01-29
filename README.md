# A SIMPLE GAME - KAUN BANEGA CROREPATI USING SIMPLE PYTHON

How i made it-
step 1 - Just make sure everything is okay and the user input is working fine so i added a quick check that if the usre want to play or not if yes then he will enter q in uppercase or lowercase it automatically lowercse the input.
step 2 - Make a list of prizemoney so that i can iterate easily and the code looks good
step 3 - two variable one is winamt and one is finwinamt to detect how much the player won during the game. as it has many stages.
step 4 - questions and answers were the tricky part that how should i store it and how to iterate without database or local storage.
step 5 - so used a list with the question with answers according to the sequence and added the correct option inn index 1 : example HORSE,COW,BIKE,DOG - IF THE CORRECT ANS IS BIKE THEN I STORED - C as it comes in 3rd place
step 6 - the i added a try statement to counter any errors in the game loop.
step 7 - the the question iterated with ans i one loop usind i as a index for every question[i][0] and answer [i][1] then gave options with [i][2],[i][3],[i][4],[i][5]
step 8 - the if,else does the option matching with the pre defined option with the user input option.
step 9 - there's also a catch that if the player crosses the winslab then wins another game he will go out with the last winslab so another if ,elif calculates that.
step 10- if any eroor occurs during the game because of user input then it comes down to exception with the error as e and the program ends smoothly.
step 11 - please share your feedback, Thank you.
