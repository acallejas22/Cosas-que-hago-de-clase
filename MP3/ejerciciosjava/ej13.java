package principal;
import java.util.Scanner;

public class Input {

    static Scanner input = new Scanner (System.in);


  public static void main(String[] args) 
  {

    Scanner input = new Scanner(System.in);
     
    System.out.print  ("ingresa la base del rectantgulo: ");
    float base = input.nextFloat();
    System.out.print  ("ingresa la altura del rectangulo: ");
    float altura = input.nextFloat();
    

   float area = (float)(base*altura);
   float perimetro = (float)(base*2)+(altura*2);

  

    
   
    System.out.println("El preimtro del rectangulo es: " + perimetro); 
    System.out.println("El area del rectangulo es: " + area ); 
  }

}
