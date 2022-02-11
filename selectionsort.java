


class Solution
{
	int  select(int arr[], int i)
	{
        int min=arr[i];// code here such that selectionSort() sorts arr[]
        for(int j=i+1;j<arr.length;j++){
            if(min>arr[j]){
              min=arr[j];  
            }
           
        }
        return min;
	}
	
	void selectionSort(int arr[], int n)
	{
	    int i;
	    for (i=0;i<n;i++){
	        int min=select(arr,i);
	        for (int j=i;j<n;j++){
	            if(min==arr[j]){
	                arr[j]=arr[i];
	                arr[i]=min;
	            }
	        }
	       
	       
	    }
	   
	}
}
