class Alphabet:
    def __init__(self):
        self.m_StringToId = dict()
        self.m_IdToString = list()
        self.m_b_fixed = False
        self.m_size = 0

    def StrToId(self,str_in):
        if str_in in self.m_StringToId:
            return self.m_StringToId[str_in]
        elif not self.m_b_fixed:
            newid = self.m_size
            self.m_StringToId[str_in] = newid
            self.m_IdToString.append(str_in)
            self.m_size += 1
            return newid
        else:
            return -1


    def from_id(self,qid = -1,def_value = ""):
        '''

        :param qid:search_id
        :param def_value: str
        :return:
        '''
        if qid < 0 or self.m_size <= qid:
            return def_value
        else:
            return self.m_IdToString[qid]

    def from_str(self,qstr = ""):
        if qstr not in self.m_StringToId:
            return -1
        return self.m_StringToId[qstr]

    def clear(self):
        self.m_StringToId = dict()
        self.m_IdToString = list()
        self.m_b_fixed = False
        self.m_size = 0

    def set_fixed_flag(self,bfixed):
        self.m_b_fixed = bfixed

    def size(self):
        return self.m_size








