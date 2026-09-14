'''
 本质是点积除以两个模长，记得判断不要除以 0 （使用 eps）

'''
import numpy as np


def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	dot_prod = np.dot(v1, v2)
	v1_norm = np.linalg.norm(v1)
	v2_norm = np.linalg.norm(v2)

	eps = 1e-6
	return dot_prod / max(v1_norm * v2_norm, eps)


import torch
import torch.nn.functional as F

# ----------------------------------------------------
# 场景 A: 计算两个一维向量的相似度 (注意 dim=0)
# ----------------------------------------------------
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([2.0, 4.0, 6.0])

# 对于 1D 向量，需显式指定 dim=0
sim = F.cosine_similarity(a, b, dim=0)
print("1D 向量相似度:", sim.item())  # 输出: 1.0

# ----------------------------------------------------
# 场景 B: 批次数据计算 (Batch, Dim)，对应位置一对一比较
# ----------------------------------------------------
# 假设有两个 batch 大小为 4、特征维度为 128 的张量
x1 = torch.randn(4, 128)
x2 = torch.randn(4, 128)

# 默认沿着 dim=1 计算
sim_batch = F.cosine_similarity(x1, x2, dim=1)
print("批次相似度形状:", sim_batch.shape)  # 输出: torch.Size([4])
print("批次相似度结果:", sim_batch)