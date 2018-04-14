class Metric:
    def __init__(self):
        self.overall_label_count = 0
        self.predicated_label_count = 0
        self.correct_label_count = 0

    def reset(self):
        self.overall_label_count = 0
        self.predicated_label_count = 0
        self.correct_label_count = 0

    def bIdentical(self):
        if self.predicated_label_count == 0:
            if self.overall_label_count == self.correct_label_count:
                return True
            return False
        elif self.overall_label_count == self.correct_label_count and self.predicated_label_count == self.correct_label_count:
                return True

        return False




    def getAccuracy(self):
        if self.predicated_label_count == 0:
            return self.correct_label_count / self.overall_label_count
        else:
            return self.correct_label_count * 2 / (self.overall_label_count + self.predicated_label_count)

    def showAccuracy(self):
        if self.predicated_label_count == 0:
            print("Accuracy:\tP=" + str(self.correct_label_count) + "/" + str(self.overall_label_count)  + " = " + str(self.correct_label_count / self.overall_label_count) )
        else:
            print("R:\t" + str(self.correct_label_count) + "/" + str(self.overall_label_count)   + "=" + str(self.correct_label_count*1/self.overall_label_count)
        + ", " + "P:\t" + str(self.correct_label_count) + "/" + str(self.predicated_label_count) + "=" + str(self.correct_label_count*1/self.predicated_label_count)
        + ", " + "F:\t" + str(self.correct_label_count*2 /(self.overall_label_count + self.predicated_label_count)) )

