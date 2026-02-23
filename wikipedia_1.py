"""
Name: wikipedia_1.py
Author: Paul Gray
Created: 02/22/2026
Purpose: 
"""

# pip install wikipedia
import wikipedia

# Type in your search term
search_terms = input("Search Wikipedia: ")

# Return a summary result of 3 sentences
summary = wikipedia.summary(search_terms, sentences=3)

# Print result
print(summary)