class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        boats=0
        l, r=0, len(people)-1
        while l<=r:
            boats+=1
            # If I can fit heaviest (r) and lightest (l).
            if people[l]+people[r]<=limit:
                l+=1
            # Heaviest (r) can always fit in boat.
            r-=1
        return boats
    

people = [3,2,2,1]
limit = 3

s=Solution()
print(s.numRescueBoats(people, limit))
