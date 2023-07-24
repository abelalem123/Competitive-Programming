/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if(n==0){
        return 1
    }
    else if(n<0){
        return myPow(1/x,-n)
    }
    else if(n%2==0){
        return myPow(x*x,n/2)
                     
    }
    else{
        return x*myPow(x*x,(n-1)/2)
        }
};