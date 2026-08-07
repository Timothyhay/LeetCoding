# 定义双向链表节点
class ListNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # 哈希表：key -> ListNode 节点对象的映射
        self.cache = {}

        # 哨兵节点（Dummy Head & Tail），用于简化边界处理
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 辅助方法1：在链表头部（即 dummy head 后面）插入新节点（表示最新访问）
    def _add_to_head(self, node: ListNode) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 辅助方法2：在链表中删除指定节点
    def _remove_node(self, node: ListNode) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # 辅助方法3：将已存在的节点移至头部（代表被访问过）
    def _move_to_head(self, node: ListNode) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    # 辅助方法4：淘汰最久未使用的节点（链表尾部 dummy tail 前面的节点）并返回
    def _pop_tail(self) -> ListNode:
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 只要被读取过，就要更新它到最常使用的位置（即链表头部）
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 已存在，修改 value 并在链表中将其移至头部
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 如果 key 不存在，创建新节点
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # 如果超出容量限制，需要淘汰最久未使用的节点
            if len(self.cache) > self.capacity:
                removed_node = self._pop_tail()
                # 必须从哈希表中同步删除该 key
                del self.cache[removed_node.key]