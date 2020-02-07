def o_question(v1, v2):
    """
    两个版本的对比
    :param v1:  版本1
    :param v2:  版本2
    :return: 1，-1，0
    """
    # python比较灵活 可以按照版本的不同分隔开并转成int类型    str(01) -> int(1)
    version1 = list(map(int, v1.split(".")))
    version2 = list(map(int, v2.split(".")))
    # python 列表顺位比较
    if version1 < version2:
        return -1
    elif version1 > version2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    o_question('1.1.001.1', '1.1.01')
