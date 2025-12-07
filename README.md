# Linear-Search-Algorithm

## Part 1
The project I have chosen to do is a linear search algorithm. Linear search algorithms provide a clear and intuitive way to demonstrate how searching algorithms operate at a fundamental level. Linear search makes every comparison step explicit, which is perfect for an educational, interactive visualization. The user can directly see how the algorithm scans through a list, evaluates each element, and how it determines whether the target value is found.

Another reason I have for selecting linear search is that it works on any type of dataset without requiring pre-processing, unlike algorithms that need specific structures. This allows users to enter any list of numbers and immediately test how the algorithm behaves.

From a computational thinking perspective, linear search is a perect example for illustrating decomposition and pattern recognition. Its repetitive comparison pattern is easy to connect to broader computing strategies, and its straightforward control flow helps show how input > processing > output are structured in algorithm design.


## Part 2
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

<img width="2352" height="354" alt="screenshot_1765123952" src="https://github.com/user-attachments/assets/05d26396-ec8c-4966-8fe3-b91a0a101f48" />
