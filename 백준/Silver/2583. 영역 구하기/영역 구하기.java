import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer token;
	static StringBuilder sb = new StringBuilder();
	
	static int m,n,k;
	static boolean[][] graph, visited;
	static List<Integer> resArr;
	
	static int[] deltaX = {0,0,1,-1};
	static int[] deltaY = {1,-1,0,0};


	public static void main(String[] args) throws IOException {
		token = new StringTokenizer(input.readLine());
		m = Integer.parseInt(token.nextToken());
		n = Integer.parseInt(token.nextToken());
		k = Integer.parseInt(token.nextToken());
		
		graph = new boolean[m][n];
		visited = new boolean[m][n];
		for (int t=0; t<k; t++) {
			token = new StringTokenizer(input.readLine());
			int x1 = Integer.parseInt(token.nextToken());
			int y1 = Integer.parseInt(token.nextToken());
			int x2 = Integer.parseInt(token.nextToken());
			int y2 = Integer.parseInt(token.nextToken());
			
			for (int i=y1; i<y2; i++) {
				for (int j=x1; j<x2; j++) {
					graph[i][j] = true;
				}
			}
		}
		resArr = new ArrayList<>();
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				if (!visited[i][j] && !graph[i][j]) {
					int cnt = 0;
					Deque<int[]> deq = new ArrayDeque();
					deq.addLast(new int[] {j,i});
					cnt++;
					visited[i][j] = true;
					
					while(!deq.isEmpty()) {
						int[] cur = deq.pollFirst();
						int x = cur[0];
						int y = cur[1];
						
						for (int d=0; d<4; d++) {
							int dx = x+deltaX[d];
							int dy = y+deltaY[d];
							
							if (isValid(dx, dy) && !graph[dy][dx] && !visited[dy][dx]) {
								deq.addLast(new int[] {dx,dy});
								cnt++;
								visited[dy][dx] = true;
							}
						}
						
					}
					resArr.add(cnt);
				}
			}
		}
		Collections.sort(resArr);
		sb.append(resArr.size()).append("\n");
		for (int a : resArr) {
			sb.append(a).append(" ");
		}
		System.out.println(sb);
		
	}
	public static boolean isValid(int x, int y) {
		return x>=0 && y>=0 && x<n && y<m;
	}
}