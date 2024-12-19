import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder res =  new StringBuilder();

    static int N,M,K;
    static char[][] map;
    static Map<String,Integer> hmap;
    static int[] deltaX = {-1,0,1,-1,1,-1,0,1};
    static int[] deltaY = {-1,-1,-1,0,0,1,1,1};

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        map = new char[N+8][M+8];
        for (int i = 0; i < N+8; i++) {
            Arrays.fill(map[i], '.');
        }
        for (int i = 4; i < N+4; i++) {
            String line = input.readLine();
            for (int j = 4; j < M+4; j++) {
                map[i][j] = line.charAt(j-4);
            }
        }
        fillMap();

        hmap = new HashMap<>();
        for (int i = 4; i < N+4; i++) {
            for (int j = 4; j < M+4; j++) {
                bfs(j,i);
            }
        }

        for (int i=0; i<K; i++){
            String s = input.readLine();
            Integer cnt = hmap.get(s);
            if (cnt == null){
                res.append(0).append("\n");
            }else{
                res.append(cnt).append("\n");
            }
        }
        System.out.println(res);
    }

    static private void bfs(int x, int y) {
        Deque<int[]> deq = new ArrayDeque<>();
        Deque<StringBuilder> sbDeq = new ArrayDeque<>();
        deq.addLast(new int[]{x,y});
        StringBuilder tempSb = new StringBuilder();
        tempSb.append(map[y][x]);
        sbDeq.addLast(tempSb);
        while (!deq.isEmpty()) {
            int[] cur = deq.pollFirst();
            StringBuilder sb = sbDeq.pollFirst();
            hmap.put(sb.toString(), hmap.getOrDefault(sb.toString(), 0) + 1);

            if (sb.length()<5){
                for (int i = 0; i < 8; i++) {
                    String temp = sb.toString();
                    StringBuilder nextSb = new StringBuilder();
                    nextSb.append(temp);
                    deq.addLast(new int[]{cur[0]+deltaX[i],cur[1]+deltaY[i]});
                    sbDeq.addLast(nextSb.append(map[cur[1]+deltaY[i]][cur[0]+deltaX[i]]));
                }
            }
        }
    }

    static private void fillMap(){
        for (int i = 4; i < N+4; i++) {
            for (int j = 0; j < 4; j++) {
                char left = map[i][M+j];
                int newM = M;
                while (left == '.'){
                    newM += M;
                    left = map[i][newM+j];
                }
                map[i][j] = left;
            }
        }

        for (int i = 4; i < N+4; i++) {
            for (int j = 0; j < 4; j++) {
                char right = map[i][4+j];
                map[i][M+4+j] = right;
            }
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < M + 8; j++) {
                char top = map[N+i][j];
                int newN = N;
                while (top == '.'){
                    newN += N;
                    top = map[newN+i][j];
                }
                map[i][j] = top;
            }
        }

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < M + 8; j++) {
                char bottom = map[4+i][j];
                map[N+4+i][j] = bottom;
            }
        }
    }
}