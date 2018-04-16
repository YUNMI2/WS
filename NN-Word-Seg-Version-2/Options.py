class Option:
    def __init__(self):
        self.wordCutOff = 0
        self.featCutOff = 0
        self.charCutOff = 0
        self.tagCutOff = 0
        self.initRange = 0.01
        self.maxIter = 200
        self.batchSize = 1 
        self.maxIter = 1000
        
        self.adaEps = 1e-6
        self.adaAlpha = 0.01
        self.regParameter = 1e-8
        self.dropProb = 0.0
        
        self.linearHiddenSize = 30
        self.hiddenSize = 200
        self.rnnHiddenSize = 300
        self.wordEmbSize = 50
        self.wordcontext = 2
        self.wordEmbFineTune = 1
        self.tagEmbSize = 50
        self.tagEmbFineTune = 1
        self.charEmbSize = 50
        self.charcontext = 2
        self.charEmbFineTune = 1
        self.charhiddenSize = 50
        self.verboseIter = 100
        self.saveIntermediate = 1
        self.train = 0

        self.maxInstance = -1
        self.outBest = ""
        self.relu = 0
        self.seg = 0
        self.atomLayers = 1
        self.rnnLayers = 1

    def setOptions(self,optionLineList):
        for line in optionLineList:
            line = line.strip()
            if not line:
                continue
            
            [pair_first,pair_second] = line.split("=")
            
            pair_first = pair_first.strip()
            pair_second = pair_second.strip()

            if pair_first == "wordCutOff":
                self.wordCutOff = int(pair_second)
            if pair_first == "featCutOff":
                self.featCutOff = int(pair_second)
            if pair_first == "charCutOff":
                self.charCutOff = int(pair_second)
            if pair_first == "tagCutOff":
                self.tagCutOff = int(pair_second)
            if pair_first == "initRange":
                self.initRange = float(pair_second)
            if pair_first == "maxIter":
                self.maxIter = int(pair_second)
            if pair_first == "batchSize":
                self.batchSize = int(pair_second)
            if pair_first == "adaEps":
                self.adaEps = float(pair_second)
            if pair_first == "adaAlpha":
                self.adaAlpha = float(pair_second)
            if pair_first == "regParameter":
                self.regParameter = float(pair_second)
            if pair_first == "dropProb":
                self.dropProb = float(pair_second)
            if pair_first == "linearHiddenSize":
                self.linearHiddenSize = int(pair_second)
            if pair_first == "hiddenSize":
                self.hiddenSize = int(pair_second)
            if pair_first == "rnnHiddenSize":
                self.rnnHiddenSize = int(pair_second)
            if pair_first == "wordcontext":
                self.wordcontext = int(pair_second)
            if pair_first == "wordEmbSize":
                self.wordEmbSize = int(pair_second)
            if pair_first == "wordEmbFineTune":
                self.wordEmbFineTune = int(pair_second) #0表示false,1表示true
            if pair_first == "tagEmbSize":
                self.tagEmbSize = int(pair_second)
            if pair_first == "tagEmbFineTune":
                self.tagEmbFineTune = int(pair_second) #0表示false,1表示true
            if pair_first == "charcontext":
                self.charcontext = int(pair_second) #0表示false,1表示true
            if pair_first == "charEmbSize":
                self.charEmbSize = int(pair_second)
            if pair_first == "charEmbFineTune":
                self.charEmbFineTune = int(pair_second) #0表示false,1表示true
            if pair_first == "charhiddenSize":
                self.charhiddenSize == int(pair_second)
            if pair_first == "verboseIter":
                self.verboseIter = int(pair_second)
            if pair_first == "train":
                self.train = int(pair_second)
            if pair_first == "saveIntermediate":
                self.saveIntermediate = int(pair_second)
            if pair_first == "maxInstance":
                self.maxInstance = int(pair_second)
            if pair_first == "outBest":
                self.outBest = int(pair_second)
            if pair_first == "seg":
                self.seg = int(pair_second)
            if pair_first == "atomLayers":
                self.atomLayers = int(pair_second)
            if pair_first == "rnnLayers":
                self.rnnLayers = int(pair_second)


    def showOptions(self):
        print("wordCutOff = ", self.wordCutOff)
        print("featCutOff = ", self.featCutOff)
        print("charCutOff = ", self.charCutOff)
        print("tagCutOff = ", self.tagCutOff)
        print( "initRange = " , self.initRange)
        print( "maxIter = " , self.maxIter)
        print( "batchSize = " , self.batchSize)
        print( "adaEps = " , self.adaEps)
        print( "adaAlpha = ", self.adaAlpha)
        print( "regParameter = ", self.regParameter)
        print( "dropProb = ", self.dropProb)

        print( "linearHiddenSize = ", self.linearHiddenSize)
        print( "hiddenSize = ", self.hiddenSize)
        print( "rnnHiddenSize = ", self.rnnHiddenSize)
        print( "wordcontext = ", self.wordcontext)
        print( "wordEmbFineTune = ", self.wordEmbFineTune)
        print( "tagEmbSize = ", self.tagEmbSize)
        print( "tagEmbFineTune = ", self.tagEmbFineTune)
        print( "charEmbSize = ", self.charEmbSize)
        print( "charcontext = ", self.charcontext)
        print( "charEmbFineTune = ", self.charEmbFineTune)
        print( "charhiddenSize = ", self.charhiddenSize)

        print( "verboseIter = ", self.verboseIter)
        print( "saveItermediate = ", self.saveIntermediate)
        print( "maxInstance = ", self.maxInstance)

        print( "outBest = ", self.outBest)
        print( "relu = ", self.relu)
        print( "seg = ", self.seg)
        print( "atomLayers = ", self.atomLayers)
        print( "rnnLayers = ", self.rnnLayers)

    def load(self,optionfile):
        with open(optionfile, "r",encoding = "utf-8") as fo:
            line_list = [line for line in fo.readlines()]
        self.setOptions(line_list)

    def writeModel(self, modelOptionFile):
        with open(modelOptionFile, "w", encoding = "utf-8") as fw:
            fw.write("wordCutOff = " + str(self.wordCutOff) + "\n")
            fw.write("featCutOff = " + str(self.featCutOff) + "\n")
            fw.write("charCutOff = " + str(self.charCutOff) + "\n")
            fw.write("tagCutOff = " + str(self.tagCutOff) + "\n")
            fw.write("initRange = " + str(self.initRange) + "\n")
            fw.write("maxIter = " + str(self.maxIter) + "\n")
            fw.write("batchSize = " + str(self.batchSize) + "\n")
            fw.write("adaEps = " + str(self.adaEps) + "\n")
            fw.write("adaAlpha = " + str(self.adaAlpha) + "\n")
            fw.write("regParameter = " + str(self.regParameter) + "\n")
            fw.write("dropProb = " + str(self.dropProb) + "\n")

            fw.write("linearHiddenSize = " + str(self.linearHiddenSize) + "\n")
            fw.write("hiddenSize = " + str(self.hiddenSize) + "\n")
            fw.write("rnnHiddenSize = " + str(self.rnnHiddenSize) + "\n")
            fw.write("wordcontext = " + str(self.wordcontext) + "\n")
            fw.write("wordEmbFineTune = " + str(self.wordEmbFineTune) + "\n")
            fw.write("tagEmbSize = " + str(self.tagEmbSize) + "\n")
            fw.write("tagEmbFineTune = " + str(self.tagEmbFineTune) + "\n")
            fw.write("charEmbSize = " + str(self.charEmbSize) + "\n")
            fw.write("charcontext = " + str(self.charcontext) + "\n")
            fw.write("charEmbFineTune = " + str(self.charEmbFineTune) + "\n")
            fw.write("charhiddenSize = " + str(self.charhiddenSize) + "\n")

            fw.write("verboseIter = " + str(self.verboseIter) + "\n")
            fw.write("saveItermediate = " + str(self.saveIntermediate) + "\n")
            fw.write("maxInstance = " + str(self.maxInstance) + "\n")

            fw.write("outBest = " + str(self.outBest) + "\n")
            fw.write("relu = " + str(self.relu) + "\n")
            fw.write("seg = " + str(self.seg) + "\n")
            fw.write("atomLayers = " + str(self.atomLayers) + "\n")
            fw.write("rnnLayers = " + str(self.rnnLayers) + "\n")


if __name__ == "__main__":
    test = Option()
    test.showOptions()


            
            


            
            

            
