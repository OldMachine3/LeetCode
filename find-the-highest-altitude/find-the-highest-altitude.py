class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alti = 0
        nilai_tertinggi = cur_alti

        for i in gain:
            cur_alti += i
            nilai_tertinggi = max(nilai_tertinggi, cur_alti)

        return nilai_tertinggi
