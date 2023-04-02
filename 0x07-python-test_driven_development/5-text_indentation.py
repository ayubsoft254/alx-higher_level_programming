#!/usr/bin/python3
""" a function that helps in indenting text """

def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    
    Args:
    - text (str): The text to be printed
    
    Raises:
    - TypeError: If text is not a string
    
    Returns:
    - None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove spaces at the beginning of the text
    while text and text[0] == ' ':
        text = text[1:]

    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1

            # Remove spaces at the beginning of the next line
            while c < len(text) and text[c] == ' ':
                c += 1

            continue
        c += 1

    # Remove spaces at the end of the text
    while text and text[-1] == ' ':
        text = text[:-1]
