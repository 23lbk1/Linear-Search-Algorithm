# Linear-Search-Algorithm

## Algorithm Choice
The project I have chosen to do is a linear search algorithm. Linear search algorithms provide a clear and intuitive way to demonstrate how searching algorithms operate at a fundamental level. Linear search makes every comparison step explicit, which is perfect for an educational, interactive visualization. The user can directly see how the algorithm scans through a list, evaluates each element, and how it determines whether the target value is found.

Another reason I have for selecting linear search is that it works on any type of dataset without requiring pre-processing, unlike algorithms that need specific structures. This allows users to enter any list of numbers and immediately test how the algorithm behaves.

From a computational thinking perspective, linear search is a perect example for illustrating decomposition and pattern recognition. Its repetitive comparison pattern is easy to connect to broader computing strategies, and its straightforward control flow helps show how input > processing > output are structured in algorithm design.


## Planning Using Computational Thinking
### Decomposition
Linear searching can be broken down into a few clear steps:
1. Receive input as a list of values and a target to search for.
2. Compare the first element of the list to the target.
3. If they match, return the index and stop.
4. If they do not match, move to the next index and repeat.
5. If the end of the list is reached and the target wasn't found return "Not found".

### Pattern Recognition
The algorithm follows a repeating pattern: check one element, compare to the target, move to the next target and repeat.

### Abstraction
To maintain simplicity, the user won't see:
- Loop counters or value updates for internal variables.
- The only things shown are the current index being checked, the value at that position, and whether or not it matches the target.

### Algorithm Design
Input: A list of numbers and a target number.
Processing: Iterate through the list left to right, comparing each element to the target.
Output: The index where the target was found in the list or "Not found". Additionally, each iterated step (i.e. the index, current value being compared, and if it matches target) is displayed on the UI.


## Test Cases
### Valid Inputs:
<img width="2349" height="333" alt="screenshot_1765125051" src="https://github.com/user-attachments/assets/cbbc7b0c-21c5-4afa-97ca-9742064ff6ff" />
<img width="2347" height="338" alt="screenshot_1765124005" src="https://github.com/user-attachments/assets/b9b5bbe4-1596-4841-8051-a496d3cbe610" />
<img width="2347" height="324" alt="screenshot_1765123988" src="https://github.com/user-attachments/assets/7bfe5cea-a170-4470-aa4f-32ea387fbbe0" />
<img width="2338" height="608" alt="screenshot_1765125183" src="https://github.com/user-attachments/assets/1415545a-fc81-4323-ba15-33ada08d824f" />
<img width="2345" height="324" alt="screenshot_1765124070" src="https://github.com/user-attachments/assets/e2546ec6-bcb3-419a-92b2-1b86fbf5c227" />
<img width="2346" height="340" alt="screenshot_1765124056" src="https://github.com/user-attachments/assets/f4b440e2-6d8a-40fb-b265-b3a2e280b352" />

### Edge Cases:
<img width="2346" height="313" alt="screenshot_1765124088" src="https://github.com/user-attachments/assets/1454917d-f0f5-4c9d-a386-29918f3450fd" />
<img width="2349" height="336" alt="screenshot_1765124035" src="https://github.com/user-attachments/assets/9b03d45d-4430-4999-9e53-23f5f8e6a33b" />
<img width="2343" height="323" alt="screenshot_1765124175" src="https://github.com/user-attachments/assets/1b639068-148b-42b3-9264-6f88aa68b32b" />
<img width="2341" height="340" alt="screenshot_1765124193" src="https://github.com/user-attachments/assets/65edc646-491f-432d-9d64-b3dc0f144825" />
<img width="2350" height="324" alt="screenshot_1765124138" src="https://github.com/user-attachments/assets/16dbc3ca-f961-4659-9ae7-a63af2567d41" />
<img width="2343" height="324" alt="screenshot_1765124218" src="https://github.com/user-attachments/assets/4a0970c0-76c6-4517-8b4c-3af8540244bc" />
