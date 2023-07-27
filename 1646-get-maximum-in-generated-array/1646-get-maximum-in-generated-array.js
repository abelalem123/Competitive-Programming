/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    memo=[0,1]
    console.log(memo)
    if(n==0){
        return 0
    }
    var dp=(i)=>{
       if(i*2>n||i*2+1>n){
           return 
       }
        
        memo[i*2]=memo[i]
        memo[i*2+1]=memo[i]+memo[i+1]
        dp(i+1)
    }
    dp(1)
    max=memo[0]
    for(i of memo){
        max=Math.max(max,i)
    }
    
    return max
};