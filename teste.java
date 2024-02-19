public class teste{
    public static int recurCount(int n)
        {
            if (n == 1)
                return 1;
            return 1 + recurCount(n - 1);
        }

    public static void main (String[] args){
        int n2 = 5;
        int num2 = recurCount(n2);
    }
}