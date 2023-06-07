class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = []
        self.times = times
        vote_count = {}
        leader = None
        for i in range(len(persons)):
            person = persons[i]
            time = times[i]
            if person not in vote_count:
                vote_count[person] = 0
            vote_count[person] += 1
            if leader is None or vote_count[person] >= vote_count[leader]:
                leader = person
            self.leaders.append(leader)
            # if len(self.times) == 0 or self.leaders[-2] != self.leaders[-1]:
            #     self.times.append(time)

    def q(self, t: int) -> int:
       
        x=bisect_right(self.times,t)
        return self.leaders[x-1]
        
        
        # while left <= right:
        #     mid = (left + right) // 2
        #     if self.times[mid] == t:
        #         return self.leaders[mid]
        #     elif self.times[mid] < t:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # # print(left,right)
        # return self.leaders[right]
        
        return left
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)