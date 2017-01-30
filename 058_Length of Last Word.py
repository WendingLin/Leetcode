#58.Length of Last Word
def lengthOfLastWord(s):
    return len(s.rstrip(" "))-s.rstrip(" ").rfind(" ")-1
print(lengthOfLastWord("a "))
