import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String s = input.readLine();
        if (s.equals("fdsajkl;") || s.equals("jkl;fdsa")){
            System.out.println("in-out");
        } else if (s.equals("asdf;lkj") || s.equals(";lkjasdf")) {
            System.out.println("out-in");
        } else if (s.equals("asdfjkl;")) {
            System.out.println("stairs");
        } else if (s.equals(";lkjfdsa")) {
            System.out.println("reverse");
        } else {
            System.out.println("molu");
        }
    }
}