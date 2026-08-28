class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        encoded_string = ""
        for w in strs:
            encoded_string += f"{length}#" + w
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s[0]:
            length = s[0]
        if s[1]:
            limiter = s[1]

        decoded_string = [x for x in s.split(f"{length}{limiter}")]

        if length == 0:
            return decoded_string
        else:
            return decoded_string[-int(length):]
        