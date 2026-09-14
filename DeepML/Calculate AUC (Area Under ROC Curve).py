# Calculate AUC (Area Under ROC Curve)
'''
1. ** 核心概念 **：
- ** ROC曲线 **：以假正率（False PositiveRate, FPR）为横轴，真正率（True Positive Rate, TPR）为纵轴绘制的曲线。

TPR = TP / P = TP / (TP + FN)
FPR = FP / N = FP / (TN + FP)

其中 $P$ 为正样本总数，$N$ 为负样本总数。

- ** AUC（Area Under ROC Curve） ** ：ROC 曲线下的面积，取值范围在 $[0, 1]$ 之间。

** 算法步骤 **：
1. ** 边界情况处理 **：统计正样本数 $P$ 和负样本数 $N$。如果全是正例（$N = 0$）或全是负例（$P = 0$），直接返回 `0.0`。
2. ** 按预测分数降序排序 **：将样本按 `y_scores` 从大到小排序。
3. ** 阈值扫描（Threshold Sweeping） ** ：
- 从初始点 $(FPR=0, TPR=0)$ 开始（对应阈值无穷大，所有样本预测为负）。
- 逐个降低阈值。 ** 注意平局处理（Ties） ** ：如果有多个样本的预测分数相同，必须将它们归入同一个阈值一次性统计，避免错误的折线计算。
- 记录每个阈值下的 $(FPR, TPR)$ 坐标点。
4. ** 梯形法则计算面积（Trapezoidal Rule） ** ：
- 遍历相邻的两个点 $(FPR_{i-1}, TPR_{i-1})$ 和 $(FPR_i, TPR_i)$，梯形面积为：
$$\Delta \text {Area} = (FPR_i - FPR_{i-1}) \times \frac {TPR_i + TPR_{i - 1}}{2}$$
（也就是 相邻的 (TPR_i + TPR_i-1) * (FRP_i - FRP_i-1) / 2 是每个小梯形，都加起来即可）
- 将所有小梯形面积累加即可得到 AUC。
'''


def calculate_auc(y_true: list, y_scores: list) -> float:
    """
    计算二分类的 AUC-ROC 值。

    参数:
        y_true: 真实标签列表 (0 或 1)
        y_scores: 模型预测的正类概率/分数列表

    返回:
        float: AUC-ROC 值
    """
    # 基础边界检查
    if not y_true or not y_scores or len(y_true) != len(y_scores):
        return 0.0

    # 统计正样本和负样本数量
    pos_count = sum(1 for y in y_true if y == 1)
    neg_count = sum(1 for y in y_true if y == 0)

    # 边界情况：所有标签均为同一类，返回 0.0
    if pos_count == 0 or neg_count == 0:
        return 0.0

    # 将 (预测分数, 真实标签) 按照分数从大到小排序
    paired = sorted(zip(y_scores, y_true), key=lambda x: x[0], reverse=True)

    # 初始化 ROC 曲线的起点 (0, 0)
    fpr_list = [0.0]
    tpr_list = [0.0]

    tp = 0
    fp = 0
    i = 0
    n = len(paired)

    # 遍历所有阈值
    while i < n:
        current_score = paired[i][0]
        # 处理分数相同的所有样本（避免 tie 分裂成多个步长）
        while i < n and paired[i][0] == current_score:
            if paired[i][1] == 1:
                tp += 1
            else:
                fp += 1
            i += 1

        # 计算当前阈值下的 FPR 和 TPR
        fpr_list.append(fp / neg_count)
        tpr_list.append(tp / pos_count)

    # 利用梯形法则数值积分计算曲线下面积
    auc = 0.0
    for j in range(1, len(fpr_list)):
        width = fpr_list[j] - fpr_list[j - 1]
        avg_height = (tpr_list[j] + tpr_list[j - 1]) / 2.0
        auc += width * avg_height

    return auc


# ---------------- 测试样例 ----------------
if __name__ == "__main__":
    y_true = [0, 0, 1, 1]
    y_scores = [0.1, 0.4, 0.35, 0.8]
    print("AUC:", calculate_auc(y_true, y_scores))  # 输出: 0.75

    # 边界情况测试：全为正例或全为负例
    print("全正例:", calculate_auc([1, 1, 1], [0.2, 0.5, 0.8]))  # 输出: 0.0
    print("全负例:", calculate_auc([0, 0, 0], [0.1, 0.4, 0.7]))  # 输出: 0.0

