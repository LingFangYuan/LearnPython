package chapter3;

import java.util.Scanner;

/**
 * 老九商城一周年庆，举行了会员抽奖活动，当会员进入老九商城时， 输入自己的5位数会员编号，只要编号各位数之和小于15，那么就会获得老九t恤衫一件，
 * 比如：输入会员编号13518，那么各位数和为18 >15，并提示“谢谢小伙伴长久以来的支持！”，
 * 如果满足条件，提示“恭喜您，获得了老九一周年纪念t恤衫一件！”。
 * 
 * @author lingfangyuan
 * @version 1.0
 * @date 2020-9-10 11:33:03
 * @remarks TODO
 *
 */

public class Shopping {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		String cardNum;
		int a, b, c, d, e;
		int total = 0;
		int choice = -1;

		System.out.println("Welcom 老九商城！");
		System.out.print("请输入您的5位会员编号：");
		cardNum = input.nextLine();
		if (cardNum.length() == 5) {
			a = Integer.parseInt(String.valueOf(cardNum.charAt(0)));
			b = Integer.parseInt(String.valueOf(cardNum.charAt(1)));
			c = Integer.parseInt(String.valueOf(cardNum.charAt(2)));
			d = Integer.parseInt(String.valueOf(cardNum.charAt(3)));
			e = Integer.parseInt(String.valueOf(cardNum.charAt(4)));
			total = a + b + c + d + e;
		} else {
			System.out.println("输入错误，必须是5位会员编号！");
			System.exit(0);
		}

		if (total > 15) {
			System.out.println("谢谢小伙伴长久以来的支持！");
		} else {
			System.out.println("恭喜您，称为本次幸运用户，将获得下列奖品之一：");
			System.out.println("1：老九定制U盘；2：老九定制笔记本；3：老九纪念勋章");
			System.out.print("请输入选择奖品编号：");
			choice = input.nextInt();

			switch (choice) {
			case 1:
				System.out.println("恭喜您，获得了 老九定制U盘 一件!");
				break;
			case 2:
				System.out.println("恭喜您，获得了 老九定制笔记本 一件!");
				break;
			case 3:
				System.out.println("恭喜您，获得了 老九纪念勋章 一件!");
				break;
			default:
				System.out.println("输入错误！很遗憾，您无法获得本次奖品！谢谢您的大力支持！");
			}
		}

		input.close();

	}

}
