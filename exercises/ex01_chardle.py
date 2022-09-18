"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730468655"

frequency = 0

clever: str = input("Enter a 5-character word:") 
if len(clever) != 5:
    print("Error: word must contain 5 characters")
    exit()
nerves: str = input("Enter a single character:")
if len(nerves) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + nerves + " in " + clever)
if nerves == clever[0]:
    print(nerves + " found at index 0 ")
    frequency = frequency + 1
if nerves == clever[1]:
    print(nerves + " found at index 1 ")
    frequency = frequency + 1 
if nerves == clever[2]:
    print(nerves + " found at index 2 ")
    frequency = frequency + 1
if nerves == clever[3]:
    print(nerves + " found at index 3 ")
    frequency = frequency + 1
if nerves == clever[4]:
    print(nerves + " found at index 4 ")
    frequency = frequency + 1

if frequency == 0:
    print("No instances of " + nerves + " found in " + clever)
if frequency == 1:
    print("1 instance of " + nerves + " found in " + clever)
if frequency == 2:
    print("2 instances of " + nerves + " found in " + clever)
if frequency == 3:
    print("3 instances of " + nerves + " found in " + clever)
if frequency == 4:
    print("4 instances of " + nerves + " found in " + clever)
if frequency == 5:
    print("5 instances of " + nerves + " found in " + clever)
