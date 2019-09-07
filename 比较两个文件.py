

def read_file_and_generate_list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file_list = f.readlines()
    return file_list

def find_differences(list_1, list_2, name_of_list_1, name_of_list_2):
    for item in list_1:
        if item not in list_2:
            print("'{}'在{}中，但是不在{}中".format(item.strip("\n"), name_of_list_1, name_of_list_2))


if __name__ == '__main__':
    # 获取文件1里面的内容
    file_1_list = read_file_and_generate_list("C:\\Users\\asus\\Desktop\\文件b.txt")

    # 获取文件2里面的内容
    file_2_list = read_file_and_generate_list("C:\\Users\\asus\\Desktop\\文件a.txt")

    print(file_1_list)
    print(file_2_list)

    # 调用两次，找出所有在文件1中而不在文件2中的行，和所有在文件2中而不在文件1中的行
    find_differences(list_1=file_1_list, list_2=file_2_list, name_of_list_1="文件1", name_of_list_2="文件2")
    find_differences(list_1=file_2_list, list_2=file_1_list, name_of_list_1="文件2", name_of_list_2="文件1")
