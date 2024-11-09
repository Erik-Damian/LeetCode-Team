class Solution {
    public int minPatches(int[] nums, int n) {
        long maxNumGen = 0;
        int lenNum = nums.length;
        int output = 0;
        int i = 0;
        while(maxNumGen < n){
            if(i<lenNum){
                if(maxNumGen + 1 >= nums[i]){
                    maxNumGen += nums[i];
                    i++;
                }
                else{
                    output++;
                    maxNumGen += maxNumGen + 1;
                }

            }
            else{
                output++;
                maxNumGen += maxNumGen + 1;
            }
            if(maxNumGen >= n){
                break;
            }
            
        }
        return output;  
    
}

}
