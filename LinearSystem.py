class LinearSystem():
    #Creating important variables:
    def __init__(self, coeficientMatrix):
        self.coeficientMatrix = coeficientMatrix
        self.pivotsCoordinates = []
        self.freeVariables = []

    #Introducing zeros inside the matrix:
    def simplifySystem(self, iPivot, jPivot):
        #For each collumn (i) of the matrix:
        for i in range(len(self.coeficientMatrix)-1):
            #For each line (j) of the collumn:
            for j in range(len(self.coeficientMatrix[i])):
                #If this element belongs to the pivot collumn and if it`s not the pivot:
                if j != jPivot and i == iPivot and i != len(self.coeficientMatrix):
                    #Calculate a variable k that turns this element to a zero:
                    k = -(self.coeficientMatrix[i][j] / self.coeficientMatrix[iPivot][jPivot])
                    #Use this k to change all the elements in the line:
                    collumn = 0
                    while collumn < len(self.coeficientMatrix):
                        self.coeficientMatrix[collumn][j] += self.coeficientMatrix[collumn][jPivot]*k
                        collumn += 1

    def returnPivotCoordinates(self, j):
        jLine = []
        #For each collumn (i) of the matrix:
        for collumn in self.coeficientMatrix:
            #Store the elements in the j line of that matrix in a list: 
            jLine.append(collumn[j])
        #Find the first element in that line diferent from 0:
        PivotCoordinates = "None"
        i = 0
        while i < len(self.coeficientMatrix) and PivotCoordinates == "None":
            if jLine[i] != 0:
                PivotCoordinates  = [i,j,jLine[i]]
            i += 1
        #Return the coordinates of that Pivot:
        return PivotCoordinates
        

        
    #Scalonating the matrix:
    def scalonate(self):
        #For each collumn (i) of the matrix:
        for i in range(len(self.coeficientMatrix)):
            #For each line (j) of the collumn:
            for j in range(len(self.coeficientMatrix[i])):
                iPivot = LinearSystem.returnPivotCoordinates(self, j)[0]
                #iPivot = returnPivotCoordinates(j)[0]
                jPivot = LinearSystem.returnPivotCoordinates(self, j)[1]
                #jPivot = returnPivotCoordinates(j)[1]
                if ["Pivot = " + str(self.coeficientMatrix[iPivot][jPivot]), iPivot, jPivot] not in self.pivotsCoordinates:
                    self.pivotsCoordinates += [["Pivot = " + str(float(self.coeficientMatrix[iPivot][jPivot])), iPivot, jPivot]]
                LinearSystem.simplifySystem(self, iPivot, jPivot)

    def getMatrix(self):
        return self.coeficientMatrix

    def printMatrix(self):
        #For each collumn (i) of the matrix:
        for i in range(len(self.coeficientMatrix)):
            #For each line (j) of the collumn:
            for j in range(len(self.coeficientMatrix[i])):
                print()

    
                    
                    
                
        
