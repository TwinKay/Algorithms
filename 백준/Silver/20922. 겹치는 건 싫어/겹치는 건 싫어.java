import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,M;
    static int[] arr, cntArr;
    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        M = Integer.parseInt(token.nextToken());
        arr = new int[N];
        cntArr = new int[100001];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        int point = 0;
        int curLen = 0;
        int maxLen = 0;
        for (int i = 0; i < N; i++) {
            cntArr[arr[i]] ++;
            curLen ++;
            while(cntArr[arr[i]] > M){
                cntArr[arr[point]] --;
                curLen --;
                point++;
            }
            maxLen = Math.max(maxLen, curLen);
        }
        System.out.println(maxLen);
    }
}