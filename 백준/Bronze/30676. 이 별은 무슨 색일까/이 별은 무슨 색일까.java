import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer token;
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(input.readLine());
        if (n>=620 && n<=780)System.out.println("Red");
        else if (n>=590) System.out.println("Orange");
        else if (n>=570) System.out.println("Yellow");
        else if (n>=495) System.out.println("Green");
        else if (n>=450) System.out.println("Blue");
        else if (n>=425) System.out.println("Indigo");
        else System.out.println("Violet");
    }
}