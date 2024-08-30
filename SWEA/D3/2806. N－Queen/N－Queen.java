import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static int n, res;
    static int[] board;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(input.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(input.readLine());
            res = 0;
            board = new int[n];
            nqueen(0);
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }
    public static void nqueen(int row){
        if(row == n){
            res++;
            return;
        }
        for (int col = 0; col < n; col++) {
            if(isValid(row, col)){
                board[row] = col;
                nqueen(row + 1);
            }
        }
    }
    public static boolean isValid(int row, int col){
        for(int i = 0; i < row; i++){
            if (board[i] == col || Math.abs(board[i]-col)==Math.abs(i-row)){
                return false;
            }
        }
        return true;
    }
}