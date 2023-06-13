
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # preserving initial indexing          
        for i, t in enumerate(tasks):
            t.append(i)
        # sorting based on enqueTime
        tasks.sort(key = lambda t: t[0])

        ans, pq = [], []
        i, time = 0, tasks[0][0]
        while i < len(tasks):
            #add task to Queue if enqueueTime is less than current time
            while i<len(tasks) and time >= tasks[i][0]:
                heappush(pq, [tasks[i][1], tasks[i][2]])
                i+=1
            
            # jump to next time if no element in priorityQueue
            if pq:
                priority, idx = heappop(pq)
                ans.append(idx)
                time += priority
            else:
                time = tasks[i][0]
        
        # pop remaining Queue
        while pq:
            priority, idx = heappop(pq)
            ans.append(idx)
        return ans