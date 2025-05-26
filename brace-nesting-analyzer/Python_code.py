# Name: Naresh Khanal
# OS: Windows 11
# Python Version: Python 3.12.0

# Open the input.txt file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Set up the variables.
depth = 0
inside_string = False
inside_block_comment = False

# Analyze every line.
for line in lines:
    i = 0
    single_line_comment = False
    while i < len(line):
        char = line[i]

        # Check for start of block comment (/*)
        if not inside_string and not inside_block_comment and not single_line_comment:
            if char == '/' and i + 1 < len(line) and line[i + 1] == '*':
                inside_block_comment = True
                i += 2
                continue

        # Check for end of block comment (*/)
        if inside_block_comment:
            if char == '*' and i + 1 < len(line) and line[i + 1] == '/':
                inside_block_comment = False
                i += 2
                continue
            i += 1
            continue

        # Check for start of single-line comment (//)
        if not inside_string and not inside_block_comment:
            if char == '/' and i + 1 < len(line) and line[i + 1] == '/':
                single_line_comment = True
                break

        # Toggle string mode if a double quote is found
        if not inside_block_comment and not single_line_comment:
            if char == '"':
                inside_string = not inside_string

        # Count braces only outside of strings and comments
        if not inside_string and not inside_block_comment and not single_line_comment:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth < 0:
                    print("Warning: Extra closing '}' found.")
                    depth = 0

        i += 1

    # Print the current depth and line
    print(depth, line.rstrip())

# Final check for unmatched opening braces
if depth != 0:
    print("Warning: Unmatched '{' found at end of file.")
    depth = 0  # Reset depth to 0 so it ends cleanly
