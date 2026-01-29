import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {


        System.out.print("What's the operation? (+, -, *, /): ");
        Scanner scanner = new Scanner(System.in);
        String operation = scanner.nextLine();

        System.out.print("First number: ");
        int x = scanner.nextInt();

        System.out.print("Second number: ");
        int y = scanner.nextInt();

        if (operation.equals("+")) {
            int sum = x + y;
            System.out.println("The result is: " + sum);
            System.exit(0);

        }
        if (operation.equals("-")) {
            int minus = x - y;
            System.out.println("The result is: " + minus);
            System.exit(0);

        }
        if (operation.equals("*")) {
            int multiply = x * y;
            System.out.println("The result is: " + multiply);
            System.exit(0);


        }
        if (operation.equals("/")) {
            int divide = x / y;
            System.out.println("The result is: " + divide);
            System.exit(0);

        }
            System.out.println("Please, insert a valid operation-sign.");


    }
}
