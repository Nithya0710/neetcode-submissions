class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        fleet=sorted(zip(position, speed), reverse=True)
        for p, s in fleet:
            time=(target-p)/s
            if not stack:
                stack.append(time)
            elif time>stack[-1]:
                stack.append(time)
        return len(stack)