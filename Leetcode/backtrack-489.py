# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# because we are starting at (1, 3) and when translating this into (0, 0)
# corridinate, the "up" position will be "-1". So, our directions[0] 
# must be (-1, 0)
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.backtrack(robot, 0, set(), 0, 0)

    def backtrack(self, robot, d, visited, x, y):
        visited.add((x, y))
        robot.clean()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(4):
            new_d = (d + i) % 4
            new_x = x + directions[new_d][0]
            new_y = y + directions[new_d][1]

            if (new_x, new_y) not in visited and robot.move():
                self.backtrack(robot, new_d, visited, new_x, new_y)
                
                # backtrack
                # turn back - 90degree
                robot.turnRight()
                robot.turnRight()
                # move back one step
                robot.move()
                # turn again to maintian the direction
                robot.turnRight()
                robot.turnRight()

            # change to another direction
            robot.turnRight()