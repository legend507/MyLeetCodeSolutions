
HASH_MULTIPLIER = (60001  # Slightly larger than 2 * max coordinate value
)

class Solution:
    def _turn(self, facing: str, command: int) -> str:
        new_facing = None
        if facing == 'north':
            if -2 == command: # Turn left.
                new_facing = 'west'
            elif -1 == command:
                new_facing = 'east'
        elif facing == 'south':
            if -2 == command:
                new_facing = 'east'
            if -1 == command:
                new_facing = 'west'
        elif facing == 'west':
            if -2 == command: # Turn left.
                new_facing = 'south'
            if -1 == command:
                new_facing = 'north'
        elif facing == 'east':
            if -2 == command: # Turn left.
                new_facing = 'north'
            if -1 == command:
                new_facing = 'south'
        return new_facing

    def _move(self, facing, command, obstacles_set, x, y):
        while command != 0:
            next_x, next_y = None, None
            if facing == 'north':
                next_x, next_y = x, y + 1
            if facing == 'south':
                next_x, next_y = x, y - 1
            if facing == 'east':
                next_x, next_y = x + 1, y
            if facing == 'west':
                next_x, next_y = x - 1, y

            # Check if next x, y is an obstacle. If so, don't move.
            if self._check_is_obstacle(obstacles_set, next_x, next_y):
                return x, y, True
            # If not obstacle, move 1 step.
            else:
                x, y = next_x, next_y

            command = command - 1
        return x, y, False

    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + HASH_MULTIPLIER * y
    def _check_is_obstacle(self, obstacles_set, x, y) -> bool:
        return self._hash_coordinates(x, y) in obstacles_set

    def _calc_dist(self, x, y):
        return ( (x)**2 + (y)**2 )

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # To make it faster by hashing the obstacle.
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        # List to record Euclidean dist at every step.
        result = []
        # Current coordinate.
        x, y = 0, 0
        facing = 'north'
        is_obstacle = False # If facing obstacle.
        for command in commands:
            if command < 0:
                facing = self._turn(facing, command)
                is_obstacle = False
            else:
                if is_obstacle is False:
                    x, y, is_obstacle = self._move(facing, command, obstacle_set, x, y)  
                    # Calculate Euclidean dist.
                    result.append(self._calc_dist(x, y))
        
        return max(result)
        

# s = Solution()
# s.robotSim(commands=[-2,-1,-2,3,7], obstacles=[[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]])

# My solution originally timeout on some test cases due to obstacle list being too long.
# Using the hashing method solves this problem.