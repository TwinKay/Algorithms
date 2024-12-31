import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,M,L;
    static int[] points, querys;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        L = Integer.parseInt(token.nextToken());
        points = new int[M+1];
        for (int i = 0; i < M; i++) {
            points[i] = Integer.parseInt(input.readLine());
        }
        points[M] = L;

        int maxQuery = 0;
        querys = new int[N];
        for (int i = 0; i < N; i++) {
            querys[i] = Integer.parseInt(input.readLine());
            maxQuery = Math.max(maxQuery, querys[i]);
        }

        int[] resArr = new int[maxQuery+1];
        for (int q = 1; q <= maxQuery; q++) {
            int start = 0; int end = L;
            int res = 0;

            while (start <= end) {
                int mid = (start + end) / 2;
                int cnt = find(mid);

                if (cnt > q) {
                    start = mid + 1;
                    res = Math.max(res,mid);
                }else{
                    end = mid - 1;
                }
            }
            resArr[q] = res;
        }

        for (int query : querys) {
            sb.append(resArr[query]).append("\n");
        }
        System.out.println(sb);

    }
    static int find(int mid) {
        int cnt = 0;
        int temp = 0;
        for (int point : points) {
            if (point-temp >= mid){
                cnt ++;
                temp = point;
            }
        }
        return cnt;
    }
}