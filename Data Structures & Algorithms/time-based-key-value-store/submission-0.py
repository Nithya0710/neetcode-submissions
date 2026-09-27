class TimeMap:

    def __init__(self):
        self.timeMap={}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key]=[]
        self.timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        nums=self.timeMap[key]
        l, r=0, len(nums)-1
        ans=""
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid][0]<=timestamp:
                ans=nums[mid][1]
                l=mid+1
            elif nums[mid][0]>timestamp:
                r=mid-1
        return ans