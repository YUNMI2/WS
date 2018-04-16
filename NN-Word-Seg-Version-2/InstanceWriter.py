import Instance
class InstanceWriter:
        def write(self,pInstance = Instance.Instance(),outputfile_name = ""):
            '''
            :param pInstance:pInstance:Instance 类的对象
            :param outputfile_name:
            :return:
            '''
            if outputfile_name == "":
                return -1
            with open(outputfile_name, "a",encoding = "utf-8") as fw:
                for i in range(len(pInstance.labels)):
                    fw.write(pInstance.words[i] + " " + pInstance.labels[i] + "\n")

                fw.write("\n")
            return 0





if __name__ == "__main__":
    test_file_name = "test.out"
    testInstance = Instance.Instance()
    testInstance.labels = ["B","I","E"]
    testInstance.words = ["中","国","人"]
    test_Writer = InstanceWriter()
    test_Writer.write(testInstance,test_file_name)
