class Solution:
    def findLucky(self, arr: List[int]) -> int:
        HashMap = {}
        values = [-1]
        for i in range(len(arr)):
            HashMap[arr[i]] = arr.count(arr[i])
            if HashMap[arr[i]] == arr[i]:
                values.append(arr[i])
        return max(values)
