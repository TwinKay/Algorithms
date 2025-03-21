import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static boolean[] possibleArr;

    public static void main(String[] args) throws IOException {
        possibleArr = new boolean[20000];

        char[][] board = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '.';
            }
        }
        recu(board, true);

        while (true) {
            String line = input.readLine();
            if (line.equals("end")) break;
            int idx = toIndex(line);
            if (possibleArr[idx]) {
                sb.append("valid\n");
            } else {
                sb.append("invalid\n");
            }
        }
        System.out.println(sb);
    }

    public static void recu(char[][] board, boolean xTurn) {
        if (isWin(board, 'X') || isWin(board, 'O')) {
            possibleArr[toIndex(board)] = true;
            return;
        }

        boolean isFull = true;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == '.') {
                    isFull = false;
                    if (xTurn) {
                        board[i][j] = 'X';
                        if (isWin(board, 'X')) {
                            possibleArr[toIndex(board)] = true;
                        } else {
                            recu(board, false);
                        }
                    }else {
                        board[i][j] = 'O';
                        if (isWin(board, 'O')) {
                            possibleArr[toIndex(board)] = true;
                        } else {
                            recu(board, true);
                        }
                    }
                    board[i][j] = '.';
                }
            }
        }

        if (isFull) {
            possibleArr[toIndex(board)] = true;
        }
    }

    public static boolean isWin(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player) return true;
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player) return true;
        }
        if (board[0][0] == player && board[1][1] == player && board[2][2] == player) return true;
        if (board[0][2] == player && board[1][1] == player && board[2][0] == player) return true;

        return false;
    }

    public static int toIndex(String line) {
        int idx = 0;
        for (int i = 0; i < 9; i++) {
            idx *= 3;
            char c = line.charAt(i);
            if (c == 'X') idx += 1;
            else if (c == 'O') idx += 2;
        }
        return idx;
    }

    public static int toIndex(char[][] board) {
        int idx = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                idx *= 3;
                if (board[i][j] == 'X') idx += 1;
                else if (board[i][j] == 'O') idx += 2;
            }
        }
        return idx;
    }
}
