// 일부러 순열로 풀어보기!! 순열 복습할 겸...

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer token;
	static StringBuilder sb = new StringBuilder();
	static Set<String> perms = new HashSet<>();
	static int[][] graph = new int[5][5];
	static int[] permSource = {1,2,3,4};
	static Set<String> res = new HashSet<>();
	
	public static void main(String[] args) throws IOException {
		// graph 생성 
		for (int i=0; i<5; i++) {
			token = new StringTokenizer(input.readLine());
			for (int j=0; j<5; j++) {
				graph[i][j] = Integer.parseInt(token.nextToken());
			}
		}
		
		// 순열 index로 돌릴 delta 생성 
		int[][] deltas = {{0,0},{0,1},{0,-1},{1,0},{-1,0}};
		
		Perm(0, new int[5]);
		
		List<char[]> order = new LinkedList<>();
		for (Object perm: perms.toArray()) {
			order.add(perm.toString().toCharArray());
		}
		
		
		for (int y=0; y<5; y++) {
			for (int x=0; x<5; x++) {
				for (char[] ord : order) {
					String str = "";
					int idxX = x;
					int idxY = y;
					
					for (char c : ord) {
						if (idxX+deltas[Character.getNumericValue(c)][0]>=0 && idxX+deltas[Character.getNumericValue(c)][0]<5 && idxY+deltas[Character.getNumericValue(c)][1]>=0 && idxY+deltas[Character.getNumericValue(c)][1]<5) {
							str += graph[idxY+deltas[Character.getNumericValue(c)][1]][idxX+deltas[Character.getNumericValue(c)][0]];
						}
						idxX += deltas[Character.getNumericValue(c)][0];
						idxY += deltas[Character.getNumericValue(c)][1];
						
					}
					if (str.length()==6) {
						res.add(str);
					}
				}
			}
		}
		System.out.println(res.size());

	}
	// 순열 생성 
	public static void Perm(int cnt, int[] save) {
		if (cnt == save.length) {
			perms.add("0"+save[0]+save[1]+save[2]+save[3]+save[4]);
			return;
		}
		
		for (int i=0; i<4; i++) {
			save[cnt] = permSource[i];
			Perm(cnt+1,save);
		}
	}
}