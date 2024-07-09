//아직 array를 배우지 않아서..

import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line1 = br.readLine();
		String line2 = br.readLine();
		String line3 = br.readLine();
		
		int temp;
		if (line1.charAt(0) != 'F' && line1.charAt(0) != 'i' && line1.charAt(0) != 'z' && line1.charAt(0) != 'B' && line1.charAt(0) != 'u') {
			temp = Integer.valueOf(line1)+3;
			} else if (line2.charAt(0) != 'F' && line2.charAt(0) != 'i' && line2.charAt(0) != 'z' && line2.charAt(0) != 'B' && line2.charAt(0) != 'u') {
				temp = Integer.valueOf(line2)+2;
			} else {
				temp = Integer.valueOf(line3)+1;
			}
		
		if (temp%3 == 0 && temp%5 == 0) {
			System.out.println("FizzBuzz");
		} else if (temp%3 == 0) {
			System.out.println("Fizz");
		} else if (temp%5 == 0) {
			System.out.println("Buzz");
		} else {
			System.out.println(temp);
		}
		
		
		}

	}