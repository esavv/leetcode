# See: https://leetcode.com/problems/asteroid-collision/
class Solution(object):
    def asteroidCollision(self, asteroids):
        return self.soln3(asteroids)
        # return self.soln2(asteroids)
        # return self.soln1(asteroids)
    
    # stack approach, linear time
    def soln3(self, asteroids):
        ans, stack = [], []
        i = 0
        while i < len(asteroids):
            a = asteroids[i]
            if a < 0:
                ans.append(a)
            else:
                stack.append(a)
            i += 1
            while stack and i < len(asteroids):
                a = asteroids[i]
                if a > 0:
                    stack.append(a)
                    i += 1
                else:
                    if stack[-1] > -1 * a:
                        i += 1
                    elif stack[-1] < -1 * a:
                        stack.pop()
                    else:
                        i += 1
                        stack.pop()
        for a in stack:
            ans.append(a)
        return ans

    # two pointer approach, quadratic time in worst case but faster than soln1
    def soln2(self, asteroids):
        left, right = 0, 1
        while left < len(asteroids)-1 and right < len(asteroids):
            while left < len(asteroids)-1 and asteroids[left] <= 0:
                left += 1

            if left >= right:
                right = left + 1
            while right < len(asteroids) and asteroids[right] >= 0:
                right += 1
            if right >= len(asteroids):
                break

            while right > left and asteroids[right] < 0:
                tmp = right-1
                while asteroids[tmp] == 0:
                    tmp -= 1

                if asteroids[tmp] < -1 * asteroids[right]:
                    asteroids[tmp] = asteroids[right]
                    asteroids[right] = 0
                    right = tmp
                elif asteroids[tmp] > -1 * asteroids[right]: 
                    asteroids[right] = asteroids[tmp]
                    asteroids[tmp] = 0
                else:
                    asteroids[tmp] = 0
                    asteroids[right] = 0

        after = []
        for asteroid in asteroids:
            if asteroid != 0:
                after.append(asteroid)
        return after
    
    # quadratic time solution
    def soln1(self, asteroids):
        for t in range(1, len(asteroids)):
            for i in range(len(asteroids) - t):
                if asteroids[i] > 0 and asteroids[i+t] < 0:
                    if asteroids[i] > -1 * asteroids[i+t]:
                        asteroids[i+t] = 0
                    elif asteroids[i] < -1 * asteroids[i+t]:
                        asteroids[i] = 0
                    else:
                        asteroids[i+t] = 0
                        asteroids[i] = 0

        ans = []
        for a in asteroids:
            if a < 0:
                ans.append(a)
        for a in asteroids:
            if a > 0:
                ans.append(a)
        return ans