import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < 10; ++i) {
            set.add(Integer.parseInt(br.readLine()) % 42);
        }
        System.out.println(set.size());
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}