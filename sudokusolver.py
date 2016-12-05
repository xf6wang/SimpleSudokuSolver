matrix = [ [0, 8, 4, 0, 0, 0, 2, 6, 0],                                                                                                                               
           [0, 0, 1, 0, 8, 2, 0, 0, 0],                                                                                                                                                   
           [0, 0, 0, 0, 0, 9, 0, 0, 0],                                                                                                                               
           [3, 4, 0, 0, 0, 1, 8, 2, 0],                                                                                                                                
           [1, 0, 0, 0, 2, 0, 0, 0, 3],                                                                                                                            
           [0, 2, 9, 8, 0, 0, 0, 7, 4],                                                                                                                                
           [0, 0, 0, 5, 0, 0, 0, 0, 0],                                                                                                                                
           [0, 0, 0, 9, 4, 0, 3, 0, 0],                                                                                                                                
           [0, 9, 5, 0, 0, 0, 4, 8, 0] ]        
       
def findNext(copyMatrix):                                                                                                                                                      	 
    for y in range(9):
	    for x in range(9):
	    	if copyMatrix[y][x] == 0:
		    	return (y, x)
    return (-1, -1)  
	

def ThreebyThreeLookup (num, y, x, copyMatrix):
    xFloor = 3 * int(x/3)
    yFloor = 3 * int(y/3)
    for m in range (3):
        for n in range(3):
            if copyMatrix[yFloor + m][xFloor + n] == num:
                return True
            
    return False;

def isValid(num, y, x, copyMatrix):
    for n in range(9):
        if copyMatrix[y][n] == num:
            return False
    for m in range(9):
	    if copyMatrix[m][x] == num:
	        return False 
    if ThreebyThreeLookup(num, y, x, copyMatrix):
        return False
    return True


def Solve(matrix):
   location = findNext(matrix)
   if location == (-1, -1):
       return True
   else:
       for q in range (9):
           if isValid(q + 1, location[0], location[1], matrix):
               matrix[location[0]][location[1]] = q + 1
               if Solve(matrix):
                   return True
               matrix[location[0]][location[1]] = 0
       return False

def printMatrix(matrix):
    for x in range(9):
        print(matrix[x])

printMatrix(matrix)
Solve(matrix)
printMatrix(matrix)
