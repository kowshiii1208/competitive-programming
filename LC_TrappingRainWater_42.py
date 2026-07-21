class Solution:
    def trap(self, height: List[int]) -> int:
        lef_max=[0]*len(height)
        rig_max=[0]*len(height)
        l_max=r_max=0
        res=0
        for i in range(len(height)):
            l_max=max(l_max,height[i])
            lef_max[i]=l_max
        for j in range(len(height)-1,-1,-1):
            r_max=max(r_max,height[j])
            rig_max[j]=r_max
        for i in range(len(height)):
            val=min(lef_max[i],rig_max[i])-height[i]
            if val>0:
                res+=val
        return res
