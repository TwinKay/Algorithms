import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int cnt = 0;
        for (int i=0; i<6; i++){
            String s = input.readLine();
            char c = s.charAt(0);
            if (c=='W'){
                cnt++;
            }
        }
        if (cnt>=5){
            System.out.println(1);
        }else if (cnt>=3){
            System.out.println(2);
        }else if (cnt>=1){
            System.out.println(3);
        }else{
            System.out.println(-1);
        }
    }
}