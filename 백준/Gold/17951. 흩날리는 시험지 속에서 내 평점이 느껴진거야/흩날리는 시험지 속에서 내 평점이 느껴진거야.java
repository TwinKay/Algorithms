// 이분 탐색이라는 걸 몰랐다면 접근할 수 있었을까..?

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    static int N,K,totalSum;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        token = new StringTokenizer(input.readLine());
        N = Integer.parseInt(token.nextToken());
        K = Integer.parseInt(token.nextToken());
        arr = new int[N];
        token = new StringTokenizer(input.readLine());
        totalSum = 0;
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
            totalSum += arr[i];
        }
        
        int left = 0;
        int right = totalSum;
        while (left <= right) {
            int mid = (left + right) / 2;
            int sum = 0;
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                sum += arr[i];
                if (sum >= mid) {
                    cnt++;
                    sum = 0;
                }
            }
            if (cnt >= K){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        System.out.println(right);
    }
}