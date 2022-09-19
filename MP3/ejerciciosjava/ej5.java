package principal;
import java.util.Scanner;

public class Input {
    static Scanner input = new Scanner (System.in);


  public static void main(String[] args) 
  {


    System.out.print("ingresa un numero1: ");

    int numeroingresado1 = Integer.parseInt(input.nextLine());

    System.out.print("ingresa un numero2: ");

    int numeroingresado2 = Integer.parseInt(input.nextLine());

    int mult = numeroingresado1 * numeroingresado2;

    System.out.println(mult);
   
  }

}
