import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        boolean[] arr = new boolean[31];
        for (int i = 0; i < 28; i++) {
            int n = Integer.parseInt(input.readLine());
            arr[n] = true;
        }
        for (int i = 1; i < 31; i++) {
            if (!arr[i]) sb.append(i).append("\n");
        }
        System.out.println(sb);


    }
}