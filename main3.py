# 数字映射
number_map = {
    "零": 0,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9
}

# 单位映射
unit_map = {
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10000,
    "亿": 100000000
}


# 正向遍历 1
def forward_cn2an_one(inputs):
    output = 0
    unit = 1
    num = 0
    for index, cn_num in enumerate(inputs):

        if cn_num in number_map:
            # 数字
            num = number_map[cn_num]
            # 最后的个位数字
            if index == len(inputs) - 1:
                output = output + num
        elif cn_num in unit_map:
            # 单位
            unit = unit_map[cn_num]
            # 累加
            output = output + num * unit
            num = 0
        else:
            raise ValueError(f"{cn_num} 不在转化范围内")

    return output


output = forward_cn2an_one("一百二十三")
print("output = ", output)

# output: 123