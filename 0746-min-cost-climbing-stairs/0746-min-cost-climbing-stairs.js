/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    memo={}
    
    var dp=function(i){
        
        if(i>=cost.length){
            return 0
        }
        
        if(i in memo){
            return memo[i]
        }
        
        let result=Math.min(dp(i+1),dp(i+2))+cost[i]
        memo[i]=result
        return result
    }
    return Math.min(dp(0),dp(1))
};
