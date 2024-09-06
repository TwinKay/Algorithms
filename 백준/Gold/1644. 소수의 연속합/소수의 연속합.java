import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int N;
    static boolean[] notPrime;
    static List<Integer> primes = new ArrayList();

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
        for (int i=1; i<N+1; i++){
            if (!notPrime[i]){
                primes.add(i);
            }
        }
        int left = 0;
        int right = 0;
        int sum = 0;
        int cnt = 0;
        while (true){
            if (sum>N){
                sum -= primes.get(left++);
            } else if (sum==N){
                cnt++;
                sum -= primes.get(left++);
            } else if (right==primes.size()){
                break;
            } else{
                sum += primes.get(right++);
            }
        }
        System.out.println(cnt);
    }
}