#!/usr/bin/python3
"""
This module prints a text by using . , ? as a delimiters
"""
def text_indentation(text):
    """Text indentation function
    Args:
        text: the text to be delimit
    Return: Reterns the text line by line after . , ?
        """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    delim = [".", "?", ":"]
    print_it = ""
    for c in text:
        if c in delim:
            print_it += c + "\n\n"
        else:
            print_it += c
    """ To remove new lines at the end and beginning"""
    print_it = (print_it.strip("\n"))
    print(print_it)
