class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        res = {node[0]: math.inf for node in edges}
        res.update({node[1]: math.inf for node in edges})
        res.update({src: 0})
        if len(res) < n:
            max_key = max(res.keys())
            for i in range(max_key + 1, n):
                res[i] = math.inf

        def helper(node_id):
            for node in edges:
                if node[0] == node_id:
                    next_node = node[1]
                    edge_weight = node[2] + res[node_id]
                    res[next_node] = min(edge_weight, res[next_node])
                    if next_node == src:
                        return
                    helper(next_node)
        helper(src)
        for key in res:
            if res[key] == math.inf:
                res[key] = -1
        return res
        