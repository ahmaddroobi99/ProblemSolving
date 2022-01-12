class Solution:
    def reorderSpaces(self, text: str) -> str:
        space = text.count(' ')                            # count how many space in total
        text = [word for word in text.split(' ') if word]  # split text to individual word in a list
        n = len(text)                                      # count total words
        if n == 1: return text[0] + space * ' '            # length == 1 is a special case, since no space in between only at the end
        avg, reminder = divmod(space, n-1)                 # get average space between words and spaces left (will be appended the end)
        return (' '*avg).join(text) + ' ' * reminder       # compose result