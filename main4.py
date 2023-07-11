import os


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    #
    # def __hash__(self):
    #     return hash((self.val, self.left, self.right))  # get a tuple's hash
    #
    # def __eq__(self, other):
    #     return (self.val, self.left, self.right) == (other.val, other.left, other.right)

    # def __repr__(self):
    #     return "hello, world"

# import uncompyle6 as uc
# pf = open("test.py", "w")
# uc.decompile_file("test.pyc", pf)

def show(tree_node: TreeNode):
    """
    友好的打印tree_node格式
    :param tree_node:
    :return:
    """
    # 广度优先遍历值
    ls = [tree_node]
    pre_ls = []
    data = [[tree_node.val]]
    while ls:
        cur = ls.pop(0)
        if not ls:
            data.append([])
            ls.extend(pre_ls)
        data[-1].extend([cur.left.val if cur.left else None, cur.right.val if cur.right else None])
        pre_ls.extend([cur.left, cur.right])
    data.append([])
    while pre_ls:
        cur = pre_ls.pop(0)
        data[-1].extend([cur.left.val if cur.left else None, cur.right.val if cur.right else None])

    # 阶梯序数
    span_list = []
    for i in range(len(data)):
        if span_list:
            span_list.append(span_list[-1] * 2 + 1)
        else:
            span_list.append(1)

    # 最合适的span长度
    span = 0
    for line_idx, val_list in enumerate(data):
        formatted_val_list = []
        for i, val in enumerate(val_list):
            str_val = str(val) if val is not None else ""
            span = span if span >= len(str_val) else len(str_val)
            if line_idx == 0:
                formatted_val_list.append(str_val)
            else:
                formatted_val_list.append(str_val)
        data[line_idx] = formatted_val_list
    c_span = span + 2

    # 格式化
    char_val_print_list = []
    formatted_val_print_list = []
    for line_idx, formatted_val_list in enumerate(data):
        char_val_list = [''] * len(formatted_val_list)
        for i, formatted_val in enumerate(formatted_val_list):
            two_space_formatted_val = ' ' * c_span if not formatted_val else ' ' + formatted_val + ' '
            formatted_val_list[i] = two_space_formatted_val
            if formatted_val:
                if i % 2 == 0:
                    # 左侧节点
                    char = ' ' * (len(two_space_formatted_val) - 1) + '/'
                else:
                    # 右侧节点
                    char = '\\' + ' ' * (len(two_space_formatted_val) - 1)
                char_val_list[i] = char
            else:
                char_val_list[i] = ' ' * c_span
        if line_idx != 0:
            char_val_print_list.append(char_val_list)
        formatted_val_print_list.append(formatted_val_list)

    # 打印
    center_length = span_list[-1] * c_span
    for line_idx, formatted_val_list in enumerate(formatted_val_print_list):
        num = span_list[-1 * line_idx - 1]
        mid_span = " " * (c_span * num)
        formatted_val_str = mid_span.join(formatted_val_list)
        print(formatted_val_str.center(center_length, " "))
        if line_idx < len(char_val_print_list):
            num = span_list[-1 * line_idx - 1 - 1]
            mid_span = " " * c_span * num
            char_val_str = mid_span.join(char_val_print_list[line_idx])
            print(char_val_str.center(center_length, " "))

# root = {val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode
#     {val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode
#     {val: 4, left: None, right: None}}}, right: TreeNode
#     {val: 1, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode
#     {val: 8, left: None, right: None}}}

root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(2)
# parent = {root:None}
parent = dict()
parent[root] = None

# show(root)
print(root)