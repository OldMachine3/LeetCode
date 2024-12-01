class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowr = len(flowerbed)
        for i in range(flowr):
            if n <= 0:
                break
            prev  = i == 0 or flowerbed[i - 1] == 0
            fut = i == flowr - 1 or flowerbed[i + 1] == 0
            if prev and fut and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0