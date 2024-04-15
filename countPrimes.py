"""
A prime number is divisible only by 1 and itself. The teacher writes a positive integer on the board. Write an algorithm to find all the prime numbers from 2 to the given positive number. Input: The first line of the input consists of an integer num, representing the number written on the board. Output: Print space-separated integers representing the prime numbers requested by the teacher in increasing order. If no prime number exists within the given range, then do not print anything. Constraints: num < 10^9 Example Input: Input: 235711 Explanation: For the given number, the prime numbers are 2, 3, 5, 7, and 11.
A prime number is divisible only by 1 and itself. The teacher writes a positive integer on the board. Write an algorithm to find all the prime numbers from 2 to the given positive number.

Input: The first line of the input consists of an integer num, representing the number written on the board.

Output: Print space-separated integers representing the prime numbers requested by the teacher in increasing order. If no prime number exists within the given range, then do not print anything.

Constraints: num < 10^9

Example Input:
Input: 11

Explanation: For the given number, the prime numbers are 2, 3, 5, 7, and 11.
"""
from typing import List


class Solution:
    def countPrimes(self, n: int) -> List[int]:
        primes = []

        # 定义数组标记是否是质数
        is_prime = [1] * (n + 1)

        count = 0
        for i in range(2, n + 1):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                primes.append(i)
                # 从 i*i 开始标记
                for j in range(i * i, n, i):
                    is_prime[j] = 0

        return primes


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(11))
