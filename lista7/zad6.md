Nie, nie mamy gwarancji, że program nie zobaczy późniejszych modyfikacji pliku. Przy stronicowaniu na żądanie prywatne odwzorowanie może użyć aktualnej zawartości pliku w momencie pierwszego zaczytania danej strony jeśli plik zmieniono po mmap, ale przed pierwszym dostępem do tej strony, proces może zobaczyć już zmienione dane



W Linuxie pliki wykonywalne są stronicowane na żądanie w razie potrzeby. Plik wykonywalny na dysku staje się wtedy "pamięcią zapasową" dla procesu. Oznacza to, że nie można modyfikować pliku wykonywalnego na dysku, gdyż wpłynęłoby to na działanie uruchomionej aplikacji. Jeśli spróbowalibyśmy użyć open(2) na pliku wykonywalnym, który jest aktualnie uruchomiony, to zwrócony zostałby błąd ETXTBSY (text file busy). Podobnie w przypadku próby uruchomienia exec(2), ten sam błąd może zostać zwrócony.

Gdyby system operacyjny stosujący stronicowanie na żądanie pozwolił na modyfikację uruchomionego pliku wykonywalnego, to niepotrzebne na początku strony nie byłyby ładowane do pamięci. Później, po wykonaniu zmian na uruchomionym programie, zostałyby wczytywane strony po modyfikacji, które prawdopodobnie kolidowałyby ze sobą, przez co program stałby się niezdatny do użytku, gdyż w każdym momencie mógłby się wywalić.



Stronicowanie na żądanie (ang. demand paging) to sposób implementacji pamięci wirtualnej. Polega ono na sprowadzaniu stron do pamięci operacyjnej tylko wtedy, gdy jest ona potrzebna, dzięki czemu zmniejszana jest liczba operacji I/O oraz zapotrzebowanie na pamięć operacyjną, ponieważ nie są sporwadzane niepotrzebne strony.
