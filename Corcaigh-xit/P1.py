
# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------




# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
#The submission confirmation number is 93f64951-b7fb-4ef8-a28e-05ea1518285a. 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start: Improt Library ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np
import sys, getopt
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End: Import Library ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start:  Create Mine Map ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createMineMap (X,Y, mineList):
    mineMap = np.zeros((int(X),int(Y)))
    
    for mine in mineList:
        mineMap[mine[0]][mine[1]] =-1
    
    print(mineMap)
    
    return mineMap
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End:  Create Mine Map ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start:  To find Neighbors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def neighbors (rowCount, colCount,rowIndex, colIndex):
        
    X = int(rowCount)-1
    Y = int(colCount)-1
    
    neighborsList = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                                   for y2 in range(y-1, y+2)
                                   if (-1 < x <= X and
                                       -1 < y <= Y and
                                       (x != x2 or y != y2) and
                                       (0 <= x2 <= X) and
                                       (0 <= y2 <= Y))]
                                   
    return neighborsList(rowIndex,colIndex)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End:   To find Neighbors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start:~Get Mine Locations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getMineLocation (filePath):
    X=0
    Y=0
    x=y=0
    MineList = []
    flagMatrixResolution = True
    with open(filePath, 'r') as mineFile:
        for line in mineFile:
            if(flagMatrixResolution):
                l = line.split()
                X= l[0]
                Y= l[1]
                flagMatrixResolution = False
                continue
            
            y=0
            for word in line.split(' '):    
                if 'x' in word:
                    MineList.append((x,y))
                y=y+1
                
            x=x+1   
    print('MineList' , MineList)                          
    return X,Y,MineList

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End:Get Mine Locations  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start: Reading Input ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
         
   return inputfile , outputfile
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End: Reading Input~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start: Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    
    inputPath, outputPath=  main(sys.argv[1:])
    
    noOfRow, noOfCol,mineList = getMineLocation(inputPath)
    
    mineMap = createMineMap(noOfRow,noOfCol,mineList )
    
    rowIndex =0
    colIndex =0
    
    while rowIndex < int(noOfRow):
        colIndex =0
        while colIndex < int(noOfCol):
            if mineMap[rowIndex][colIndex] == -1:
                colIndex += 1
                continue
            neighborsList = neighbors(noOfRow,noOfCol,rowIndex, colIndex)
            mineCount =0
            for cell in neighborsList:
                if(mineMap[cell[0]][cell[1]]) == -1:
                    mineCount+=1
            mineMap[rowIndex][colIndex] = mineCount
            colIndex+=1
        rowIndex+=1
        
    print('enc')
    
    with open(outputPath, 'w') as f:
        for item in mineMap.tolist():
            item = [int(w) for w in item]
            item = [str(w).replace('-1', 'X') for w in item]
            print(item)
            
            f.write("%s\n" % str((item)))

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ End: Main~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~