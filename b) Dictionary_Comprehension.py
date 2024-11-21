
s = "DataScience"

ascii_value = {
    char: 65 + (ord(char) - ord('A')) 
    if 'A' <= char <= 'Z' 
    else 97 + (ord(char) - ord('a')) 
    for char in s
}

print(ascii_value)