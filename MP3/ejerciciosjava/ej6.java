package principal;
import java.util.Scanner;

public class Input {

    static Scanner input = new Scanner (System.in);


  public static void main(String[] args) 
  {


    System.out.print  ("ingresa un numero1: ");

    int numeroingresado1 = Integer.parseInt(input.nextLine());

    System.out.print("ingresa un numero2: ");

    int numeroingresado2 = Integer.parseInt(input.nextLine());

    int suma = numeroingresado1 + numeroingresado2;

    int resta = numeroingresado1 - numeroingresado2;

    int mult = numeroingresado1 * numeroingresado2;

    int div = numeroingresado1 / numeroingresado2;

    int mod = numeroingresado1 % numeroingresado2;

    
   
    System.out.println(numeroingresado1 + "+" + numeroingresado2 + "=" + suma); 
    System.out.println(numeroingresado1 + "-" + numeroingresado2 + "=" + resta);
    System.out.println(numeroingresado1 + "*" + numeroingresado2 + "=" + mult);
    System.out.println(numeroingresado1 + "/" + numeroingresado2 + "=" + div);
    System.out.println(numeroingresado1 + "%" + numeroingresado2 + "=" + mod);
   
  }

}
