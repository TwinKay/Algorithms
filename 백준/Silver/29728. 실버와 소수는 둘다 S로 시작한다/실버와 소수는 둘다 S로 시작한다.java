import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static boolean[] notPrime;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        notPrime = new boolean[N+1];
        notPrime[0] = true;
        notPrime[1] = true;

        for (int i=2; i<=Math.sqrt(N); i++){
            if (!notPrime[i]){
                for (int j=i*i; j<N+1; j+=i){
                    notPrime[j] = true;
                }
            }
        }
        Deque<Character> deq = new ArrayDeque<>();
        boolean pointer = true;
        for (int i=1; i<=N; i++){
            if (notPrime[i]){
                if (pointer){
                    deq.addLast('B');
                }else{
                    deq.addFirst('B');
                }
            }else{
                if (pointer){
                    if (deq.peekLast() =='B'){
                        deq.pollLast();
                        deq.addLast('S');
                        deq.addLast('S');
                    }else{
                        deq.addLast('S');
                    }
                    pointer = false;
                }else{
                    if (deq.peekFirst() =='B'){
                        deq.pollFirst();
                        deq.addFirst('S');
                        deq.addFirst('S');
                    }else{
                        deq.addFirst('S');
                    }
                    pointer = true;
                }
            }
        }
        int cntB = 0;
        for (char c : deq){
            if (c == 'B') cntB++;
        }
        sb.append(cntB).append(" ").append(deq.size()-cntB);
        System.out.println(sb);
    }
}