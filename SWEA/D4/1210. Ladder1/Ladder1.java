import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
 
public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
 
    public static void main(String[] args) throws IOException {
        for (int t = 1; t < 11; t++) {
            String a = input.readLine();
            int[][] graph = new int[100][100];
            int idxX = -1;
            int idxY = -1;
            for (int i=0; i<100; i++){
                tokens = new StringTokenizer(input.readLine());
                for (int j=0; j<100; j++){
                    int temp = Integer.parseInt(tokens.nextToken());
                    if (temp==2){
                        idxX = j;
                        idxY = i;
                    }
                    graph[i][j] = temp;
                }
            }
            boolean[][] visited = new boolean[100][100];
            visited[idxY][idxX] = true;
 
            while (idxY != 0){
                if (idxX-1 >= 0){
                    if (!visited[idxY][idxX-1] && graph[idxY][idxX-1] == 1){
                        idxX --;
                        visited[idxY][idxX] = true;
                    }
                }
                if (idxX+1 != 100){
                    if (!visited[idxY][idxX+1] && graph[idxY][idxX+1] == 1){
                        idxX ++;
                        visited[idxY][idxX] = true;
                    }
                }
                if (idxY-1 >= 0){
                    if (!visited[idxY-1][idxX] && graph[idxY-1][idxX] == 1){
                        idxY --;
                        visited[idxY][idxX] = true;
                    }
                }
 
            }
            sb.append("#").append(t).append(" ").append(idxX);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}