function minPatches(nums: number[], n: number): number {
    let [maxNumGen, output, i] = [0,0,0];
    let numLen = nums.length;

    while(maxNumGen < n){
        if(maxNumGen + 1 >= nums[i]){
            maxNumGen += nums[i];
            i++;
        }
        else{
            output++;
            maxNumGen += maxNumGen + 1;
        }
    }
    return output
};   