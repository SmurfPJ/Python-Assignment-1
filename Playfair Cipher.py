string_old = input("What is your keyword: ")

# Formating Keyword
string = string_old + "abcdefghiklmnopqrstuvwxyz"
string = string.upper()
string = string.replace("J", "I")
string = string.replace(" ", "")
new_string = ""
for char in string:
    if char not in new_string:
        new_string += char
# print(new_string)

plaintext = input("\nEnter you plaintext: ")

array_2D = [[None]*5 for _ in range(5)]
letter_num = 0
for i in range(5):
    for j in range(5):
        array_2D [i][j] = new_string[letter_num]
        letter_num += 1
# print(array)

# Presenting cipher grid

print(" _____________________", end="")
for i in range(5):
    print("\n | ", end="")
    j = 0
    for j in range(5):
        print(array_2D[i][j], "| ", end="")
        j += 1
print("\n ---------------------", end="")


# Grid Example:
# ___________________
#| A | B | C | D | E | 
#| F | G | H | I | K | 
#| L | M | N | O | P |
#| Q | R | S | T | U | 
#| V | W | X | Y | Z | 
# -------------------