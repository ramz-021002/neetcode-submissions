class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        encoded_string = ""
        for w in strs:
            encoded_string += f"{length}#" + w
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if len(s) == 1:
            return [""]

        if len(s) >= 1 :
            length = int(s[0])
            limiter = s[1]
            decoded_string = [x for x in s.split(f"{length}{limiter}")]
            return decoded_string[-length:]
        else:
            return []


            
        