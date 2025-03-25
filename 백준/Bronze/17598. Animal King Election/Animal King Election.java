import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int cntLions = 0;
        int cntTigers = 0;
        for (int i=0; i<9; i++) {
            String s = input.readLine();
            if (s.length()==4) cntLions++;
            else cntTigers++;
        }
        if (cntLions>cntTigers) System.out.println("Lion");
        else System.out.println("Tiger");
    }
}

