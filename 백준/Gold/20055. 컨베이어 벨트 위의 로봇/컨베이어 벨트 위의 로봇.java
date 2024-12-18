import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N, K, zeroCnt, stageCnt;
    static int[] belt;
    static boolean[] robots;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        token = new StringTokenizer(input.readLine());
        belt = new int[2*N];
        for (int i = 0; i < 2*N; i++) {
            belt[i] = Integer.parseInt(token.nextToken());
        }

        robots = new boolean[N];
        stageCnt = 0;

        while (zeroCnt < K) {
            stageCnt++;

            rotate();
            move();
            placeRobot();
            countZero();
        }
        System.out.println(stageCnt);
    }

    private static void rotate() {
        int temp = belt[2*N-1];
        for (int i = 2*N-1; i > 0; i--) {
            belt[i] = belt[i-1];
        }
        belt[0] = temp;

        for (int i = N - 1; i > 0; i--) {
            robots[i] = robots[i-1];
        }
        robots[0] = false;
        robots[N-1] = false;
    }

    private static void move() {
        for (int i = N-1; i > 0; i--) {
            if (robots[i-1] && !robots[i] && belt[i] > 0) {
                robots[i] = true;
                robots[i-1] = false;
                belt[i]--;
            }
        }
        robots[N-1] = false;
    }

    private static void placeRobot() {
        if (belt[0] > 0) {
            robots[0] = true;
            belt[0]--;
        }
    }

    private static void countZero() {
        zeroCnt = 0;
        for (int i = 0; i < 2 * N; i++) {
            if (belt[i] == 0) {
                zeroCnt++;
            }
        }
    }
}