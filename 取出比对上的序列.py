

def delete_line_break(filename):
    sequence = ''
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            if line[0] == '>':
                line_a = '\n'+line
                sequence += line_a

            else:
                line_b =line.strip()
                sequence += line_b

        return sequence

def create_dict(filename):

    name_list = []
    sequence_list = []
    name_and_sequence_dict = {}
    with open(filename, 'r', encoding='utf-8') as fa:
        for line in fa:
            print('line=',line)
            if line[0] == '>':
                 k = line.strip()
                 name_list.append(k)
            else:
                v = line
                sequence_list.append(v)
        for i in range(len(name_list)):
                name_and_sequence_dict[name_list[i]] = sequence_list[i+1]

        return name_and_sequence_dict

def get_name(filename):
    name = []
    with open(filename,'r',encoding='utf-8') as fb:
        for line in fb:
            line_a = line.split()
            line_b = '>'+line_a[0]
            name.append(line_b)

    return name
if __name__ == '__main__':
    sequence = delete_line_break('sequence.fasta')
    open('sequence.txt','w').write(sequence)

    name_and_sequence_dict = create_dict('sequence.txt')
    print(name_and_sequence_dict)
    print(len(name_and_sequence_dict))

    name = get_name('out.txt')
    print(name)
    
    for k in name_and_sequence_dict:
        name_a = k.split()
        name_b = name_a[0]
        if name_b in name:
            print(k,name_and_sequence_dict[k])
            open('取到的序列.txt', 'a').write(k + '\n' + name_and_sequence_dict[k] + '\n')

