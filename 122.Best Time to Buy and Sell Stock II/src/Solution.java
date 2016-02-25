public class Solution {
	public int maxProfit(int[] prices) {
		if (prices.length == 0 || prices.length == 1)
			return 0;
		int result = 0;
		int current = 0;
		for (int i = 1; i < prices.length; i++) {
			if (prices[i] < prices[i-1]) {
				result = result + current;
				current = 0;
			}
			else if (prices[i] > prices[i-1]) {
				current += prices[i] - prices[i-1];
			}
		}
		result += current;
		return result;
	}
}
