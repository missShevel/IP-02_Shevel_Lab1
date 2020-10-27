import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    System.out.print("Будь ласка, введіть число: ");
    int number = in.nextInt();

    double a = number / 100d; // перша цифра
    double b = (number / 10d) % 10; // друга цифра
    double c = number % 10; // третя цифра

    int d = number / 10; // число десятків

    double ave = (a + b + c) / 3; // середнє арифметичне

    System.out.printf("Число одиниць: %1.0f%n", c);
    System.out.printf("Число десятків: %d%n", d);
    System.out.printf("Середнє арифметичне: %1.2f", ave);
  }

}