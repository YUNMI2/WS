def cleanLabel(curLabel):
    '''
    :param curLabel:str
    :return:除了前缀列表里面的后缀
    '''
    pre_label_list = ['B','b',"M","m","E","e","s","S","I","i"]
    if len(curLabel) > 2 and curLabel[1] == "-":
        if curLabel[0] in pre_label_list:
            return curLabel[2:]
    return curLabel

def is_start_label(label):
    '''
    :param label:str
    :return:
    '''
    if len(label) < 3:#不是很明白这边的长度判断是干什么的
        return False
    return (label[0] == "b" or label[0] == "B" or label[0] == "s" or label[0] == "S")  and label[1] == "-"


def is_continue_label(label,startlabel,distance):
    '''
    :param label: str
    :param startlabel:str
    :param distance: int
    :return:
    '''
    if distance == 0:
        return True
    if len(label) < 3:
        return False
    if distance != 0 and is_start_label(label):
        return False
    if (startlabel[0] == 's' or startlabel[0] == 'S') and startlabel[1] == "-":
        return False
    curcleanlabel = cleanLabel(label)
    startcleanlabel = cleanLabel(startlabel)
    if curcleanlabel != startcleanlabel:
        return False
    return True


if __name__ == "__main__":
    print(is_start_label("b-seg"))
    print(cleanLabel("b-seg"))
    print(is_continue_label("e-seg",'b-seg',1))
