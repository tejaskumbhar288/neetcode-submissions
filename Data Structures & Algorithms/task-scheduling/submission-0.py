from collections import Counter
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Max heap using negative frequencies
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        # (remaining_frequency, available_time)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1

            # Move tasks whose cooldown has expired back to heap
            if cooldown and cooldown[0][1] == time:
                freq, _ = cooldown.popleft()
                heapq.heappush(heap, freq)

            # Execute highest-frequency available task
            if heap:
                freq = heapq.heappop(heap)
                freq += 1  # remember: negative frequency

                if freq != 0:
                    cooldown.append((freq, time + n + 1))

        return time