package graphs1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/*
 * Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using DFS and print the first path that you encountered.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
Note : Save the input graph in Adjacency Matrix.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
Line (E+2) : Two integers v1 and v2 (separated by space)
Output Format :
Path from v1 to v2 in reverse order (separated by space)
Constraints :
2 <= V <= 1000
1 <= E <= 1000
0 <= v1, v2 <= V-1
Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3
Sample Output 1 :
3 0 1
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3
Sample Output 2 :

 */
public class Code_Get_Path_DFS {
	public static ArrayList<Integer> DFS(int[][] graph,int start,int end,int[] visited) {
		ArrayList<Integer> temp = new ArrayList<Integer>();
		visited[start] = 1;
		for (int i = 0; i < visited.length; i++) {
			if(visited[i]==0 && graph[start][i]==1) {
				if(end==i) {
					temp.add(i);//this is the final place where we need to be
					temp.add(start);// this is from where we got here
					return temp;
				}
				temp = DFS(graph, i, end, visited);
				if(!temp.isEmpty()) {
					temp.add(start);//because we found a way using this start so this should be in path
					return temp;
				}
			}
		}
		return temp;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sf = new Scanner(System.in);
		int n = sf.nextInt();
		int e = sf.nextInt();
		int[][] graph = new int[n][n];
		for (int i = 0; i < graph.length; i++) {
			Arrays.fill(graph[i], 0);
		}
		for (int i = 0; i < e; i++) {
			int from = sf.nextInt();
			int to = sf.nextInt();
			graph[from][to] = 1;
			graph[to][from] = 1;
		}
		int start = sf.nextInt();
		int end = sf.nextInt();
		int[] visited = new int[graph.length];
		Arrays.fill(visited, 0);
		ArrayList<Integer> temp = DFS(graph, start, end, visited);
		for (int i = 0; i < temp.size(); i++) {
			System.out.print(temp.get(i)+" ");
		}
		sf.close();
	}

}
