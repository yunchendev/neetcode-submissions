class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque()
        time = 0

        for i in range(n):
            q.append(i)

        while q:
            curr = q.popleft()
            tickets[curr] -= 1
            time += 1

            if tickets[curr] == 0:
                if curr == k:
                    return time
            else:
                q.append(curr)

        return time