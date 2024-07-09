import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String A = br.readLine();
		String B = br.readLine();
		String C = br.readLine();
		br.close();
		
		int intA = Integer.valueOf(A);
		int intB = Integer.valueOf(B);
		int intC = Integer.valueOf(C);
		
		int AB = Integer.valueOf(A+B);

		System.out.println(intA+intB-intC);
		System.out.println(AB-intC);
	}

}