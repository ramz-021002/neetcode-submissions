class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        encoded_string = ""
        for w in strs:
            encoded_string += f"{length}#" + w
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if len(s) > 0 :
            length = s[0]
            limiter = s[1]
        if length and limiter:
            decoded_string = [x for x in s.split(f"{length}{limiter}")]
        else:
            decoded_string = []
        
        if length == 0:
            return decoded_string
        else:
            return decoded_string[-int(length):]
        