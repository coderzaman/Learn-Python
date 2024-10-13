# 1. Single-Line Comments
# This is a single-line comment

# 2. Multi-Line Comments(Not Recommended)

# Approach 1: Multiple Single-Line Comments
# This is a multi-line comment.
# It spans several lines.
# Each line starts with a hash symbol.


# Approach 2: Multi-Line Strings (Not Recommended for Comments)
"""
This is a multi-line string,
not a true comment.
It can be used as a comment,
but it's intended for docstrings.
"""

# 3. Docstrings
# Definition:
# Docstrings (documentation strings) are multi-line comments used to document modules, classes, functions, and methods.
# Unlike regular comments, docstrings are accessible at runtime via the __doc__ attribute and are used by documentation tools.

def greet(name):
    """
    Greet the user by name.

    Parameters:
    name (str): The name of the user.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

print(greet.__doc__)

