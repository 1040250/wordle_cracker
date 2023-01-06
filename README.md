# WORDLE CRACKER
#### Video demo:  https://youtu.be/Z4KaxiZ1UE8


This program helps you solve any English-language [Wordle](https://www.nytimes.com/games/wordle/index.html) game in typically four moves.

It takes your guesses and the resulting color clues as input and optimizes your next guess. As start word, "arose" is recommended.

Wordle is a web-based word game created and developed by Welsh software engineer Josh Wardle, and owned and published by The New York Times Company. Players have six attempts to guess a five-letter word, with feedback given for each guess in the form of colored tiles indicating when letters match or occupy the correct position. Wordle has a single daily solution, with all players attempting to guess the same word.

After every guess, each letter is marked as either green, yellow or gray: green indicates that letter is correct and in the correct position, yellow means it is in the answer but not in the right position, while gray indicates it is not in the answer at all. Multiple instances of the same letter in a guess, such as the "o"s in "robot", will be colored green or yellow only if the letter also appears multiple times in the answer; otherwise, excess repeating letters will be colored gray. The game has a "hard mode" option, which requires players to include letters marked as green and yellow in subsequent guesses. This program supports hard mode.

The programm will prompt you for your guess (must be five-letter word) and the feedback from Wordle. You encode the feedback in five characters, each representing one of the letters of your guess, in order. You type 
- "a" or "1" for green, 
- "b" or "2" for yellow, and 
- "c" or "3" for grey. 

Example: "abbcc" (or "12233") means the first letter is green, second and third yellow, the other two grey.

The program returns the subset of the word list that fulfils the constraints provided by the feedback. The list is sorted in a way that the most common letters are preferred. The score for each word is printed next to the word.

The word list used here is the one from [@tabatkins](https://github.com/tabatkins/wordle-list/blob/main/words), according to whom it has all the "valid guesses in wordle, taken straight from the game's source code".
