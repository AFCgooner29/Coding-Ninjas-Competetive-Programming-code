package bit_manipulation;

import java.util.Scanner;

public class Unset_ith {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sf = new Scanner(System.in);
		int a  = sf.nextInt();
		int b  = sf.nextInt();
		int c = 1<<b;
		c = ~c;
		System.out.println(a & c);
		sf.close();
	}

}
