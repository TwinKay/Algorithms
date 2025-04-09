import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException {
        int total = Integer.parseInt(input.readLine());
        for (int i = 0; i < 9; i++) {
            total -= Integer.parseInt(input.readLine());
        }
        System.out.println(total);

    }
}