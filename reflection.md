# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
When I first ran the game, it looked functional, but after testing it I found several gameplay and logic issues. 
The most noticeable bug was that the hints were reversed: when my guess was too low, the game told me to go lower, and when my guess was too high, it told me to go higher. 
I also found problems with the difficulty settings, such as Hard mode having a smaller range than Normal mode and the New Game button ignoring the selected difficulty. Another issue was that entering invalid input still consumed an attempt. 
Finally, after finishing a game and clicking New Game, the score and history were not reset, and the game would not accept new guesses, leaving it in a broken state.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 30 when secret is 45 | Tell player to "Go Higher" | Told player to "Go Lower "| None |
| Guess 99 when secret is 45 | Tell player to "Go Lower" | Told player to "Go Higher" | None |
| Click New Game while on Easy Difficulty| Secret Number should be between 1-20 |Secret can be anywhere from 1-100 | None |
| Click New Game after finishing a game | Start a fresh game with reset score, cleared history and ability to keep playing | Attempts and Secrets reset, but score and history remain, and the game would not accept new guesses | None |
| Enter "hello" as guess | Show validation error and not consume attempt| Showed error but still consumed an attempt | None|
| Select Hard Difficulty | Hard mode should be harder than Normal mode | Hard range is easier than Normal range, uses a range of 1-50 while Normal is 1-100 | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
