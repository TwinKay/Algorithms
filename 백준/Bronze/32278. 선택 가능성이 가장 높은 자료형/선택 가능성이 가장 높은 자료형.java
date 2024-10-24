import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        Long l = Long.parseLong(input.readLine());
        if (l>=-32768 && l<=32767) {
            System.out.println("short");
        }else if (l>=-2147483648 && l<=2147483647) {
            System.out.println("int");
        }else{
            System.out.println("long long");
        }
    }
}