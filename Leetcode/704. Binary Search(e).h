tag: binary search

```c++

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size()-1;
        int mid=0;
        while(left<right){
            mid=left+(right-left)/2;
            if(target>nums[mid]){
                left=mid+1;
            }
            else if(target<nums[mid]){
                right=mid-1;
            }
            else{
                break;
            }
        }
        mid=left+(right-left)/2;
        if(target==nums[mid])
            return mid;
        return -1;
    }
};


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return -1;
    }
};
```