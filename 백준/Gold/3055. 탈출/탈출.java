import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static char[][] graph;
    static boolean safe;

    static int[] deltaX = {0,0,-1,1};
    static int[] deltaY = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        graph = new char[N][M];
        for (int i = 0; i < N; i++) {
            String s = input.readLine();
            graph[i] = s.toCharArray();
        }
        safe = false;
        int cnt = 0;
        while (true){
            cnt++;
            move();
            if (safe){
                break;
            }
            spread();
            if (!isAlive()){
                break;
            }
        }
        if (safe){
            System.out.println(cnt);
        }else{
            System.out.println("KAKTUS");
        }
    }
    public static void move(){
        boolean[][] visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j] && graph[i][j] == 'S') {
                    for (int k=0; k<4; k++){
                        int dx = j+deltaX[k];
                        int dy = i+deltaY[k];
                        if (isValid(dx,dy) && graph[dy][dx] == '.') {
                            graph[dy][dx] = 'S';
                            visited[dy][dx] = true;
                        } else if (isValid(dx,dy) && graph[dy][dx] == 'D'){
                            safe = true;
                            return;
                        }
                    }
                }
            }
        }
    }
    public static void spread(){
        boolean[][] visited = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j] && graph[i][j] == '*') {
                    for (int k=0; k<4; k++){
                        int dx = j+deltaX[k];
                        int dy = i+deltaY[k];
                        if (isValid(dx,dy) && (graph[dy][dx] == '.' || graph[dy][dx] == 'S')) {
                            graph[dy][dx] = '*';
                            visited[dy][dx] = true;
                        }
                    }
                }
            }
        }
    }
    public static boolean isAlive(){
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph[i][j] == 'S') {
                    return true;
                }
            }
        }
        return false;
    }
    public static boolean isValid(int x, int y){
        return x>=0 && x<M && y>=0 && y<N;
    }
}