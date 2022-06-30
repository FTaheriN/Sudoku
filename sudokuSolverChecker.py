import datetime


def row_check(puzzle , row_num , column_num , number):
    for i in range (0,9):
        if puzzle[row_num][i] == number and i != column_num:
            return False
    return True


def column_check(puzzle , row_num , column_num , number):
    for i in range (0,9):
        if puzzle[i][column_num] == number and i != row_num:
            return False
    return True    


def grid_check(puzzle , row_num , column_num , number):
    row_i = row_num // 3
    column_j = column_num //3
    for i in range (row_i*3 , row_i*3 +3):
        for j in range (column_j*3 , column_j*3 +3):
           if puzzle[i][j] == number and i != row_num and j != column_num:
            return False
    return True     


def is_valid(puzzle , row_num , column_num , number):
    if row_check(puzzle , row_num , column_num , number):
        if column_check(puzzle , row_num , column_num , number):
            if grid_check(puzzle, row_num , column_num , number):
                return True
    return False

def find_empty(puzzle , empty):
    for i in range (0,9):
        for j in range (0,9):
            if puzzle[i][j] == 0:
                empty[0] = i
                empty[1] = j
                return True
    return False


def solver(puzzle):
    empty = [0,0]
    if not (find_empty(puzzle,empty)):
        return True
   
    
    emp_i = empty[0]
    emp_j = empty[1]

    for k in range(1,10):
        if is_valid(puzzle , emp_i , emp_j , k):
            puzzle[emp_i][emp_j] = k
            if solver(puzzle):
                return True
        
        puzzle[emp_i][emp_j] = 0

    return False


def checker(puzzle):
    for i in range (0,9):
        for j in range (0,9):
            if puzzle[i][j] >=1 and puzzle[i][j] <=9:
                if not(is_valid(puzzle, i, j, puzzle[i][j])):
                    print("not valid!")
                    return False
    print("valid***")
    return True


def print_grid(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j] , end=" ")
        print()


def main():
    puzzle=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 
    
    if solver(puzzle):
        print_grid(puzzle)
    else:
        print("not valid")


main()
# def main():
#     puzzle=[[1, 4, 5, 3, 2, 7, 6, 9, 8],
#             [8, 3, 9, 6, 5, 4, 1, 2, 7],
#             [6, 7, 2, 9, 1, 8, 5, 4, 3],
#             [4, 9, 6, 1, 8, 5, 3, 7, 2],
#             [2, 1, 8, 4, 7, 3, 9, 5, 6],
#             [7, 5, 3, 2, 9, 6, 4, 8, 1],
#             [3, 6, 7, 5, 4, 2, 8, 1, 9],
#             [9, 8, 4, 7, 6, 1, 2, 3, 5],
#             [5, 2, 1, 8, 3, 9, 7, 6, 4]]
    
#     print(datetime.datetime.now())

#     if checker(puzzle):
#         print_grid(puzzle)
#     else:
#         print("not valid")
    
#     print(datetime.datetime.now())


# main()

