import Alphabet
import Options
import Pipe
import MyLib
import Feature
import Instance
import Example
import torch

class Labeler:
    def __init__(self):
        self.nullkey = "-null-"
        self.unknownkey = "-unknown-"
        self.seperateKey = "#"
        self.m_featAlphabet = Alphabet.Alphabet()
        self.m_labelAlphabet =Alphabet.Alphabet()
        self.m_wordAlphabet = Alphabet.Alphabet()
        self.m_tagAlphabets = [] #里面元素是Alphabet类的对象
        self.m_options = Options.Option()
        self.m_pipe = Pipe.Pipe()
    ####LSTMCRFMLClassifier<cpu> m_classifier;

    def createAlphabet(self,vecInsts = []):
        '''
        vecInsts : vector<Instance>&
        :return:
        '''
        print("Creating Alphabet...")
        feature_stat = dict()#key:str,value:int
        word_stat = dict() #key:str,value:int
        tag_stat = list()# 元素是dict（key:str,value:int）
        self.m_labelAlphabet.clear()

        tagNum = len(vecInsts[0].tagfeatures[0])#表示有多少种tag，一般是bichar和trichar
        for i in range(tagNum):
            tag_stat[i] = dict()
            self.m_tagAlphabets.append(Alphabet.Alphabet())

        for numInstance in range(len(vecInsts)):
            pInstance = vecInsts[numInstance]
            words = pInstance.words
            labels = pInstance.labels
            sparsefeatures = pInstance.sparsefeatures
            tagfeatures = pInstance.tagfeatures
            assert len(tagfeatures) == tagNum


            for i in range(len(labels)):
                labelId = self.m_labelAlphabet.StrToId(labels[i])
                curword = MyLib.normalize_to_lowerwithdigit(words[i])
                if curword in word_stat:
                    word_stat[curword] += 1
                else:
                    word_stat[curword] = 1

                for one in sparsefeatures[i]:
                    if one in feature_stat:
                        feature_stat[one] += 1
                    else:
                        feature_stat[one] = 1
                for j in range(tagNum):
                    if tagfeatures[i][j] in tag_stat[j]:
                        tag_stat[j][tagfeatures[i][j]] += 1
                    else:
                        tag_stat[j][tagfeatures[i][j]] = 1

            if numInstance + 1 % self.m_options.verboseIter == 0:
                print(numInstance + 1 ,end = " ")
                if numInstance + 1 % (40 * self.m_options.verboseIter) == 0:
                    print()
            if self.m_options.maxInstance > 0 and numInstance == self.m_options.maxInstance:
                break

        print(numInstance ," " )
        print("Label num: " , self.m_labelAlphabet.size())
        print("Total word num: ",len(word_stat))
        print("Total feature num: ",len(feature_stat))
        print("tag num =", tagNum)
        for iter_tag in tagNum:
            print("Total tag ",iter_tag," num ",len(tag_stat[iter_tag]))

        self.m_featAlphabet.clear()
        self.m_wordAlphabet.clear()
        self.m_wordAlphabet.StrToId(self.nullkey)
        self.m_wordAlphabet.StrToId(self.unknownkey)

        for i in range(tagNum):
            self.m_tagAlphabets[i].clear()
            self.m_tagAlphabets[i].StrToId(self.nullkey)
            self.m_tagAlphabets[i].StrToId(self.unknownkey)

        for k,v in feature_stat.items():
            if v  > self.m_options.featCutOff:
                self.m_featAlphabet.StrToId(k)

        for k,v in word_stat.items():
            if not self.m_options.wordEmbFineTune or  v > self.m_options.wordCutOff:
                self.m_wordAlphabet.StrToId(k)

        for i in range(tagNum):
            for k,v in tag_stat[i].items():
                if not self.m_options.tagEmbFineTune or v > self.m_options.tagCutOff:
                    self.m_tagAlphabets[i].StrToId(k)


        print("Remain feature num: ",self.m_featAlphabet.size())
        print("Remain words num: ",self.m_wordAlphabet.size())
        for i in range(tagNum):
            print("Remain tag ",i," num ",self.m_tagAlphabets[i].size())

        self.m_labelAlphabet.set_fixed_flag(True)
        self.m_featAlphabet.set_fixed_flag(True)
        self.m_wordAlphabet.set_fixed_flag(True)

        for i in range(tagNum):
            self.m_tagAlphabets[i].set_fixed_flag(True)


    def extractFeature(self,feat = Feature.Feature(),pInstance = Instance.Instance(),idx = -1):
        feat.clear()

        words = feat.words
        sentsize = len(words)

        if idx >= 0 and idx < sentsize:
            curWord = MyLib.normalize_to_lowerwithdigit(words[idx])
        else:
            curWord = self.nullkey

        unknownId = self.m_wordAlphabet.from_str(self.unknownkey)
        curWordId = self.m_wordAlphabet.from_str(curWord)
        if curWordId >= 0:
            feat.words.append(curWordId)
        else:
            feat.words.append(unknownId)

        tagfeatures = pInstance.tagfeatures
        tagNum = len(tagfeatures[idx])

        for i in range(tagNum):
            unknownId = self.m_tagAlphabets[i].from_str(self.unknownkey)
            curTagId = self.m_tagAlphabets[i].from_str(tagfeatures[idx][i])
            if curTagId >= 0:
                feat.tags.append(curTagId)
            else:
                feat.tags.append(unknownId)
        linear_features = pInstance.sparsefeatures[idx]
        for one in linear_features:
            curFeatId = self.m_featAlphabet.from_str(one)
            if curFeatId >= 0:
                feat.linear_features.append(curFeatId)

    def convert2Example(self,pInstance = Instance.Instance(),exam = Example.Example()):
        exam.clear()
        labels = pInstance.labels
        curInstSize = len(labels)

        for i in range(curInstSize):
            orcale = labels[i]
            numLabels = self.m_labelAlphabet.size()

            curlabels = []
            for j in numLabels:
                if orcale == self.m_labelAlphabet.from_id(j):
                    curlabels.append(1)
                else:
                    curlabels.append(0)
            exam.m_labels.append(curlabels)
            feat = Feature.Feature()

            self.extractFeature(feat,pInstance,i)
            exam.m_features.append(feat)


    def initialExamples(self,vecInsts = [],vecExams = []):
        '''
        :param vecInsts:vector<Instance>&
        :param vecExams:vector<Example>&
        :return:
        '''
        for numInstance in range(len(vecInsts)):
            pInstance = vecInsts[numInstance]
            curExam = Example.Example()
            self.convert2Example(pInstance,curExam)
            vecExams.append(curExam)
            if numInstance + 1 % self.m_options.verboseIter == 0:
                print(numInstance + 1," ", end="")
                if numInstance + 1 % (40 * self.m_options.verboseIter) == 0:
                    print()
            if self.m_options.maxInstance > 0 and numInstance == self.m_options.maxInstance:
                break
        print(numInstance, " ")


    def train(self,trainFile,devFile,testFile,optionFile):
        if optionFile != "":
           self.m_options.load(optionFile)
        self.m_options.showOptions()

        trainInsts = list() # vector<Instance>
        devInsts = list()
        testInsts = list()
        decodeInstResults = list() #vector<Instance>
        curDecodeInst = Instance.Instance()
        bCurIterBetter = False

        self.m_pipe.readInstance(trainFile,trainInsts, self.m_options.maxInstance)
        self.m_pipe.readInstance(devFile,devInsts, self.m_options.maxInstance)
        self.m_pipe.readInstance(testFile, testInsts, self.m_options.maxInstance)

        self.createAlphabet(trainInsts)




if __name__ == "__main__":
    test = Labeler()
    test.train("","","","")
    # x = torch.Tensor(3,5)
    # print(x)

























