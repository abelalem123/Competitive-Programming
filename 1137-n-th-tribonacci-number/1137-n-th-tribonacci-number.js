/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    memo={}
    var dp=function(n){
        if(n==0|| n==1){
            return n
        }
        if(n==2){
            return 1
        }
        
        if(n in memo){
            return memo[n]
        }
        
        let result=dp(n-3)+dp(n-2)+dp(n-1)
        memo[n]=result
        return result
    }
    return dp(n)
};