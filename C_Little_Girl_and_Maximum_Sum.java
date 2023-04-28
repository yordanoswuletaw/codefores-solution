import java.util.*;

public class Main {
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
int n = scanner.nextInt();
int q = scanner.nextInt();
int[] nums = new int[n];
for (int i = 0; i < n; i++) {
nums[i] = scanner.nextInt();
}
Arrays.sort(nums);
reverse(nums);
int[] prfxSum = new int[n + 1];
for (int i = 0; i < q; i++) {
int start = scanner.nextInt();
int end = scanner.nextInt();
prfxSum[start - 1] += 1;
prfxSum[end] -= 1;
}
for (int i = 1; i < prfxSum.length; i++) {
prfxSum[i] += prfxSum[i - 1];
}
reverse(prfxSum);
long maxSum = 0;
for (int i = 0; i < n; i++) {
if (prfxSum[i] == 0) {
break;
}
maxSum += (long) prfxSum[i] * nums[i];
}
System.out.println(maxSum);
}