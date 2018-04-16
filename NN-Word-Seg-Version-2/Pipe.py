import Instance
import copy

class Pipe:
    def outputAllInstance(self,file_name,vecInstances):
        '''
        :param file_name:文件名
        :param vecInstances: 实例的list
        :return:直接修改vecInstance
        '''
        if file_name == "":
            print("load file error!,please check!")
            exit()

        with open(file_name, "w",encoding = "utf-8") as fw:
            for i in range(len(vecInstances)):
                for j in range(len(vecInstances[i].labels)):
                    #conll格式的写
                    fw.write(vecInstances[i].words[j] + "\t" + vecInstances[i].labels[j] + "\n")
                fw.write("\n")



    def readInstance(self,m_strInfile,vecInstances = [],maxInstance = -1):
        '''
        :param m_strInfile:输入的文件名
        :param vecInstances:list 元素是instance
        :param maxInstance: 最大的实例个数
        :return:
        '''
        vecInstances.clear()

        if m_strInfile == "":
            print("load input file error,please check!")
            exit()
        with open(m_strInfile,"r",encoding = "utf-8") as fo:
            one_instance = Instance.Instance()
            for line in fo.readlines():
                line = line.strip()
                if not line :
                    if one_instance.size() > 0:
                        vecInstances.append(one_instance)
                        one_instance.clear()
                line_list = line.split()

                one_instance.words.append(line_list[0])
                one_instance.labels.append(line_list[-1])
                for one in line_list:
                    if one.startswith("[S]"):
                        one_instance.sparsefeatures.append(one)
                    if one.startswith("[T"):
                        one_instance.tagfeatures.append(one)

            if one_instance.size() > 0:
                vecInstances.append(one_instance)
                one_instance.clear()










