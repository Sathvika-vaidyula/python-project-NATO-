import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary using a dictionary comprehension
p = {row['letter']: row['code'] for (index, row) in df.iterrows()}

choose = input("Enter word: ").upper()

# Generate the phonetic code list
o = [p[letter] for letter in choose if letter in p]

print(o)
