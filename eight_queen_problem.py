'''
Have the function f(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board. 
The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right).
Your program should determine if all of the queens are placed in such a way where none of them are attacking each other.
If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided.
For example, if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true.


Sample Test Cases:
Input:["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]
Output:"(2,1)"
Input:["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]
Output:"(5,3)"
'''

strArr = ["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]

def f(strArr):
    x = [[int(i) for i in p[1:-1].split(',')[0]] for p in strArr]
    y = [[int(i) for i in p[1:-1].split(',')[1]] for p in strArr]
    tupArr = []
    for i in range(len(strArr)):
        tupArr.append((x[i][0], y[i][0]))
    for i in range(len(strArr) - 1):
        for j in range(i + 1, len(strArr)):
            x1, y1 = tupArr[i]
            x2, y2 = tupArr[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                 return f'({x1}, {y1})'
    return 'true'

print(type(f(strArr)))
