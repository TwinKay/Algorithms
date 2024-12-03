import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N;
    static int[] finalArr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        finalArr = new int[N];
        token = new StringTokenizer(input.readLine());
        for(int i=0; i<N; i++){
            finalArr[i] = Integer.parseInt(token.nextToken());
        }

        for(int t2=1; t2<N; t2++){
            for(int t1=1; t1<N; t1++){
                int left = 0;
                while(left < N) {
                    int sVal = ((left+t1) % N) + 1;
                    int mVal = finalArr[( (left-t2) % N + N ) % N];
                    if(sVal == mVal) left++;
                    else break;
                }
                if(left >= N-1) {
                    continue;
                }

                int right = N-1;
                while(right >= 0) {
                    int sVal = ((right+t1) % N) + 1;
                    int mVal = finalArr[( (right-t2) % N + N ) % N];
                    if(sVal == mVal) right--;
                    else break;
                }

                if(left >= right) continue;

                boolean find = true;
                for(int k=0; k <= (right-left); k++){
                    int sVal = ((left+k+t1) % N) + 1;
                    int mVal = finalArr[( (right-k-t2) % N + N ) % N];
                    if(sVal != mVal){
                        find = false;
                        break;
                    }
                }

                if(find) {
                    sb.append(t1).append("\n");
                    sb.append(left+1).append(" ").append(right+1).append("\n");
                    sb.append(t2).append("\n");
                    System.out.println(sb);
                    return;
                }
            }
        }
    }
}