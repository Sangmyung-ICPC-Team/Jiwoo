import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeSet;

// 차집합
// https://www.acmicpc.net/problem/1822

public class Boj1822 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int an = scanner.nextInt();
        int bn = scanner.nextInt();

        // TreeSet 또는 HashSet은 집합을 표현하며 자동으로 요소들을 정렬해준다
        TreeSet<Integer> aList = new TreeSet<Integer>();

        for(int i=0; i<an; i++) {
            aList.add(scanner.nextInt());
        }

        for(int i=0; i<bn; i++) {
            int n = scanner.nextInt();
            
            if(aList.contains(n)) {
                aList.remove(n);
            }
        }

    
        System.out.println(aList.size());
        for(Integer n : aList) {
            System.out.print(n + " ");
        }
        System.out.println();

        scanner.close();
    }
}