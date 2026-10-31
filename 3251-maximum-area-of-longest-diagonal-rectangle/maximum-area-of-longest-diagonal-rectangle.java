class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int n = dimensions.length;
        int ma = 0, md = 0;
        for(int i = 0; i<n; i++){
            int l = dimensions[i][0];
            int w = dimensions[i][1];
            int cd = l*l + w*w;
            if (cd>md || (cd == md && l*w > ma)){
                md = cd;
                ma = l*w;
            }
        }
        return ma;
    }
}