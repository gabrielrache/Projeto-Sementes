public class Main {

    public static void main(String[] args) {

        String[] nomes = {"Dave Mustaine", "Alice Cooper", "Corey Taylor", "Dave Mustaine",
                "Marko Hietala", "Ozzy Osbourne", "Bruce Dickinson", "James Hetfield",
                "Ozzy Osbourne", "James Hetfield", "Corey Taylor", "Tarja Turunen",
                "Amy Lee", "Bruce Dickinson", "Andre Matos","Simone Simons",
                "Serj Tankian", "Chester Bennington", "Bruce Dickinson", "Amy Lee"};


        for (int i = 0; i < nomes.length; i++) {

            for (int j = (i + 1); j < nomes.length; j++){

                if (nomes[i].equalsIgnoreCase(nomes[j])) {
                        nomes[j] = "";
                }
            }
        }

        for (String nome : nomes)
        {
            if (!nome.isEmpty())
                System.out.println(nome);
        }
    }
}