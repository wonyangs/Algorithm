import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
                
        System.out.println(pibo(n));
    }

    public static int pibo(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }

        return pibo(n-1) + pibo(n-2);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}