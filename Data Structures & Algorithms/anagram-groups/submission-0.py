class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = []
        for element in strs:
            var = "".join(sorted(element))
            temp.append(var)
        
        print(temp)
        hashmap = {}
        for i in range(0,len(temp)):
            if temp[i] in hashmap:
                hashmap[temp[i]].append(strs[i])
            else:
                hashmap[temp[i]] = [strs[i]]

        return list(hashmap.values())