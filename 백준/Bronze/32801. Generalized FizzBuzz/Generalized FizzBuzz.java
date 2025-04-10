import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static long gcd(long x, long y) {
        while (y != 0) {
            long temp = x % y;
            x = y;
            y = temp;
        }
        return x;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] tokens = input.readLine().split(" ");
        long n = Long.parseLong(tokens[0]);
        long a = Long.parseLong(tokens[1]);
        long b = Long.parseLong(tokens[2]);

        long lcm = a / gcd(a, b) * b;

        long countFizzBuzz = n / lcm;
        long countFizz = n / a - countFizzBuzz;
        long countBuzz = n / b - countFizzBuzz;

        System.out.println(countFizz + " " + countBuzz + " " + countFizzBuzz);
    }
}