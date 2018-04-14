import MyLib

class Instance:
    def __init__(self):
        self.labels = []
        self.words = []
        self.tagfeatures = []
        self.sparsefeatures = []

    def size(self):
        return len(self.words)

    def clear(self):
        self.words.clear()
        self.labels.clear()
        self.tagfeatures.clear()
        self.sparsefeatures.clear()

    def copyValuesFrom(self,one_instance):
        self.clear()
        for i in range(one_instance.size()):
            self.words.append(one_instance.words[i])
            self.labels.append(one_instance.labels[i])
            for j in range(len(one_instance.tagfeatures)):#不直接appendlist，防止浅拷贝
                tmp_list = one_instance.tagfeatures[j]
                self.tagfeatures.append(tmp_list)
            for j in range(len(one_instance.sparsefeatures)):#不直接appendlist，防止浅拷贝
                tmp_list = one_instance.sparsefeatures[j]
                self.sparsefeatures.append(tmp_list)

    def assignLabel(self, resultd_labels_stringList):
        assert (len(resultd_labels_stringList) == len(self.words))
        self.labels.clear()
        self.labels.extend(resultd_labels_stringList)#这边应该是每个位置赋予一个确定的标签，而不是一个标签集合

    def SegEvaluate(self,resultd_labels,evalu):
        '''
        :param resultd_labels: list<string>
        :param eval: 评价类
        :return:
        '''
        idx =0
        idy = 0
        endpos = 0
        golds = set()
        while idx < len(self.labels):#这边是处理答案
            if MyLib.is_start_label(self.labels[idx]):#如果idx位置是词的开头
                idy = idx
                endpos = -1
                while idy < len(self.labels):
                    if not MyLib.is_continue_label(self.labels[idy], self.labels[idx], idy - idx):
                        endpos = idy - 1
                        break
                    endpos = idy
                    idy += 1

                str_start_to_end = "[" + str(idx) + "," + str(idy) + "]"
                golds.add(MyLib.cleanLabel(MyLib.cleanLabel(self.labels[idx]) + str_start_to_end))
                idx = endpos
            idx += 1

        preds = set()
        while idx < len(resultd_labels):  # 这边是处理答案
            if MyLib.is_start_label(resultd_labels[idx]):  # 如果idx位置是词的开头
                idy = idx
                endpos = -1
                while idy < len(self.labels):
                    if not MyLib.is_continue_label(resultd_labels[idy], resultd_labels[idx], idy - idx):
                        endpos = idy - 1
                        break
                    endpos = idy
                    idy += 1

                str_start_to_end = "[" + str(idx) + "," + str(idy) + "]"
                preds.add(MyLib.cleanLabel(MyLib.cleanLabel(resultd_labels[idx]) + str_start_to_end))
                idx = endpos
            idx += 1
        evalu.overall_label_count += len(golds)
        evalu.predicated_label_count += len(preds)
        for one in preds:
            if one in golds:
                evalu.correct_label_count += 1






if __name__ == "__main__":
    print(1)


            
            


            
            

            
