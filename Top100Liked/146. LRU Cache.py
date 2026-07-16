class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # 初始化虚拟头节点和尾节点，避免处理边界时的空指针判断
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # 使用 len(self.cache) 替代 self.size 判断是否超出容量
            if len(self.cache) > self.capacity:
                # 淘汰最久未使用的节点
                removed_node = self._remove_tail()
                # 必须先从哈希表删除，确保长度正确
                del self.cache[removed_node.key]

    # --- 链表操作辅助函数 ---

    def _add_to_head(self, node):
        """将节点插入到虚拟头节点后面"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """从双向链表中移除一个节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        """将已有节点移动到头部（表示最近被访问）"""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        """移除并返回尾部的真实节点"""
        res = self.tail.prev
        self._remove_node(res)
        return res