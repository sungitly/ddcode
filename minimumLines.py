"""
An airline company wishes to establish a flight service in a new country. The company wants to provide flight service in such a way that will cover all the cities in the country with a minimum number of flights. Given the coordinates of all the cities in the country, the company has to determine the minimum number of straight routes necessary to cover all the cities. Write an algorithm to help the company find the minimum number of straight routes necessary to cover all the cities.

Input
The first line of the input consists of: two space-separated integers: numCities, representing the number of cities in the country(N). The next N lines consist of two space-separated integers: coordX and coordY representing the X and Y coordinates of the cities, respectively.

Output
Print an integer representing the minimum number of straight routes necessary to cover all the cities.

Constraints
0 <= numCitiess <= 10^4
-100 <= coordX, coordY <= 100

Example
Input:
8 2
1 4
2 3
2 1
3 2
4 1
5 0
4 3
5 4

Output:
2

Explanation:

The points (2,1)(3,2)((4,3)(5,4) fall on a straight line and the points (1,4)(2,3)(3,2)(4,1)(5,0) fall on another straight line.
"""
from typing import List


class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)

        def is_line(i1: int, i2: int, i3: int) -> bool:
            x1, y1 = points[i1]
            x2, y2 = points[i2]
            x3, y3 = points[i3]
            return (x2 - x1) * (y3 - y2) == (x3 - x2) * (y2 - y1)

        def dp(state: int) -> int:
            i = j = -1
            tmp, cnt = state, 0
            while tmp:
                if tmp & 1:
                    i, j, k = cnt, i, j
                    if k > -1 and not is_line(i, j, k):
                        break
                tmp >>= 1
                cnt += 1
            if tmp == 0:
                return 1
            sub, end = state & (state - 1), state >> 1
            res = n
            while sub > end:
                res = min(res, dp(sub) + dp(state - sub))
                sub = (sub - 1) & state
            return res

        return dp((1 << n) - 1)


if __name__ == '__main__':
    solution = Solution()

    params = [[1, 4], [2, 3], [2, 1], [3, 2], [4, 1], [5, 0], [4, 3], [5, 4]]
    # params = [[0, 2], [-2, -2], [1, 4]]
    print(solution.minimumLines(params))
