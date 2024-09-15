class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # Thoughts: 
        # 1. Use dict to store key=smaller_region, value=immediate bigger region.
        # 2. Find all region1's parents (including itself), then check region2's parents one by one, if they are in region1's parents list.

        # 1.
        region_dict = {}
        for region_list in regions:
            for i in range(1, len(region_list)):
                region_dict[region_list[i]] = region_list[0]
        
        # 2.
        region1_parents = []
        region1_parents.append(region1) # Region1 includes itself.
        key = region1
        while key in region_dict:
            region1_parents.append(region_dict[key])
            key = region_dict[key]

        # Corner case, where region2 include region1.
        if region2 in region1_parents:
            return region2

        key = region2
        while key in region_dict:
            parent = region_dict[key]
            if parent in region1_parents:
                return parent
            key = parent

        return None

