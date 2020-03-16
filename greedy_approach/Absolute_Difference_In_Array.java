package greedy_approach;

import java.util.Arrays;
import java.util.Scanner;

/*
 * Min. Absolute Difference In Array
Send Feedback
Given an integer array A of size N, find and return the minimum absolute difference between any two elements in the array.
We define the absolute difference between two elements ai, and aj (where i != j ) is |ai - aj|.
Input format :
Line 1 : Integer N, Array Size
Line 2 : Array elements (separated by space)
Output Format :
Minimum difference
Constraints :
1 <= N <= 10^6
Sample Input :
5
2 9 0 4 5
Sample Input :
1

 */
public class Absolute_Difference_In_Array {
	
	public static int minAbsoluteDifference(int input[]) {
		/* Your class should be named Solution
		 * Don't write main().
		 * Don't read input, it is passed as function argument.
		 * Return output and don't print it.
		 * Taking input and printing output is handled automatically.
		 */
		Arrays.sort(input);
		int min_val = Integer.MAX_VALUE;
		for (int i = 1; i < input.length; i++) {
			min_val = Math.min(Math.abs(input[i]-input[i-1]), min_val);
		}
		return min_val;

	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sf = new Scanner(System.in);
		int tot = sf.nextInt();
		int[] input = new int[tot];
		for (int i = 0; i < tot; i++) {
			input[i] = sf.nextInt();
		}
		System.out.println(minAbsoluteDifference(input));
		sf.close();
	}

}
