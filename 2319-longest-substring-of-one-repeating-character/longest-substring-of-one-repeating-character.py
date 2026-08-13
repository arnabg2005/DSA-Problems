class Node:
    def __init__(self):
        self.mx = 0   # Maximum repeating substring length in this range
        self.pre = 0  # Repeating length from the left boundary
        self.suf = 0  # Repeating length from the right boundary
        self.sz = 0   # Total length of this range

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def merge(self, parent: Node, left: Node, right: Node, mid: int, l: int) -> None:
        parent.sz = left.sz + right.sz
        parent.mx = max(left.mx, right.mx)
        parent.pre = left.pre
        parent.suf = right.suf

        # Check if the characters at the boundary can be merged
        if self.s[mid] == self.s[mid + 1]:
            parent.mx = max(parent.mx, left.suf + right.pre)
            
            # If left child is uniform, prefix extends into right child
            if left.pre == left.sz:
                parent.pre = left.sz + right.pre
            # If right child is uniform, suffix extends into left child
            if right.suf == right.sz:
                parent.suf = right.sz + left.suf

    def build(self, node: int, l: int, r: int) -> None:
        if l == r:
            self.tree[node].mx = 1
            self.tree[node].pre = 1
            self.tree[node].suf = 1
            self.tree[node].sz = 1
            return
        
        mid = (l + r) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)
        self.merge(self.tree[node], self.tree[2 * node], self.tree[2 * node + 1], mid, l)

    def update(self, node: int, l: int, r: int, idx: int, ch: str) -> None:
        if l == r:
            self.s[idx] = ch
            return
        
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, ch)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, ch)
            
        self.merge(self.tree[node], self.tree[2 * node], self.tree[2 * node + 1], mid, l)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        st = SegmentTree(s)
        ans = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, st.n - 1, idx, ch)
            ans.append(st.tree[1].mx)
            
        return ans
