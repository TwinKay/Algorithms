import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static int[][] graph;
    static List<int[]> blanks;

    public static void main(String[] args) throws IOException {
        graph = new int[9][9];
        blanks = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            String temp = input.readLine();
            for (int j = 0; j < 9; j++) {
                graph[i][j] = temp.charAt(j) - '0';
                if (graph[i][j] == 0){
                    blanks.add(new int[]{j,i});
                }
            }
        }
        recu(0);
    }
    public static void recu(int idx){
        if (idx == blanks.size()) {
            for (int[] g : graph) {
                for (int n : g){
                    sb.append(n);
                }
                sb.append("\n");
            }
            System.out.println(sb);
            System.exit(0);
        }
        int[] temp = blanks.get(idx);
        int x = temp[0]; int y = temp[1];
        for (int num=1; num<=9;num++){
            if (isContainCol(x,y,num) || isContainRow(x,y,num) || isContainBox(x,y,num)){
                continue;
            }
            graph[y][x] = num;
            recu(idx+1);
            graph[y][x] = 0;
        }
    }
    public static boolean isContainCol(int x, int y, int num){
        for (int i=0; i<9; i++){
            if (graph[y][i] == num){
                return true;
            }
        }
        return false;
    }
    public static boolean isContainRow(int x, int y, int num){
        for (int i=0; i<9; i++){
            if (graph[i][x] == num){
                return true;
            }
        }
        return false;
    }
    public static boolean isContainBox(int x, int y, int num){
        int nx = x/3;
        int ny = y/3;
        for (int i=3*ny; i<3*ny+3; i++){
            for (int j=3*nx; j<3*nx+3; j++){
                if (graph[i][j] == num){
                    return true;
                }
            }
        }
        return false;
    }
}