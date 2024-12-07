import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        boolean[] arr = new boolean[101];
        for (int i=2; i<=9; i++) {
            for (int j=1; j<=9; j++){
                arr[i] = true;
                arr[j] = true;
                arr[i*j] = true;
            }
        }
        int N = Integer.parseInt(input.readLine());

        if(arr[N]) System.out.println(1);
        else System.out.println(0);

    }
}