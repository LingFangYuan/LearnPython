package chapter3;
/**
 * 在任意一个四位整数中，如果该数的个位数和百位数之和大于16，
 * 并且十位数和千位数之和小于3，就称这种数为“老九幸运数“，
 * 请小伙伴编程计算出在1000~9999中，一共有多少个满足老九幸运数的四位整数呢，
 * 打印出最终的个数！
 * TODO
 * @author lingfangyuan
 * @version 1.0
 * @date 2020-9-10 14:40:39
 * @remarks TODO
 *
 */

public class LuckyNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int ge, shi, bai, qian;
		int count = 0;
		
		for (int i = 1000; i <= 9999; i++) {
			qian = i / 1000;
			bai = i % 1000 / 100;
			shi = i % 1000 % 100 /10;
			ge = i % 10;
			//System.out.printf("千：%d，百：%d，十：%d，个：%d。\n", qian, bai, shi, ge);
			
			if (ge + bai > 16 && shi + qian < 3) {
				count += 1;
			}
			
		}
		System.out.printf("1000~9999中，一共有 %d 个满足老九幸运数的四位整数!", count);

	}

}
