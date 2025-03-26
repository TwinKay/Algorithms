import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        double n = Double.parseDouble(input.readLine());
        double d = n/100 + 25;
        if (d<=100){
            System.out.println("100.00");
        }else if (d>2000){
            System.out.println("2000.00");
        }else {
            System.out.println(String.format("%.2f", d));
        }
    }
}

