import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        char[][] graph = new char[n][n];
        List<int[]> arr = new ArrayList<>();
        List<int[]> students = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            tokens = new StringTokenizer(input.readLine());
            for (int j = 0; j < n; j++) {
                char c = tokens.nextToken().charAt(0);
                graph[i][j] = c;
                if (c == 'X') {
                    arr.add(new int[]{j, i});
                } else if (c == 'S') {
                    students.add(new int[]{j, i});
                }
            }
        }

        boolean resFlag = false;

        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.size(); j++) {
                for (int k = 0; k < arr.size(); k++) {
                    if (i < j && j < k) {
                        int[] obj1 = arr.get(i);
                        int[] obj2 = arr.get(j);
                        int[] obj3 = arr.get(k);

                        // 장애물 설치
                        graph[obj1[1]][obj1[0]] = 'O';
                        graph[obj2[1]][obj2[0]] = 'O';
                        graph[obj3[1]][obj3[0]] = 'O';

                        if (isSafe(graph, n, students)) {
                            resFlag = true;
                        }

                        // 장애물 제거
                        graph[obj1[1]][obj1[0]] = 'X';
                        graph[obj2[1]][obj2[0]] = 'X';
                        graph[obj3[1]][obj3[0]] = 'X';

                        if (resFlag){
                            break;
                        }
                    }
                }
                if (resFlag) {
                    break;
                }
            }
            if (resFlag) {
                break;
            }
        }
        if (resFlag) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    private static boolean isSafe(char[][] graph, int n, List<int[]> students) {
        int[] deltaX = {1, -1, 0, 0};
        int[] deltaY = {0, 0, 1, -1};

        for (int[] student : students) {
            int x = student[0];
            int y = student[1];

            for (int d = 0; d < 4; d++) {
                int nx = x;
                int ny = y;
                while (true) {
                    nx += deltaX[d];
                    ny += deltaY[d];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                        break;
                    }
                    if (graph[ny][nx] == 'O') {
                        break;
                    }
                    if (graph[ny][nx] == 'T') {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}