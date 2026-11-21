from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freqMap=Counter(hand)
        for card in sorted(freqMap.keys()):
            while freqMap[card]>0:
                for nextCard in range(card, card+groupSize):
                    if freqMap.get(nextCard, 0)==0:
                        return False
                    freqMap[nextCard]-=1
        return True