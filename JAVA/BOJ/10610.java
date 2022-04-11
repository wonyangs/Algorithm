import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] a = br.readLine().toCharArray();
        Arrays.sort(a);
        if (a[0] != '0' || sum(a) % 3 != 0) {
            System.out.println("-1");
            return;
        }
        System.out.println(new StringBuilder(String.valueOf(a)).reverse());
    }

    private static int sum(char[] num) {
        int hap = 0;
        for (char n : num) {
            hap += Character.getNumericValue(n);
        }
        return hap;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}