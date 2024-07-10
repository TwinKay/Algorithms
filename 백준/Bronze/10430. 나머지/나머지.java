import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int a = Integer.valueOf(st.nextToken());
		int b = Integer.valueOf(st.nextToken());
		int c = Integer.valueOf(st.nextToken());
		
		int res1 = (a+b)%c;
		int res2 = ((a%c) + (b%c))%c;
		int res3 = (a*b)%c;
		int res4 = ((a%c) * (b%c))%c;
		
		System.out.println(res1);
		System.out.println(res2);
		System.out.println(res3);
		System.out.println(res4);
	}

}