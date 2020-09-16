package chapter3;

import java.util.Scanner;

/**
 * 老九商城1周年福利继续放送，凡是在老九商城购物的会员和非会员，均享受不同程度的折扣优惠，
 * 编写一个程序，完成会员购物后根据优惠政策计算付款的功能：
 * a)所有商城会员购物均享受9折优惠。
 * b)对于非会员的购物满200元，也可以享受9折优惠。
 * c)如果是会员，而且购物满200元，可以享受8折优惠。
 * 假如有一个用户购买了2件商品：”老九大礼包“、”老九答疑会员“，
 * 请计算该用户可得到的折扣额以及应该支付多少钱？
 * TODO
 * @author lingfangyuan
 * @version 1.0
 * @date 2020-9-10 13:48:02
 * @remarks TODO
 *
 */

public class LJMall {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String id_status;           //判断是否是会员，会员为'y'，非会员为'n'
		double goods_package;        //购买老九大礼包的金额
		double goods_answer;         //购买老九答疑会员的金额
		double total_cost;           //购买两个商品的总金额
		double discount;            //折扣
		double discount_amount;      //折扣金额
		double pay;                 //最终支付金额
		Scanner input = new Scanner(System.in);
		
		System.out.print("是否是会员？(y/n)：");
		id_status = input.next();
		System.out.print("请输入老九大礼包的价格：");
		goods_package = input.nextFloat();
		System.out.print("请输入老九答疑会员的价格：");
		goods_answer = input.nextFloat();
		
		total_cost = goods_package + goods_answer;
		discount = 1;
		discount_amount = 0;
		
		//判断是否为会员
		if (id_status.equals("y")) {
			//判断是否购物满200元
			if (total_cost >= 200) {
				discount = 0.8;
			} else {
				discount = 0.9;
			}
			
		} else if (id_status.equals("n")) {
			//判断是否购物满200元
			if (total_cost >= 200) {
				discount = 0.9;
			}
		} else {
			System.out.println("输入错误！");
			System.exit(0);
		}
		
		pay = total_cost * discount;
		discount_amount = total_cost - pay;
		
		System.out.printf("本次购物商品总金额为：%.2f，折扣金额为：%.2f，应付金额为：%.2f。",
				total_cost, discount_amount, pay);
		
		input.close();

	}

}
