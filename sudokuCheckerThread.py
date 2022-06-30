from threading import Thread
import queue
import datetime

def check_set(arr):
    if set([1,2,3,4,5,6,7,8,9]) == set(arr):
        return True
    return False


def row_check(puzzle , q):
    row = []
    for i in range (len(puzzle)):
        for j in range (len(puzzle[0])):
            row.append(puzzle[i][j])
        if not(check_set(row)):
            q.put(False)
            return
        row.clear()
    q.put(True)
    return

                
def column_check(puzzle , q):
    col = []
    for i in range (len(puzzle)):
        for j in range (len(puzzle[0])):
            col.append(puzzle[j][i])
        if not(check_set(col)):
            q.put(False)
            return
        col.clear()
    q.put(True)
    return


def grid_check(puzzle , row , col , q):
    block = []
    for row_i in range(row,row + 3):
        for col_j in range(col , col + 3):
            block.append(puzzle[row_i][col_j])
    if not(check_set(block)):
        q.put(False)
        return
    q.put(True)
    return


def checker(puzzle):
    q = queue.Queue()

    row_thread = Thread(target=row_check, args=(puzzle, q))
    row_thread.start()

    columns_thread = Thread(target=column_check, args=(puzzle, q))
    columns_thread.start()

    grid_threads = []
    for row in range(0,9,3):
        for col in range (0,9,3):
            t = Thread(target=grid_check, args=(puzzle , row , col , q))
            t.start()
            grid_threads.append(t)

    row_thread.join()
    columns_thread.join()

    [t.join() for t in grid_threads]

    results = []
    while not q.empty():
        results.append(q.get())

    return all(results)


def main():
    valid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    
    print("Startig time:")
    print(datetime.datetime.now())

    if checker(valid):
        print("valid input")
    else:
        print("invalid input")

    print("Ending time:")
    print(datetime.datetime.now())

    invalid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 8, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]]
               
    print("Startig time:")
    print(datetime.datetime.now())

    if checker(invalid):
        print("valid input")
    else:
        print("invalid input")

    print("Ending time:")
    print(datetime.datetime.now())


main()