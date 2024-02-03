class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);
        int prefixp=1;
        for(int i=0;i<nums.size();i++){
            result[i]*=prefixp;
            prefixp*=nums[i];
        }   
        int suffixp=1;
        for(int i=nums.size()-1;i>=0;i--){
            result[i]*=suffixp;
            suffixp*=nums[i];
        }
        return result;     
    }
};
