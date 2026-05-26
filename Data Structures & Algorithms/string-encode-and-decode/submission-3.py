class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "_" + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0

        strs = []
        while left < len(s):
            while s[right].isnumeric():
                right += 1

            str_len = int(s[left:right])
            start_idx = right + 1
            word = s[start_idx:str_len + start_idx]

            strs.append(word)
            left = start_idx + str_len
            right = left

        return strs
