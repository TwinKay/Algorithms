import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static int N;
    static int[] arr;
    static List<Integer> lst = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(input.readLine());
        arr = new int[N];
        token = new StringTokenizer(input.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(token.nextToken());
        }
        lst.add(arr[0]);
        for (int i = 1; i < N; i++) {
            if (lst.get(lst.size() - 1) < arr[i]) {
                lst.add(arr[i]);
            }else{
                int idx = Collections.binarySearch(lst, arr[i]);
                if (idx < 0) {
                    idx = -idx - 1;
                    lst.set(idx, arr[i]);
                }
            }
        }
        System.out.println(lst.size());
    }
}