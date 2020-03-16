package graphs1;

import java.beans.Visibility;
import java.util.Arrays;
import java.util.Scanner;

/*
 * Connecting Dots
Send Feedback
Gary has a board of size NxM. Each cell in the board is a coloured dot. 
There exist only 26 colours denoted by uppercase Latin characters (i.e. A,B,...,Z). 
Now Gary is getting bore and wants to play a game. The key of this game is to find 
a cycle that contain dots of same colour. Formally, we call a sequence of
 dots d1, d2, ..., dk a cycle if and only if it meets the following condition:
1. These k dots are different: if i ≠ j then di is different from dj.
2. k is at least 4.
3. All dots belong to the same colour.
4. For all 1 ≤ i ≤ k - 1: di and di + 1 are adjacent. Also, dk and d1 should also be adjacent. Cells x and y are called adjacent if they share an edge.
Since Gary is colour blind, he wants your help. Your task is to determine if there 
exists a cycle on the board.
Assume input to be 0-indexed based.
Input Format :
Line 1 : Two integers N and M, the number of rows and columns of the board
Next N lines : a string consisting of M characters, expressing colors of dots in 
each line. Each character is an uppercase Latin letter.
Output Format :
Return 1 if there is a cycle else return 0
Constraints :
2 ≤ N, M ≤ 50
Sample Input :
3 4
AAAA
ABCA
AAAA
Sample Output :
1
 */
public class Connecting_dots {
	public static void finder(String[][] graph,int x,int y,int k,String s1,int[][] visited) {
		if(k!=0) {
			if(graph[x][y].equals(s1) && visited[x][y] == 0) {
				visited[x][y] = 1;
				finder(graph, x+1, y, k, s1, visited);
				finder(graph, x, y+1, k, s1, visited);
				finder(graph, x, y-1, k, s1, visited);
				finder(graph, x-1, y, k, s1, visited);
			}
		}
		else {
			if(graph[x][y].equals(s1) && visited[x][y] == 0) {
				visited[x][y] = 1;
				finder(graph, x+1, y, k, s1, visited);
				finder(graph, x, y+1, k, s1, visited);
				finder(graph, x, y-1, k, s1, visited);
				finder(graph, x-1, y, k, s1, visited);
			}
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sf = new Scanner(System.in);
		int n = sf.nextInt();
		int m = sf.nextInt();
		String[][] graph= new String[n][m];
		for (int i = 0; i < graph.length; i++) {
			graph[i] = sf.next().split("");
		}
		int[][] visited = new int[n][m];
		for (int i = 0; i < visited.length; i++) {
			Arrays.fill(visited[i], 0);
		}
		sf.close();
		
	}

}
