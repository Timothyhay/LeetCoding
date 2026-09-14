from typing import List


def pack_samples(
    samples: List[List[int]],
    max_length: int,
    eod_id: int = -1,
    pad_id: int = -2,
) -> List[List[int]]:
    """将多个样本打包为尽可能少、长度固定为 max_length 的 packs。

    :param samples: 待打包的样本列表
    :param max_length: 每个 pack 的目标固定长度
    :param eod_id: 样本结束符 ID
    :param pad_id: 填充占位符 ID
    :return: 打包并填充后的 List[List[int]]
    """
    if not samples:
        return []

    # 1. 预处理：给每个 sample 加上 eod_id
    prepared_samples = [s + [eod_id] for s in samples]

    # 检查单个样本长度是否超限
    for s in prepared_samples:
        if len(s) > max_length:
            raise ValueError(
                f"Sample length {len(s)} exceeds max_length {max_length}"
            )

    # 2. 贪心策略：按样本长度降序排序
    prepared_samples.sort(key=len, reverse=True)

    # bins 存储每个 pack 当前包含的 samples
    # remaining_capacities 存储每个 pack 剩余可用容量
    bins: List[List[List[int]]] = []
    remaining_capacities: List[int] = []

    # 3. Best-Fit Decreasing 装箱
    for sample in prepared_samples:
        item_len = len(sample)

        # 寻找能容纳当前样本且剩余容量最小的 bin
        best_idx = -1
        min_remaining = max_length + 1

        for i, cap in enumerate(remaining_capacities):
            if cap >= item_len and cap < min_remaining:
                min_remaining = cap
                best_idx = i

        if best_idx != -1:
            # 放入最合适的已有 bin
            bins[best_idx].append(sample)
            remaining_capacities[best_idx] -= item_len
        else:
            # 放不下，新开一个 bin
            bins.append([sample])
            remaining_capacities.append(max_length - item_len)

    # 4. 组装结果并用 pad_id 补齐至 max_length
    result = []
    for b in bins:
        # 展平当前 bin 中的所有 sample
        packed_seq = [token for sample in b for token in sample]
        # 用 pad_id 填充至 max_length
        pad_len = max_length - len(packed_seq)
        packed_seq.extend([pad_id] * pad_len)
        result.append(packed_seq)

    return result



samples = [
    [120, 32, 4342, 1],  # len + 1 = 5
    [1, 2, 3, 4, 5],     # len + 1 = 6
    [10, 20],            # len + 1 = 3
    [99],                # len + 1 = 2
]
max_length = 10
eod_id = -1
pad_id = -2

packs = pack_samples(samples, max_length, eod_id, pad_id)
for idx, pack in enumerate(packs):
    print(f"Pack {idx + 1}: {pack}")