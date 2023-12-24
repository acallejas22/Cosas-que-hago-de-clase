public class Main {
    public static void main(String[] args) {
        int rand, color = 0, n = 10;
        while (true) {
            for (int i = 0; i < n + n / 2; i++) {
                for (int j = n + (n / 2); j > i; j--) {
                    System.out.print(" ");
                }

                for (int k = 1; k <= 2 * i - 1; k++) {
                    rand = (int) (Math.random() * 101) + 1;
                    if (rand % 7 == 0) {
                        System.out.print("\u001B[34mº");
                    } else {
                        System.out.print("\u001B[32mº");
                    }
                }
                System.out.println("");
            }

            for (int i = 1; i < n - (n / 2); i++) {
                for (int j = n - 1 + (n / 2); j > 1; j--) {
                    System.out.print(" ");
                }
                System.out.println("\u001B[31m***");
            }

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace(); // Manejo básico de la excepción, puedes personalizarlo según tus necesidades.
            }

            System.out.println("\033[H\033[2J");
            System.out.flush();
        }
    }
}
