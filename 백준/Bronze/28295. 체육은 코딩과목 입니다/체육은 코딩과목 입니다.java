import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int cnt;

    public static void main(String[] args) throws IOException {
        cnt = 1080;
        for (int i = 0; i < 10; i++) {
            int q = Integer.parseInt(br.readLine());
            if (q==1){
                cnt += 90;
            }else if (q==2){
                cnt += 180;
            }else{
                cnt -= 90;
            }
        }
        cnt %= 360;
        if (cnt==0){
            System.out.println("N");
        }else if (cnt==90){
            System.out.println("E");
        }else if (cnt==180){
            System.out.println("S");
        }else{
            System.out.println("W");
        }
    }
}