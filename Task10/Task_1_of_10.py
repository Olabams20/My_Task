strtxt = "python"
text = "I am learning python programming"

try:
    if "python" == strtxt.lower():
        print("The string contains 'python'.")
    elif "python" in text:
        print("The string contains 'python' in the text.")
    else:
        print("The string does not contain 'python'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed.")
