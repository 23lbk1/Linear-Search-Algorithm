def linear_search(num_list, target):
  cleaned_num_list = [] # Empty list to store each number in num_list once separated

  
  # Establishes target as an integer or returns an error if it is not compatible
  try:
    target = int(target)
  except ValueError:
    return "Error: Target value must be an integer."

  
  # Convert user inputs
  for num in num_list.split(","):
    num = num.strip() # Removes any spaces before and after the number being evaluted at a given index (will remove any arbitrary amount of spaces)
    
    if num == "":
      continue
    
    try:
      cleaned_num_list.append(int(num)) # Establishes the cleaned up number as an integer and appends it to the list cleaned_num_list
    except ValueError:
      return "Error: Please enter a list of integers separated by commas."

  
  # Prevent empty and invalid input
  if not cleaned_num_list:
    return "Error: Please enter at least one valid integer."

  
  steps = [] # Stores each step of the search to be displayed on the Gradio UI
  
  # Linear Search: scans left to right and records each comparison
  for index, value in enumerate(cleaned_num_list):
    steps.append(f"Checking index {index}: value = {value}")
    
    if value == target:
      steps.append(f"\nTarget {target} FOUND at index {index}")
      return "\n".join(steps)
      
  # If no target is found at the end of the loop:
  steps.append(f"\nTarget {target} NOT FOUND in the list.")
  return "\n".join(steps)




import gradio as gr

# Gradio UI
app = gr.Interface(
  fn = linear_search,
  
  inputs = [
    gr.Textbox(
      label = "Enter a list of numbers separated by commas",
      placeholder = "Example: 4, 7, 12, 2"
    ),
    gr.Textbox(
      label = "Enter the target value",
      placeholder = "Example: 2"
    )
  ],
  
  outputs = gr.Textbox(
    label = "Search Steps",
    lines = 5,
    max_lines = 40
  ),
  
  title = "Linear Search Algorithm",
  
  description = """This app will run a linear search step-by-step and show every step.
  Enter a list of integers separated by commas, and then a target value to begin.""")

if __name__ == "__main__": # Prevents app from launching when importing the algoritm
  app.launch()
