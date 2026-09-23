class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for cnt in count.values():
            heapq.heappush(heap,-cnt)
        q = deque()
        timer = 0
        while heap or q:
            timer += 1
            if heap:
                cnt = heapq.heappop(heap)+1
                if cnt:
                    q.append([cnt,timer + n])
            if q and q[0][1] == timer:
                heapq.heappush(heap,q.popleft()[0])
        return timer