import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int r;
    static int c;
    static boolean[][] graph;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        r = Integer.parseInt(token.nextToken());
        c = Integer.parseInt(token.nextToken());

        graph = new boolean[r][c];
        for (int i = 0; i < r; i++) {
            String t = input.readLine();
            for (int j = 0; j < c; j++) {
                if (t.charAt(j) == 'x'){
                    graph[i][j] = true;
                }
            }
        }

        for (int i = 0; i < r; i++) {
            dfs(0,i);
        }

        int cnt = 0;
        for (int i = 0; i < r; i++) {
            if (graph[i][c-1]){
                cnt ++;
            }
        }
        System.out.println(cnt);
    }

    public static void dfs(int firstX, int firstY){
        List<int[]> path = new ArrayList<>();
        path.add(new int[]{firstX, firstY});
        graph[firstY][firstX] = true;
        int[] deltaY = {-1,0,1};

        flag:
        while(!path.isEmpty()){
            int[] cur = path.get(path.size()-1);
            int x = cur[0]; int y = cur[1];
            if (x+1 == c) break flag;
            boolean isFind = false;
            for (int delY : deltaY){
                if (checkIdx(x+1,y+delY) && !graph[y+delY][x+1]) {
                    path.add(new int[]{x+1,y+delY});
                    graph[y+delY][x+1] = true;
                    isFind = true;
                    break;
                }
            }

            if (!isFind){
                path.remove(path.size()-1);
            }
        }
    }

    public static boolean checkIdx(int x, int y){
        if (x>=0 && x<c && y>=0 && y<r){
            return true;
        }
        return false;
    }
}