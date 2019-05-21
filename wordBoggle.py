'''
Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words, find all the possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell twice in one word.

Example

For

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
wordBoggle(board, words) = ["CODE", "RULES"].

Example

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char board

A two-dimensional array of uppercase English characters representing a rectangular Boggle board.

Guaranteed constraints:
2 ≤ board.length ≤ 4,
2 ≤ board[i].length ≤ 4,
'A' ≤ board[i][j] ≤ 'Z'.

[input] array.string words

An array of unique English words composed only of uppercase English characters.

Guaranteed constraints:
0 ≤ words.length ≤ 100,
2 ≤ words[i].length ≤ 16,
'A' ≤ words[i][j] ≤ 'Z'.

[output] array.string

Words from words that can be found on the Boggle board without duplicates and sorted lexicographically in ascending order.
[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

Input:
board: [["R","L","D"], 
 ["U","O","E"], 
 ["C","S","O"]]
words: ["CODE", 
 "SOLO", 
 "RULES", 
 "COOL"]
Expected Output:
["CODE", 
 "RULES"]

'''

from copy import deepcopy
def wordBoggle(board, words):
    sol=[]
    completedWords=set()
    for word in words:
        #print(completedWords)
        if(word in completedWords):
            continue
        output=None
        for i in range(0,len(board)):
            if(output==word):
                break
            for j in range(0,len(board[i])):
                if(output==word):
                    break
                if(board[i][j]==word[0]):
                    visited=[[0]*len(board[0]) for i in range(len(board)) ]
                    visited[i][j]=1
                    output=wordBoggleHelper(board, word, sol, i, j, word[0], 1, visited, completedWords)
    return sorted(sol)

def wordBoggleHelper(board, word, sol, height, width, string, position, visited, completedWords):   
    #base case
    if(position==len(word)):
        if(word not in completedWords):
            sol.append(string)
        completedWords.add(string)
        return string
    else:
        next_char=word[position]
    #recursive dfs
    for i in range(height-1, height+2):
        if(len(board)<i+1 or i<0):
                continue
        for j in range(width-1, width+2):
            if(len(board)<i+1 or len(board[i])<j+1 or j<0):
                continue
            #temp_char=board[i][j]
            #if(board[i][j]==board[i][j]):
            if(board[i][j]==next_char):
                if(visited[i][j]==0):
                    copy_visited=deepcopy(visited)
                    copy_visited[i][j]=1
                    wordBoggleHelper(board, word, sol, i, j, string+word[position], position+1, copy_visited, completedWords)
    return None
# board= [["R","L","D"], 
#  ["U","O","E"], 
#  ["C","S","O"]]
# words= ["CODE", 
#  "SOLO", 
#  "RULES", 
#  "COOL"]
# ExpectedOutput=["CODE", 
#  "RULES"]


# board= [["A","X","V","W"], 
#  ["A","L","T","I"], 
#  ["T","T","J","R"]]
# words= ["AXOLOTL", 
#  "TAXA", 
#  "ABA", 
#  "VITA", 
#  "VITTA", 
#  "GO", 
#  "AXAL", 
#  "LATTE", 
#  "TALA", 
#  "RJ"]
# ExpectedOutput=["AXAL", 
#  "RJ", 
#  "TALA", 
#  "TAXA", 
#  "VITTA"]

board=[["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]]
words=["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]

ExpectedOutput=["aabbbbabbaababaaaabababbaaba","abaabbbaaaaababbbaaaaabbbaab","ababaababaaabbabbaabbaabbaba"]

import datetime
start=datetime.datetime.now()
output=wordBoggle(board, words)
end=datetime.datetime.now()
duration=end-start
print(duration)
print(output)
print(output==ExpectedOutput)
print(len(words))
print(len(output))