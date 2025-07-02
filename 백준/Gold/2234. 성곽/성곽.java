import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int beforeN,beforeM,N,M;
    static int[][] firstGraph, graph, idGraph;
    static boolean[][] visited;

    static int[] oneDeltaX = {0,1,0,-1};
    static int[] oneDeltaY = {1,0,-1,0};
    static int[] twoDeltaX = {0,2,0,-2};
    static int[] twoDeltaY = {2,0,-2,0};
    
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        beforeM = Integer.parseInt(token.nextToken());
        beforeN = Integer.parseInt(token.nextToken());
        firstGraph = new int[beforeN][beforeM];
        for (int i = 0; i < beforeN; i++) {
            token = new StringTokenizer(input.readLine());
            for (int j = 0; j < beforeM; j++) {
                firstGraph[i][j] = Integer.parseInt(token.nextToken());
            }
        }

        N = beforeN*2+1; M = beforeM*2+1;
        graph = new int[N][M]; // -1: 벽, -2: 벽x, -9: 상관x, 나머지: roomID
        for (int i = 0; i < beforeN; i++) {
            for (int j = 0; j < beforeM; j++) {
                String bits = Integer.toBinaryString(firstGraph[i][j]);
                bits = String.format("%4s", bits).replace(' ', '0');
                for (int k = 0; k < 4; k++) {
                    if (bits.charAt(k) == '1') {
                        graph[i*2+oneDeltaY[k]+1][j*2+oneDeltaX[k]+1] = -1;
                    }else{
                        graph[i*2+oneDeltaY[k]+1][j*2+oneDeltaX[k]+1] = -2;
                    }
                }
            }
        }

        visited = new boolean[N][M];
        int id = 0;
        List<Integer> sizeList = new ArrayList<>();
        sizeList.add(0); // dummy
        for (int i = 1; i < N; i = i+2) {
            for (int j = 1; j < M; j = j+2) {
                if (graph[i][j] != 0) continue;
                id ++;
                int size = 0;
                Deque<int[]> deq = new ArrayDeque<>();
                deq.addLast(new int[]{j,i});
                graph[i][j] = id;
                visited[i][j] = true;
                while (!deq.isEmpty()) {
                    int[] cur = deq.pollFirst();
                    size++;
                    int x = cur[0];
                    int y = cur[1];
                    for (int k = 0; k < 4; k++) {
                        int deltaOneX = x + oneDeltaX[k];
                        int deltaOneY = y + oneDeltaY[k];
                        int deltaTwoX = x + twoDeltaX[k];
                        int deltaTwoY = y + twoDeltaY[k];

                        if (graph[deltaOneY][deltaOneX] == -1) continue;
                        if (visited[deltaTwoY][deltaTwoX]) continue;

                        deq.addLast(new int[]{deltaTwoX,deltaTwoY});
                        graph[deltaTwoY][deltaTwoX] = id;
                        visited[deltaTwoY][deltaTwoX] = true;
                    }
                }
                sizeList.add(size);
            }
        }

        int max = Integer.MIN_VALUE;
        for (int i = 1; i < N-1; i++) {
            for (int j = 1; j < M-1; j++) {
                if (graph[i][j] != -1) continue;
                int[] tempIds = new int[]{-1,-1};
                for (int k = 0; k < 4; k++) {
                    int dx = j + oneDeltaX[k];
                    int dy = i + oneDeltaY[k];
                    if (graph[dy][dx] == 0) continue;
                    if (tempIds[0] == -1) tempIds[0] = graph[dy][dx];
                    else tempIds[1] = graph[dy][dx];
                }
                if (tempIds[0] != tempIds[1]) {
                    int sumSize = sizeList.get(tempIds[0]) + sizeList.get(tempIds[1]);
                    if (sumSize > max) max = sumSize;
                }
            }
        }
        
        sb.append(sizeList.size()-1).append("\n");
        int beforeMax = 0;
        for (int i = 1; i < sizeList.size(); i++) {
            if (sizeList.get(i) > beforeMax) beforeMax = sizeList.get(i);
        }
        sb.append(beforeMax).append("\n");
        sb.append(max);
        System.out.println(sb);
    }
}