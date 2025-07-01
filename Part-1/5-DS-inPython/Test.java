import java.util.Scanner;

class Test{
    public static void main(String[] args) {
    // Input validation
    int number;
    do {
        System.out.print("Enter a positive number: ");
        number = scanner.nextInt();
        if (number <= 0) {
            System.out.println("Please enter a positive number!");
        }
    } while (number <= 0);
    }
}