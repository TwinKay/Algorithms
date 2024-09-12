import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M,res;
    static char[][] graph;
    static boolean[][] visited;
    static boolean[] isKeys;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t=0; t<T; t++) {
            token = new StringTokenizer(input.readLine());
            N = Integer.parseInt(token.nextToken());
            M = Integer.parseInt(token.nextToken());

            graph = new char[N+2][M+2];
            for (int i=0; i<M+2; i++){
                graph[0][i] = '.';
                graph[N+1][i] = '.';
            }
            for (int i=1; i<N+1; i++){
                String s = input.readLine();
                for (int j=0; j<M+2; j++){
                    if (j==0 || j==M+1) {
                        graph[i][j] = '.';
                    }
                    else{
                        graph[i][j] = s.charAt(j-1);
                    }
                }
            }
            isKeys = new boolean[26];
            String k = input.readLine();
            if (!k.equals("0")){
                for (int i=0; i<k.length(); i++){
                    isKeys[k.charAt(i) - 'a'] = true;
                }
            }

            res = 0;
            boolean isEnd = false;
            while (!isEnd){
                isEnd = bfs(0,0);
            }
            sb.append(res).append('\n');
        }
        System.out.println(sb);
    }
    public static boolean bfs(int firstX, int firstY){
        visited = new boolean[N+2][M+2];

        Deque<int[]> deq = new ArrayDeque<>();
        deq.addLast(new int[]{firstX, firstY});
        visited[firstY][firstX] = true;
        while (!deq.isEmpty()){
            int[] cur = deq.pollFirst();
            int x = cur[0];
            int y = cur[1];
            for (int i=0; i<4; i++){
                int dx = x+deltaX[i];
                int dy = y+deltaY[i];

                if (isValid(dx,dy)&&!visited[dy][dx]){
                    if (graph[dy][dx]=='.'){
                        deq.addLast(new int[]{dx,dy});
                        visited[dy][dx] = true;
                    } else if (graph[dy][dx]=='*'){
                        visited[dy][dx] = true;
                    } else if (graph[dy][dx]=='$'){
                        graph[dy][dx] = '.';
                        deq.addLast(new int[]{dx,dy});
                        visited[dy][dx] = true;
                        res ++;
                    } else{
                        if (isUpper(graph[dy][dx])){
                            if (isKeys[graph[dy][dx]-'A']){
                                graph[dy][dx] = '.';
                                deq.addLast(new int[]{dx,dy});
                                visited[dy][dx] = true;
                            } else{
                                visited[dy][dx] = true;
                            }
                        } else{
                            isKeys[graph[dy][dx]-'a'] = true;
                            graph[dy][dx] = '.';
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
    public static boolean isValid(int x, int y){
        return y>=0 && y<N+2 && x>=0 && x<M+2;
    }
    public static boolean isUpper(char c){
        int y = c - 'a';
        if (y>=0 && y<=25){
            return false;
        } else{
            return true;
        }
    }
}