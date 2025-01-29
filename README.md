# A SIMPLE GAME - KAUN BANEGA CROREPATI USING SIMPLE PYTHON  

## How I made it:  

### Step 1  
Just make sure everything is okay and the user input is working fine, so I added a quick check that if the user wants to play or not.  
If yes, then they will enter `q` in uppercase or lowercase, and it automatically converts the input to lowercase.  

### Step 2  
Make a list of prize money so that I can iterate easily and the code looks good.  

### Step 3  
Two variables:  
- `winamt`: To detect how much the player won during the game.  
- `finwinamt`: To track the final winning amount as it has many stages.  

### Step 4  
Questions and answers were the tricky part—how should I store them and iterate without using a database or local storage?  

### Step 5  
I used a list with the question and answers in sequence and added the correct option at index `1`.  
**Example:**  
- Options: **HORSE, COW, BIKE, DOG**  
- If the correct answer is **BIKE**, then I stored `"C"` as it comes in the 3rd place.  

### Step 6  
I added a `try` statement to counter any errors in the game loop.  

### Step 7  
The questions iterated with answers in one loop using `i` as an index:  
- `question[i][0]` → Fetches the question.  
- `answer[i][1]` → Stores the correct answer.  
- Options: `question[i][2], question[i][3], question[i][4], question[i][5]`.  

### Step 8  
The `if-else` checks if the user-selected option matches the predefined correct option.  

### Step 9  
There's also a catch:  
- If the player crosses the **win slab** and wins another game, they will go out with the last **win slab** amount.  
- Another `if-elif` condition calculates that.  

### Step 10  
If any error occurs during the game due to user input, the program catches the exception using `except Exception as e`, displays the error, and ends smoothly.  

### Step 11  
**Please share your feedback. Thank you!** 🎉  
