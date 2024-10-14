import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static BufferedReader input= new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M,K,T;
    static Map<String, Cell> graph;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(input.readLine());
        for (int t=1; t<=T; t++){
            token = new StringTokenizer(input.readLine());
            N = Integer.parseInt(token.nextToken());
            M = Integer.parseInt(token.nextToken());
            K = Integer.parseInt(token.nextToken());
            graph = new HashMap<>();
            List<Cell> activeCells = new ArrayList<>();
            List<Cell> unActiveCells = new ArrayList<>();

            int gapX = K + M;
            int gapY = K + N;
            for (int i = 0; i < N; i++){
                token = new StringTokenizer(input.readLine());
                for (int j = 0; j < M; j++){
                    int temp = Integer.parseInt(token.nextToken());
                    if (temp != 0){
                        int x = j + gapX;
                        int y = i + gapY;
                        Cell cell = new Cell(x, y, temp);
                        graph.put(cell.getKey(), cell);
                        unActiveCells.add(cell);
                    }
                }
            }

            for (int time = 1; time <= K; time++){
                List<Cell> newActiveCells = new ArrayList<>();
                List<Cell> reproducingCells = new ArrayList<>();
                Map<String, Cell> newCells = new HashMap<>();

                for (Cell cell: unActiveCells){
                    cell.unActiveCnt--;
                    if (cell.unActiveCnt == 0){
                        newActiveCells.add(cell);
                    }
                }
                for (Cell cell: activeCells){
                    cell.activeCnt--;
                    if (cell.activeCnt == cell.hp - 1){
                        reproducingCells.add(cell);
                    }
                }

                for (Cell cell : reproducingCells){
                    int[] deltaX = {1, 0, -1, 0};
                    int[] deltaY = {0, 1, 0, -1};
                    for (int i = 0; i < 4; i++){
                        int nx = cell.x + deltaX[i];
                        int ny = cell.y + deltaY[i];
                        StringBuilder tempSb = new StringBuilder();
                        tempSb.append(nx).append(",").append(ny);
                        String key = tempSb.toString();
                        if (!graph.containsKey(key) && !newCells.containsKey(key)){
                            Cell newCell = new Cell(nx, ny, cell.hp);
                            newCells.put(key, newCell);
                        } else if (newCells.containsKey(key)){
                            if (newCells.get(key).hp < cell.hp){
                                newCells.get(key).hp = cell.hp;
                                newCells.get(key).activeCnt = cell.hp;
                                newCells.get(key).unActiveCnt = cell.hp;
                            }
                        }
                    }
                }

                for (Cell cell : newCells.values()){
                    graph.put(cell.getKey(), cell);
                    unActiveCells.add(cell);
                }

                activeCells.addAll(newActiveCells);
            }

            int cnt = 0;
            for (Cell cell : graph.values()){
                if (cell.unActiveCnt > 0 || cell.activeCnt > 0){
                    cnt++;
                }
            }
            sb.append("#").append(t).append(" ").append(cnt).append("\n");
        }
        System.out.println(sb);
    }
}

class Cell{
    int x, y;
    int activeCnt;
    int unActiveCnt;
    int hp;

    Cell(int x, int y, int hp){
        this.x = x;
        this.y = y;
        this.hp = hp;
        this.activeCnt = hp;
        this.unActiveCnt = hp;
    }

    public String getKey(){
        StringBuilder tempSb = new StringBuilder();
        tempSb.append(x).append(",").append(y);
        return tempSb.toString();
    }

    @Override
    public String toString() {
        return "[" + activeCnt + "_" + unActiveCnt + "_" + hp +"]";
    }
}