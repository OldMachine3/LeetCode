class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        hand_size = len(hand)
        if hand_size % groupSize != 0:
            return False
        
        # counter to store the count of each card value
        card_count = Counter(hand)

        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)


        while min_heap:
            current_card = min_heap[0]
            for i in range(groupSize):
                if card_count[current_card + i] == 0:
                    return False
                card_count[current_card + i] -= 1
                if card_count[current_card + i] == 0:
                    if current_card + i != heapq.heappop(min_heap):
                        return False
        return True