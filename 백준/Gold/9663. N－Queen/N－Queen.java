// 1차원으로 해결할 수 있다니.. 학습 후, 다시 처음부터 구현

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int n, res;
    static int[] board;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());
        res = 0;
        board = new int[n];
        nqueen(0);
        System.out.println(res);
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