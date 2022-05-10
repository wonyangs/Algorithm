import java.io.*;
import java.util.*;

public class Main{
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer.parseInt(st.nextToken());
        Integer.parseInt(st.nextToken());

        HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> setA = new HashSet<>();
        HashSet<Integer> setB = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            setA.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            setB.add(Integer.parseInt(st.nextToken()));
        }

        set.addAll(setA);
        set.addAll(setB);
        setA.retainAll(setB);

        System.out.println(set.size() - setA.size());

    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}