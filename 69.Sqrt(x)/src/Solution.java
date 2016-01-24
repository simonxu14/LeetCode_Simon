public class Solution {
    public int mySqrt(int x) {
        int l = 1;
        int r = x;
        int mid = 0;
        while (l <= r) {
        	mid = (l + r)/2;
        	if (mid<= x/mid && x/(mid+1) < (mid+1))
        		return mid;
        	else if (x/mid < mid)
        		r = mid;
        	else
        		l = mid + 1;
        }
        return 0;
    }
    
//    public int mySqrt(int x) {
//        if(x <= 0) return x;
//        int low = 1, high = x/2;
//        while (low < high){
//            int mid = low + (high - low) / 2;
//            if(mid == x/mid) {low = mid; break;} 
//            else if(mid > x/mid) high = mid;
//            else if(mid < x/mid && (mid+1) <= x/(mid+1)) low = mid + 1;
//            else if(mid < x/mid && (mid+1) > x/(mid+1)) {low = mid; break;}
//        }
//        return low;
//    }
    
    
    
    
    
    public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(s.mySqrt(2147395599));
		
	}
}