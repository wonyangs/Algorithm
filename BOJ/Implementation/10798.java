import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    String[] lines = new String[5];
	    
		for (int i = 0; i < 5; ++i) {
		    lines[i] = sc.nextLine();    
		}
		
		sc.close();
		
		for (int i = 0; i < 15; ++i) {
		    for (String line : lines) {
		        if (line.length() > i) {
		            System.out.print(line.charAt(i));
		        }
		    }    
		}
		System.out.println();
	}
}
