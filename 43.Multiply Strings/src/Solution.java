public class Solution {
    public String multiply(String num1, String num2) {
        int m=num1.length(), n=num2.length(), zero=0;
        int[] a = new int[m], c = new int[m+n];
        for(int i=0,k=m; i<m; i++) a[--k]=num1.charAt(i)-'0';
        for(int i=n-1; i>=0; i--)
            add(c,a,num2.charAt(i)-'0',zero++);
        System.out.println(c);
        carry(c);
        int i=m+n;
        while(i>0 && c[--i]==0);
        i++;
        StringBuilder ret = new StringBuilder(i);
        while(i>0) ret.append((char)(c[--i]+'0'));
        return ret.toString();
    }
    
    void carry(int[] a){
        int i;
        for(int k=0,d=0; k<a.length; k++){
            i=a[k]+d;
            a[k]=i%10;
            d=i/10;
        }
    }
    
    void add(int[] c, int[] a, int b, int zero){
        for(int i=zero,j=0; j<a.length; j++,i++){
            c[i]+=a[j]*b;
            System.out.println(a[j]);
            System.out.println(b);
        	System.out.println(c[i]);
        }
    }
    
    public static void main(String[] args) {
		Solution s = new Solution();
		System.out.println(s.multiply("45", "67"));
	}
}