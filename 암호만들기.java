// 암호만들기
// https://www.acmicpc.net/problem/1759
import java.util.Arrays;
import java.util.Scanner;

public class 암호만들기 {

    private static int l = 0;
    private static int c = 0;
    private static char chs[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        l = sc.nextInt();
        c = sc.nextInt();

        chs = new char[c];
        for(int i=0;i<c;i++){
            chs[i] = sc.next().charAt(0);
        }

        Arrays.sort(chs);

        solve("", -1, 0);
    }

    private static void solve(String pwd, int currPos, int currLen){
        if(currLen == l) {
            int vowel_nums = 0;
            int consonant_nums = 0;
            for (int i=0; i<l;i++) {
                if (pwd.charAt(i) == 'a' || pwd.charAt(i) == 'e' || pwd.charAt(i) == 'i' || pwd.charAt(i) == 'o' || pwd.charAt(i) == 'u')
                    vowel_nums++;
                else
                    consonant_nums++;

                if (vowel_nums >= 1 && consonant_nums >= 2) {
                    System.out.println(pwd);
                    break;
                }
            }
        } else if(currLen > l)
            return;
        else{
            for(int i=currPos+1; i<c;i++)
                solve(pwd+chs[i], i, currLen+1);
        }
    }
}
