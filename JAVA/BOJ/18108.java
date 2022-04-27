import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        System.out.println(m-543);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}