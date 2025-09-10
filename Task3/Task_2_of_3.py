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

# Given a string with extra spaces, remove the leading and trailing spaces.
def remove_extra_spaces(input_string):
    return input_string.strip()

input_string = " Hello World "
print(remove_extra_spaces(input_string))

# Ask the user to enter a sentence and print the number of vowels in it.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count

input_string = input("Enter a sentence:")
print("Number of vowels:", count_vowels(input_string))    


# Convert a string "1234" to an integer and multiply it by 2.
def convert_and_multiply(input_string):
    return int(input_string) * 2
input_string ="1234"
print(convert_and_multiply(input_string))
