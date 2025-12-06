def linear_search(num_list, target):
  arr = [] # Empty list to store each number in num_list once separated
  
  # Convert user inputs
  for x in num_list.split(","):
    if x == "":
      continue
    x = x.strip() # Makes sure that x is equated to only a number for the given index
    
    try:
      arr.append(int(x)) # Establishes the cleaned up number as an integer and appends it to the list arr
    except ValueError:
      return "Error: Please enter a list of integers separated by commas."
    try:
      target = int(target) # Establishes target as an integer
    except ValueError:
      return "Error: Target value must be an integer."
  
  # Linear Search
  for index, value in enumerate(arr):
    steps.append("Checking index " index ": value = ", value)

    if value == target:
      steps.append("\n Target ", target, " FOUND at index ", index)
      return "\n".join(steps)
      
  # If no target is found at the end of the loop:
  steps.append("\n Target ", target, " NOT FOUND in the list.")
  return "\n".join(steps)
