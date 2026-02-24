import time
import sys

# Function to type out each line
def type_lyric(line, char_delay=0.085):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()  # Move to next line

# Function to print all lyrics
def print_lyrics():
    lyrics = [
        "Baby",
        "I'm",
        "Dancing in the dark",
        "With you between my arms",
        "Barefoot on the grass",
        "While listenin' to our favourite song",
        "When you said you look a mess",
        "I whispered underneath my breath",
        "You",
        "Heard it,",
        "Darling, you look perfect tonight",
        "Well, I found a woman",
        "Stronger than anyone I know",
        "She said my dreams, I hope that someday",
        "I'll share her home",
        "I found a love",
        "To carry more than just my secrets",
        "To carry love",
        "To carry childrens",
        "Of our own"
        
      
    ]

    delays = [0.5,3, 1.6,2.3, 1.3, 0.7, 1, 1, 1,1,7.5,2.0,0.6, 0.7, 2, 2.9,2.2, 1, 0.5,0.5]

    
    print("\nProgram created by Lyx\n")
    print("\nBy edd sheeran\n")
    print("\nPerfect\n")
    time.sleep(5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

# Call the function to actually print lyrics
print_lyrics()