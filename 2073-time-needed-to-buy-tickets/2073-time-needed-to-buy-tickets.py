class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int: 
        nums = tickets 
        time_sec = 0
        least_tickets = nums[k]     
		
        for i in range(len(nums)):                  
            if k < i and nums[i] >= least_tickets :         #(1)
                time_sec += (least_tickets - 1)
            elif nums[i] < least_tickets :                   #(2)
                time_sec += nums[i]
            else:                                            #(3)
                time_sec += least_tickets
				
        return time_sec