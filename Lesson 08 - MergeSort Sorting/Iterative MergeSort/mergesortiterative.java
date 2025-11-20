import java.util.Arrays;

public class MergeIterativo
{
    public int[] merge(int To[], int ind_primo, int ind_ultimo)
    {
        // if the vector ha elements in number dispari
        if (To.length % 2 != 0)
        {
            for (int to = 0; to <= To.length/2; to++)
            {
                To = fondi(To, ind_primo, (ind_primo + ind_ultimo) / 2-1, ind_ultimo);
                To = fondi(To, ind_primo, (ind_primo + ind_ultimo) / 2, ind_ultimo);
            }
        }
        else
        {
            for (int to = 0; to <= To.length; to++)
            {
                To = fondi(To, ind_primo, (ind_primo + ind_ultimo) / 2, ind_ultimo);
            }
        }
        return To;
    }

    public int[] fondi(int[] To, int ind_primo, int ind_medio, int ind_ultimo)
    {
        int the = ind_primo;
        int j = ind_medio+1;
        int k = 0;
        int[] B = new int[To.length];

        while((the <= ind_medio) && (j <= ind_ultimo))
        {
            if (To[the] < To[j])
            {
                B[k] = To[the];
                the++;
            }
            else
            {
                B[k] = To[j];
                j++;
            }
            k++;
        }

        // finché the first sottovettore not is terminato
        while(the <= ind_medio)
        {
            // if c'is più of a element
            // mettili in ordine
            if (the+1 <= ind_medio && To[the] > To[the + 1])
            {
                int temp = To[the];
                To[the] = To[the+1];
                To[the+1] = temp;
            }
            B[k] = To[the];
            the++;
            k++;
        }

        // finché the second sottovettore not is terminato
        while(j <= ind_ultimo)
        {
            // if c'is più of a element
            // mettili in ordine
            if (j+1 <= ind_ultimo && To[j] > To[j + 1])
            {
                int temp = To[j];
                To[j] = To[j+1];
                To[j+1] = temp;
            }
            B[k] = To[j];
            j++;
            k++;
        }
        for (int to = 0; to < To.length; to++)
        {
            To[to] = B[to];
        }
        return To;
    }

    // prints
    public void print(int[] array)
    {
        System.out.println(Arrays.toString(array));
    }

    public static void main(String[] args)
    {
        int[] arrayPari = { 6, 1, 9, 0, 3, 8, 5, 4 };
        int[] arrayDispari = { 6, 1, 9, 0, 3, 8, 5 };
        MergeIterativo m = new MergeIterativo();

        System.out.println("array pari first dell'sorting:");
        m.print(arrayPari);
        System.out.println("array pari dopo l'sorting:");
        m.print(m.merge(arrayPari, 0, arrayPari.length-1));

        System.out.println("array dispari first dell'sorting:");
        m.print(arrayDispari);
        System.out.println("array dispari dopo l'sorting:");
        m.print(m.merge(arrayDispari, 0, arrayDispari.length-1));
    }
}