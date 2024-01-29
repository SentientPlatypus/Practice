import java.util.Scanner;

public class MinMax 

{
	public static void main(String []args)
	{
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int[] arr = new int[n];
	for (int i = 0; i < n; i++)
	{
		arr[i] = sc.nextInt();
	}
	int min = arr[0];
	int max = arr[0];
	for (int j = 0; j < n; j++)
	{
		if (min > arr[j])
		{
			min = arr[j];
		}
		if (max < arr[j])
		{
			max = arr[j];
		}
	}
	System.out.println("Min: " + min);
	System.out.println("Max: " + max);
	sc.close();

	}

}