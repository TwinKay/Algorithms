import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;

    static int N;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        Arrays.sort(arr);
        int res = Integer.MAX_VALUE;

        for (int i=0; i<N-3; i++){
            for (int j=i+3; j<N; j++){
                res = Math.min(res, findMinDiff(i,j));
            }
        }

        System.out.println(res);

    }
    public static int findMinDiff(int leftLimit, int rightLimit){
        int left = leftLimit+1;
        int right = rightLimit-1;
        int len1 = arr[leftLimit]+arr[rightLimit];
        int minDiff = Integer.MAX_VALUE;
        while(left < right){
            int len2 = arr[left]+arr[right];
            int diff = Math.abs(len2-len1);
            minDiff = Math.min(minDiff, diff);
            if(len2 < len1){
                left ++;
            }else{
                right --;
            }
        }
        return minDiff;
    }
}