import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int tmp = b;

        System.out.println(a*(tmp%10));
        tmp = tmp / 10;
        System.out.println(a*(tmp%10));
        tmp = tmp / 10;
        System.out.println(a*(tmp%10));
        System.out.println(a*b);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}