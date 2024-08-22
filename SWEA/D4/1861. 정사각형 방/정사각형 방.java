import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();
 
    static int n;
    static int[][] graph;
    static boolean[][] visited;
 
    static int[] deltaX = {1, -1, 0, 0};
    static int[] deltaY = {0, 0, -1, 1};
 
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t=1; t<=T; t++) {
            n = Integer.parseInt(input.readLine());
            graph = new int[n][n];
            visited = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(token.nextToken());
                }
            }
            int resStart = Integer.MAX_VALUE;
            int resSize = -1;
 
            flag:
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j]) {
                        int[] temp = bfs(j, i);
                        int start = temp[0];
                        int size = temp[1];
 
                        if (size > resSize){
                            resSize = size;
                            resStart = start;
                        } else if (size == resSize){
                            if (start < resStart){
                                resStart = start;
                            }
                        }
 
                        if (resSize > n*n/2) break flag;
 
                    }
                }
            }
            sb.append("#").append(t).append(" ").append(resStart).append(" ").append(resSize).append("\n");
        }
        System.out.println(sb);
    }
    public static int[] bfs(int firstX, int firstY){
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Deque<int[]> deq = new ArrayDeque<>();
        deq.push(new int[]{firstX, firstY});
        visited[firstY][firstX] = true;
        pq.add(graph[firstY][firstX]);
 
        while (!deq.isEmpty()){
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            int num = graph[y][x];
 
            for (int i = 0; i < 4; i++) {
                int delX = x + deltaX[i];
                int delY = y + deltaY[i];
                if (checkIdx(delX, delY) && checkUpDownNum(num, graph[delY][delX]) && !visited[delY][delX]) {
                    pq.add(graph[delY][delX]);
                    deq.push(new int[]{delX, delY});
                    visited[delY][delX] = true;
                }
            }
        }
        return new int[] {pq.peek(),pq.size()};
    }
    public static boolean checkIdx(int x, int y){
        return x >= 0 && x < n && y >= 0 && y < n;
    }
    public static boolean checkUpDownNum(int nowNum, int nextNum){
        return nextNum == nowNum-1 || nextNum == nowNum+1;
    }
}