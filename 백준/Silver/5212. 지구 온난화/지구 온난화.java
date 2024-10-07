import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M, minX, maxX, minY, maxY;
    static char[][] graph, newGraph, smallGraph;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new char[N+2][M+2];
        for (char[] g: graph) {
            Arrays.fill(g,'.');
        }
        for (int i=1; i<=N; i++) {
            String s = input.readLine();
            for (int j=1; j<=M; j++) {
                graph[i][j] = s.charAt(j-1);
            }
        }
        minX = Integer.MAX_VALUE;
        maxX = Integer.MIN_VALUE;
        minY = Integer.MAX_VALUE;
        maxY = Integer.MIN_VALUE;
        newGraph = new char[N+2][M+2];
        for (char[] g: newGraph) {
            Arrays.fill(g,'.');
        }
        for (int i=1; i<=N; i++) {
            for (int j=1; j<=M; j++) {
                if(graph[i][j] == 'X') {
                    int cnt = 0;
                    for (int k=0; k<4; k++){
                        int dx = j+deltaX[k];
                        int dy = i+deltaY[k];
                        if (graph[dy][dx]=='.'){
                            cnt++;
                        }
                    }
                    if (cnt<=2){
                        newGraph[i][j]='X';
                        if (j<minX){
                            minX = j;
                        }
                        if (j>maxX){
                            maxX = j;
                        }
                        if (i<minY){
                            minY = i;
                        }
                        if (i>maxY){
                            maxY = i;
                        }
                    }
                }
            }
        }
        smallGraph = new char[maxY-minY+1][maxX-minX+1];
        for (int i=minY; i<=maxY; i++) {
            for (int j=minX; j<=maxX; j++) {
                smallGraph[i-minY][j-minX] = newGraph[i][j];
            }
        }

        for (char[] g:smallGraph){
            for (char c:g){
                sb.append(c);
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}