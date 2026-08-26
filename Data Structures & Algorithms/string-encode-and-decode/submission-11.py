class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for w in strs:
            encoded_string += f"{len(w)}#" + w
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1

            decoded.append(s[i:i + length])
            i += length
        
        return decoded

            
        