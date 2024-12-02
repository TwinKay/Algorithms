import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int a = Integer.parseInt(input.readLine());
        int b = Integer.parseInt(input.readLine());

        if (a<=b) {
            System.out.println("high speed rail");
        }else{
            System.out.println("flight");
        }
    }
}