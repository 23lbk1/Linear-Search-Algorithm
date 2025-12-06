def linear_search(num_list, target):
  arr = [] # Empty list to store each number in num_list once separated
  
  try:
    target = int(target) # Establishes target as an integer
  except ValueError:
    return "Error: Target value must be an integer."
  
  # Convert user inputs
  for x in num_list.split(","):
    if x == "":
      continue
      
    x = x.strip() # Removes any spaces before and after the number being evaluted at a given index (will remove any arbitrary amount of spaces)
    
    try:
      arr.append(int(x)) # Establishes the cleaned up number as an integer and appends it to the list arr
    except ValueError:
      return "Error: Please enter a list of integers separated by commas."

  
  steps = []  # Stores each step of the search
  
  # Linear Search
  for index, value in enumerate(arr):
    steps.append(f"Checking index {index}: value = {value}")

    if value == target:
      steps.append(f"\n Target {target} FOUND at index {index}")
      return "\n".join(steps)
      
  # If no target is found at the end of the loop:
  steps.append(f"\n Target {target} NOT FOUND in the list.")
  return "\n".join(steps)




# Gradio UI
app = gr.Interface(fn = linear_search, inputs = [gr.Textbox(label = "Enter a list of numbers separated by commas"),
                                                 gr.Textbox(label = "Enter the target value")],
                   outputs = gr.Textbox(label = "Search Steps"), title = "Linear Search Algorithm", description = """This app will run a linear search step-by-step and show every step.
Enter a list of integers separated by commas, and then a target value to begin.""")
