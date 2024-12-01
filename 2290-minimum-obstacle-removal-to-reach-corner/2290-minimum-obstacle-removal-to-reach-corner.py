class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        deque_ = deque([(0, 0, 0)]) 
        visited = [[False] * n for _ in range(m)]
        
        while deque_:
            x, y, obstacles = deque_.popleft()
            if x == m - 1 and y == n - 1:
                return obstacles
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] == 0:
                        deque_.appendleft((nx, ny, obstacles))
                    else:
                        deque_.append((nx, ny, obstacles + 1))
        
        return -1
        