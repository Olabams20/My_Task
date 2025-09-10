#  Check if a given string contains the substring "python" (case-insensitive).
strtxt ="python"

text = "I am learing python programming"

if "python" == strtxt.lower:{
    print("the string contains 'python'.")
}
else:{
    print("The string contains 'python'.")

}
#===============OR
if "python" in text.lower():
    print("the string contains 'python'.")
else:
    print("the string does not contain 'python'.") 

    #  Write a program to reverse a string without using slicing ([::-1]).
def reverse_string(input_string):
    reversed_string =""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string    

input_string ="Hello World"
print(reverse_string(input_string))