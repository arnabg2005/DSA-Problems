class Solution {
public:
    void rotateArrayByOne(vector<int>& nums) {
        int temp=arr[0];
        for(int j=1;j<nums.size();j++){
            nums[j-1]=nums[j];
        }
        nums[nums.size()-1]=temp;
    }
};
