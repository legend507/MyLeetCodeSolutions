class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_list = []
        for one_str in strs:
            encoded_str = [ord(i) for i in one_str]
            encoded_list.append('|'.join(map(str, encoded_str)))
        ret = ','.join(encoded_list)
        return ret

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        original_list = []
        encoded_list = s.split(',')
        for one_element in encoded_list:
            encoded_str = one_element.split('|')
            decoded_str = [chr(int(i)) for i in encoded_str if i != '']
            original_str = ''.join(decoded_str)
            original_list.append(original_str)
        return original_list
        
# Much easier method. It seems π is not included in ascii 256.
class Codec_non_ascii:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return 'π'.join(strs)
        
    def decode(self, s):
        """Decodes a single string to a list of strings."""
        return s.split('π')


s = Codec()

encoded = s.encode(["Hello","World"])
print(encoded)
decoded = s.decode(encoded)
print(decoded)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))