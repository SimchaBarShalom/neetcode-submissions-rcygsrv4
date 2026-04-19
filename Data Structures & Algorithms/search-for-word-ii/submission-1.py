class Solution:
    def findWords(self, board, words):
        from collections import Counter

        # --- שלב 1: סינון מילים לא אפשריות ---
        board_count = Counter(c for row in board for c in row)
        words = [
            w for w in words
            if all(board_count[c] >= w.count(c) for c in set(w))
        ]

        # --- שלב 2: בניית Trie ---
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["word"] = word  # שומרים את המילה עצמה

        rows, cols = len(board), len(board[0])
        res = []

        # --- שלב 3: DFS ---
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node:
                return

            next_node = node[char]

            # מצאנו מילה
            if "word" in next_node:
                res.append(next_node["word"])
                del next_node["word"]  # מונע כפילויות

            board[r][c] = '#'

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            board[r][c] = char

            # pruning – אם אין המשך, מוחקים מה־Trie
            if not next_node:
                del node[char]

        # --- שלב 4: התחלת DFS רק מאותיות רלוונטיות ---
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res