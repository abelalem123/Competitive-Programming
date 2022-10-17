class Solution {
    public int maxVowels(String s, int k) {
        int count=0;
        for(int i=0;i<k;i++){
            char ch=s.charAt(i);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') count++;
        }
        int max=count;
        int l=0;
        int r=k-1;
        while(r<s.length()-1){
          
            char chl=s.charAt(l);
            if(chl=='a'||chl=='e'||chl=='i'||chl=='o'||chl=='u')count--;
            l++;
            r++;
              char chr=s.charAt(r);
            if(chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u')count++;
            max=Math.max(max,count);
        }
        return max;
    }
}
