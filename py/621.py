class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        hp = [-cnt for (char, cnt) in c.items()]

        cycles = 0
        heapify(hp)
        q = deque()

        while hp or q:
            cycles += 1

            if hp:
                remaining = heappop(hp) + 1

                if remaining < 0:
                    q.append((remaining, cycles + n))

            if q and q[0][1] == cycles:
                heappush(hp, q.popleft()[0])

        return cycles


