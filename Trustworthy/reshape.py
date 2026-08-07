def reshape(input_array, new_shape):

    flat_input_list =[]

    def _flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                _flatten(sub_item)
        else:
            flat_input_list.append(item)

    _flatten(input_array)
    total_elements = len(flat_input_list)

    # 3. 填充前先处理 -1
    minus_one_count = new_shape.count(-1)
    if minus_one_count > 1:
        raise ValueError

    if -1 in new_shape:
        other_product = 1
        minus_one_position = -1
        for i, elem in enumerate(new_shape):
            if elem != -1:
                other_product *= elem
            else:
                minus_one_position = i

        new_shape[minus_one_position] = total_elements // other_product

    # 1. 元素数守恒
    new_shape_elements = 1
    for elem in new_shape:
        new_shape_elements *= elem

    if total_elements != new_shape_elements:
        raise ValueError

    # 2. 行优先填充
    # 推出条件：就剩1维 - [it for _ in range(dims[0)]
    # 否则 build [build(dims[1:]) for _ in range(dims[0]]

    # 分治[1:] 确保行优先

    def build(data, shape):
        if len(shape) == 1:
            return data

        dim = shape[0]
        sub_size = len(data) // dim

        result = []
        for i in range(dim):
            start = i * sub_size
            end = start + sub_size
            sub_data = data[start:end]

            result.append(build(sub_data, shape[1:]))

        return result

    return build(flat_input_list, new_shape)


def reshape_updated(input_array, new_shape):
    # 1. 展平数组
    flat_data = []

    def flatten(arr):
        for item in arr:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_data.append(item)

    flatten(input_array)
    total_elements = len(flat_data)

    # 2. 解析 new_shape 与自动推导 -1
    new_shape = list(new_shape)
    neg_one_count = new_shape.count(-1)

    if neg_one_count > 1:
        raise ValueError("new_shape 中最多只能有一个 -1")

    known_product = 1
    for dim in new_shape:
        if dim != -1:
            if dim <= 0:
                raise ValueError("维度必须为正整数或 -1")
            known_product *= dim

    if neg_one_count == 1:
        if known_product == 0 or total_elements % known_product != 0:
            raise ValueError("无法推导 -1 的维度")
        inferred_dim = total_elements // known_product
        # 替换 -1
        new_shape[new_shape.index(-1)] = inferred_dim
    else:
        if known_product != total_elements:
            raise ValueError("元素总数不匹配")

    # 3. 递归重构多维列表
    it = iter(flat_data)

    def build(shape):
        if not shape:
            return next(it)
        return [build(shape[1:]) for _ in range(shape[0])]

    return build(new_shape)

if __name__ == '__main__':
    # answer = reshape([[1, 2], [3, 4]], [1, 4])
    # print(answer)
    #
    # answer = reshape([[1, 2], [3, 4], [5, 6]], [2, 3])
    # print(answer)
    #
    # answer = reshape([[1, 2], [3, 4], [5, 6]], [2, -1])
    # print(answer)
    #
    # answer = reshape([[1, 2, 3, 4], [5, 6, 7, 8]], [2, 2, 2])
    # print(answer)


    # =====  1. 基础维度变换 =====
    input1 = [[1, 2, 3], [4, 5, 6]]  # 形状 (2, 3)，总数 6
    shape1 = [3, 2]
    # 预期输出: [[1, 2], [3, 4], [5, 6]]
    print("Test 1:", reshape(input1, shape1))

    # =====  2. 降维成一维列表 =====
    input2 = [[1, 2], [3, 4]]  # 形状 (2, 2)，总数 4
    shape2 = [4]
    # 预期输出: [1, 2, 3, 4]
    print("Test 2:", reshape(input2, shape2))

    # =====  3. 升维至三维列表 =====
    input3 = [1, 2, 3, 4, 5, 6, 7, 8]  # 形状 (8,)，总数 8
    shape3 = [2, 2, 2]
    # 预期输出: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    print("Test 3:", reshape(input3, shape3))

    # ===== 4. 使用 -1 自动推导维度 =====
    input4 = [[1, 2, 3], [4, 5, 6]]  # 总数 6
    shape4 = [-1, 2]  # -1 应该被推导为 3
    # 预期输出: [[1, 2], [3, 4], [5, 6]]
    print("Test 4:", reshape(input4, shape4))

    # ===== 5. 异常处理：元素总数不匹配 =====
    input5 = [1, 2, 3, 4]  # 总数 4
    shape5 = [2, 3]  # 需要 6 个元素
    try:
        reshape(input5, shape5)
    except ValueError as e:
        # 预期捕获异常
        print("Test 5 (Expected Error):", e)

    # ===== 6. 异常处理：非法的 -1 使用 =====
    input6 = [1, 2, 3, 4]
    shape6 = [-1, -1]  # 两个 -1 无法唯一确定
    try:
        reshape(input6, shape6)
    except ValueError as e:
        # 预期捕获异常
        print("Test 6 (Expected Error):", e)

    # ===== 7. 二维到三维 =====
    # 形状 (4, 3)，总数 12
    input7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    shape7 = [2, 3, 2]
    # 预期输出: [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]
    print("Test 7:", reshape(input7, shape7))