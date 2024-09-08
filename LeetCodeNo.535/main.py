class Codec:

# My Initial thought was to use a hash fn to encode the url.
# This is NOT necessary. The requirement only mentioned about encode, not to hash or just a plan idx number.
# In this case, just using a dictionary with idx = 1, 2, 3... works.

    def __init__(self):
        self.m = {}
        self.idx = 0
        self.domain = "https://tinyurl.com/"
  
    def encode(self, longUrl):
        # Increment the index to create a new identifier
        self.idx += 1
        # Map the current index to the long URL
        self.m[str(self.idx)] = longUrl
        # Generate and return the shortened URL
        return f'{self.domain}{self.idx}'
  
    def decode(self, shortUrl):
        # Extract the identifier from the URL
        idx = shortUrl.split('/')[-1]
        # Retrieve the original long URL
        return self.m[idx]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))