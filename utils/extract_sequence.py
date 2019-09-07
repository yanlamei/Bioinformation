

class ExtractSeq():
    def __init__(self, filename):
        # 初始化变量
        self.filename = filename

    def find_name_and_base_sequence(self):
        name_and_sequence = {}
        name_list = []
        sequence_list = []
        with open(self.filename, 'r', encoding='utf-8') as f:
            # 读取第一行
            line = f.readline()
            # sequence用来存储一个基因对应的全部碱基序列
            sequence = ""
            # 判断读取一个基因的碱基是否结束
            read_finished = False
            while line:
                line_strip = line.strip()
                print("line_strip = ", line_strip)
                line = f.readline()

                # 判断这一行的是不是以">"开头
                if line_strip[0] == ">":
                    # 以">"开头，则判定为名字
                    name_list.append(line_strip)
                    read_finished = True
                else:
                    # 不以">"开头，则判定为碱基序列
                    sequence += line_strip

                # 如果遇到了名字这一行或者是最后一行，那么就把前面的
                # sequence放入到sequence_list中
                if read_finished or (not line):
                    sequence_list.append(sequence)
                    # sequence清0
                    sequence = ""
                    read_finished = False

            for i in range(len(name_list)):
                name_and_sequence[name_list[i]] = sequence_list[i + 1]  # 这里为什么要加1

            return name_and_sequence
