import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        token = new StringTokenizer(input.readLine());
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        int left = 0; int right = N-1;
        int max = Math.min(arr[left], arr[right])*(right - left-1);
        while (left+1 != right) {
            if (arr[left] > arr[right]) {
                max = Math.max(max, arr[right]*(right - left-1));
                right--;
            }else{
                max = Math.max(max, arr[left]*(right - left-1));
                left++;
            }
        }
        System.out.println(max);
        
    }
}