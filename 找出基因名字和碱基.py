

def find_name_and_base_sequence(filename):
    name_and_sequence = {}
    name_list = []
    sequence_list = []
    with open(filename, 'r', encoding='utf-8') as f:
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
            name_and_sequence[name_list[i]] = sequence_list[i+1]  #这里为什么要加1

        return name_and_sequence
        #为什么不用关闭文件




if __name__ == '__main__':
    name_and_sequence = find_name_and_base_sequence("sequence.fasta")
    print(name_and_sequence)
    print(len(name_and_sequence))
    for k in name_and_sequence:
        print(k,name_and_sequence[k])

    name = []
    with open('out.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line_a = line.split()
            line_a[0] = '>'+line_a[0]
            name.append(line_a[0])
        print(name)
        n = len(name)
        print('n=',n)
        f.close()

    for k in name_and_sequence:
        name_1 = k.split()
        name_2 = name_1[0]

        if name_2 in name :
                print('name_2=',name_2)

                print(k,name_and_sequence[k])
                open('取到的序列.txt','a').write(k+'\n'+name_and_sequence[k]+'\n')
