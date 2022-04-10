import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main{

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BigInteger n = new BigInteger(br.readLine());
        BigInteger m = new BigInteger(br.readLine());

        br.close();

        System.out.println(n.add(m));
        System.out.println(n.subtract(m));
        System.out.println(n.multiply(m));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}