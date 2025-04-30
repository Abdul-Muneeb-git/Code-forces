def minimize_string_length(s):
    s = list(s)  # Convert string to list for easier manipulation
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            # Perform the operation: replace s[i] and remove s[i+1]
            s[i] = 'a'  # Replace with any character (e.g., 'a')
            s.pop(i + 1)  # Remove the next character
            # Reset i to 0 to recheck the string from the beginning
            i = 0
        else:
            i += 1
    return len(s)

# Input reading and processing
t = int(input())  # Number of test cases
for _ in range(t):
    s = input().strip()  # Read the string
    print(minimize_string_length(s))
