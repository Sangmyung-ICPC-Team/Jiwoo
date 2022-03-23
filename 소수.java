import java.util.Scanner;

public class 소수 {

    public static boolean isNotPrime[];

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();

        int totalSum = 0;
        int minPrime = -1;

        isNotPrime = new boolean[n+1];

        eratosthenesSieve();

        for(int i = m; i <= n; i++){
            if(!isNotPrime[i]) {
                totalSum += i;

                if(minPrime == -1)
                    minPrime = i;
            }
        }

        if(minPrime != -1) {
            System.out.println(totalSum);
        }
        System.out.println(minPrime);

        sc.close();
    }

    private static void eratosthenesSieve() {
        isNotPrime[0] = true;
        isNotPrime[1] = true;

        for(int i = 2; i <= Math.sqrt(isNotPrime.length); i++) {
            for(int j = i*i; j < isNotPrime.length; j += i){
                isNotPrime[j] = true;
            }
        }
    }
}
