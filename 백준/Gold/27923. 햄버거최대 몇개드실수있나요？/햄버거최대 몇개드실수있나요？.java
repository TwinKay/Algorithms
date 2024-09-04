import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int[] colaTime;
    static List<Integer> hambergers, colaTimeAfter;

    static int N,K,L;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        L = Integer.parseInt(token.nextToken());

        hambergers = new ArrayList<>();
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            hambergers.add(Integer.parseInt(token.nextToken()));
        }
        colaTime = new int[N+1];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i<K; i++) {
            int t = Integer.parseInt(token.nextToken());
            colaTime[t] ++;
            if (t+L<N+1){
                colaTime[t+L] --;
            }
        }
        colaTimeAfter = new ArrayList<>();
        int c = 0;
        for (int i=1; i<N+1; i++) {
            c+=colaTime[i];
            colaTimeAfter.add(c);
        }
        colaTimeAfter.sort((o1, o2) -> {
            return o2 - o1;
        });
        hambergers.sort((o1, o2) -> {
            return o2 - o1;
        });
        long sum = 0;
        for (int i=0; i<N; i++){
            sum += (long)(hambergers.get(i) / Math.pow(2,colaTimeAfter.get(i)));
        }
        System.out.println(sum);
    }
}