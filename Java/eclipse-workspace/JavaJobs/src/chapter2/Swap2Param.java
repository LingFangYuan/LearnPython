package chapter2;

import java.util.Scanner;

/**
 * 接收两个整数，分别保存到两个变量中，交换两个变量的值。
 * @author lingfangyuan
 * @version 1.0
 * @date 2020-9-9 17:50:47
 * @remarks TODO
 *
 */
public class Swap2Param {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int a;
		int b;
		int t;
		
		System.out.print("请输入第一个整数：");
		a = input.nextInt();
		System.out.print("请输入第二个整数：");
		b = input.nextInt();
		
		System.out.printf("交换前：a：%d，b：%d \n", a, b);
		
		t = a;
		a = b;
		b = t;
		System.out.printf("交换后：a：%d，b：%d \n", a, b);
		
		input.close();

	}

}
