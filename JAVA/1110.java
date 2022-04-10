import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
        int res = a%10*10 + sum(a)%10;
        int count = 1;

        while(a != res) {
            res = res%10*10 + sum(res)%10;
            count++;
        }
        System.out.println(count);
    }

    private int sum(int num) {
        return num%10 + num/10;
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();        
    }
}