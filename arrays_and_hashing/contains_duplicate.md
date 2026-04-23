# Contains Duplicate
 
- Difficulty: Easy
- Topic: Hash Set

## Idea
ハッシュセットを使うことでO(n)で重複があるかどうか判別する．

## Complexity
- Time O(n)
- Space O(n)

## Tips
- seen = set() #空集合の作成.重複する項目は自動的に削除される.
- array.sort() #配列のソート．O(n log n)．

## Solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for i in range(len(nums)):
            array.append(nums[i])
            for j in range(len(array)-1):
                if array[j] == nums[i]:
                    return True
        return False
O(n^2),O(n)
## Comment
わざわざarrayを定義しなくても解くことのできる問題だった．O(n^2)

## Model Answer
- Brute Force
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if num[i] == num[j]:
                    return True
        return False
O(n^2),O(1)
- Sort
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    return True
            return False
O(nlogn), O(n) or O(1)
- Hash Set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
O(n), O(n)
- Hash Set Length
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
O(n), O(n)

## Comment
setの使い方が理解できた．最後のHash Set Lengthのプログラムは感動した．
