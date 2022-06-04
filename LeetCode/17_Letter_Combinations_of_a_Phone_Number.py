from collections import deque
def letterCombinations(digits):
    d = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    q = deque(d[digits[0]])
    print(q)
    # print(len(digits))
    for i in range(1, len(digits)):
        s = len(q)
        while s:
            out = q.popleft()
            # print(out)
            # print(q)
            for j in d[digits[i]]:
                q.append(out + j)
            s -= 1
    return q

    




digits = "23"
output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# digits = ""
output = []
# digits = "2"
output = ["a", "b", "c"]

print(letterCombinations(digits))

# Time complexity: O(4^n * n) where n is the length of the digits. 
# Space complexity: O(n) where n is the length of digits


def letterCombinations(digits):
    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0: 
        return []
    
    # Map all the digits to their corresponding letters
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
    def backtrack(index, path):
        # If the path is the same length as digits, we have a complete combination
        if len(path) == len(digits):
            combinations.append("".join(path))
            return # Backtrack
        
        # Get the letters that the current digit maps to, and loop through them
        possible_letters = letters[digits[index]]
        for letter in possible_letters:
            # Add the letter to our current path
            path.append(letter)
            # Move on to the next digit
            backtrack(index + 1, path)
            # Backtrack by removing the letter before moving onto the next
            path.pop()

    # Initiate backtracking with an empty path and starting index of 0
    combinations = []
    backtrack(0, [])
    return combinations