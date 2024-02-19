public class Programa1{

    static int count(int arr[], int tam, int num)
    {
        int c = 0;
        for (int i = 1; i < tam; i++)
            if(arr[i] > num)
                c = c+1;
        return c;
    }

  // Compara os números do array a partir do index 1 "tam" vezes
  // com o "num" e soma 1 caso os números do array forem maiores
  // que o "num".
    public static int recurCount(int n)
    {
        if (n == 1)
            return 1;
        return 1 + recurCount(n - 1);
    }

  // Basicamente imprime o número do parâmetro através de uma soma
  // com recursão, fazendo com que retorne um forçadamente até que
  // (n-1) seja 1 e a função pare.

    public static void main(String[] args)
    {
        int arr[] = { 12, 1234, 45, 67, 1 };
        int n = 5;
        int num = 5;
        int num1 = count(arr, n, num);
        int n2 = 5;
        int num2 = recurCount(n2);

        System.out.println(num1);
        System.out.println(num2);
    }
}
