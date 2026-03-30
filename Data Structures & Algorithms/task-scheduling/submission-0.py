class Solution:
    def leastInterval(self, tasks, n):

        counts = Counter(tasks)

        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # (ready_time, remaining_count)

        while maxHeap or cooldown:
            time += 1

            # run a task if available
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1  # toward zero
                if count != 0:
                    cooldown.append((time + n, count))

            # release all tasks whose cooldown expired
            while cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(maxHeap, cnt)

        return time