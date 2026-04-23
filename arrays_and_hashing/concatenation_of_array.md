# Concatenation of Array

- Difficulty: Easy
- Topic: Arrays

## Idea
配列を初期化する際に要素数を指定することで効率的にデータを格納する．

## Tips
- array[]=[0]*n #要素数nの配列の初期化．0を入れるのを忘れないように.
- len(array) #配列の要素数を返す.
- array.append(num) #要素の追加.

## Complexity
- Time: O(n)
- Space: O(n)

## Pattern
- Arrays

## Python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)*2
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        return ans