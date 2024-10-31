import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N,D,K,C;
    static int[] arr, cntArr;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        D = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        C = Integer.parseInt(token.nextToken());
        arr = new int[N*2];
        for (int i = 0; i < N; i++) {
            int temp = Integer.parseInt(input.readLine());
            arr[i] = temp;
            arr[N+i] = temp;
        }
        cntArr = new int[D+1];
        cntArr[C] ++;

        int res = 1;
        for (int i = 0; i < K; i++) {
            if (cntArr[arr[i]]==0) res++;
            cntArr[arr[i]]++;
        }
        int max = res;
        for (int i=0; i<N; i++){
            int point = i+K;
            cntArr[arr[i]] --;
            if (cntArr[arr[i]]==0) res--;
            if (cntArr[arr[point]]==0) res++;
            cntArr[arr[point]]++;
            max = Math.max(res,max);
            if (max==K+1) break;
        }
        System.out.println(max);
    }
}