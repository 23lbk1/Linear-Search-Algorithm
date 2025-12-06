def linear_search(num_list, target):
  # Convert user inputs
  arr = [] # Empty list to store each number in num_list once separated
  target = int(target) # Establishes target as an integer
  steps = []  # Stores each step of the search to be displayed on gradio
  
  for x in num_list.split(","):
    x = x.strip() # Makes sure that x is equated to only a number for the given index
      arr.append(int(x)) # 

  # Linear Search
  for index, value in enumerate(arr):
    steps.append("Checking index " index ": value = ", value)

      if value == target:
        steps.append("\n Target ", target, " FOUND at index ", index)
        return steps

  # If no target is found at the end of the loop:
  steps.append("\n Target ", target, " NOT FOUND in the list.")
  return steps

