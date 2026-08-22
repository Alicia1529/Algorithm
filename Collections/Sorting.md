```
python3 sorting_practice.py 
```

### merge sort
```c++
class Solution {
public:
    vector<int> mergeArray(vector<int>& left, vector<int>& right) {
        vector<int> merged;
        int i = 0, j = 0;
        while (i < left.size() && j < right.size()) {
            if (left[i] <= right[j]) {
                merged.push_back(left[i++]);
            } else {
                merged.push_back(right[j++]);
            }
        }
        while (i < left.size()) {
            merged.push_back(left[i++]);
        }
        while (j < right.size()) {
            merged.push_back(right[j++]);
        }
        return merged;
    }

    vector<int> sortArray(vector<int>& nums) {
        if (nums.size() <= 1) return nums;
        int mid = nums.size() / 2;
        vector<int> left(nums.begin(), nums.begin() + mid);
        vector<int> right(nums.begin() + mid, nums.end());
        left = sortArray(left);
        right = sortArray(right);
        return mergeArray(left, right);
    }
};
```

