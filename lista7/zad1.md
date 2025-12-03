Odwzorowanie plików w pamięć (ang. memory-mapped files) to zmapowanie obszaru pliku lub zasobu plikopodobnego do pamięci wirtualnej procesu. Po zmapowaniu można bezpośrednio się dostać do zawartości poprzez operowanie na jego bajtach w odpowiadającym obszarze pamięci. Strony są automatycznie ładowane z pliku, gdy zajdzie taka potrzeba.

Odwzorowanie pamięci anonimowej (ang. anonymous mappings) to mapowanie, które nie ma odpowiadającego pliku, a strony mapowania są zainicjalizowane zerami.

Odwzorowanie prywatne (MAP_PRIVATE) działa tak, że modyfikacje zawartości odwzorowania nie są widoczne dla innych procesów, a dla odwzorowań plików w pamięć - nie są zapisywane do pliku. Jądro dokonuje tego poprzez kopiowanie przy zapisie, a więc przy próbie modyfikacji zawartości strony przez proces, jądro tworzy nową, oddzielną kopię tej strony dla procesu. Ta technika wykorzystywana jest w bardzo prostym celu - zmiany nie mogą być widoczne dla innych procesów, a więc dopóki nie są wykonywane żadne zapisy, nie ma potrzeby kopiowania pamięci, a gdy jakiś proces spróbuje coś zapisać, zmiany będą widoczne tylko dla niego (na własnej kopii).

Odwzorowanie dzielone (MAP_SHARED) sprawia, że modyfikacje zawartości odwzorowania są widoczne dla innych procesów dzielących to odwzorowanie oraz w przypadku odwzorowań plików w pamięć, są zapisywane do plików. Pamięć odzworowana może być dzielona z odwzorowaniami w innych procesach (wpisy tabeli stron każdego procesu wskazują na to samo miejsce w pamięci RAM) na dwa sposoby: dwa procesy odwzorowują ten sam obszar pliku lub poprzez fork(2) (dziecko dziedziczy wszystkie odwzorowania rodzica).



Czy pamięć obiektów odwzorowanych prywatnie może być współdzielona?: Pamięć odwzorowana prywatnie może być współdzielona tylko do odczytu (np. po fork()), ale modyfikacje nie są współdzielone, w chwili zapisu kernel tworzy prywatną kopię strony (Copy-on-Write).
 
Czemu można tworzyć odwzorowania plików urządzeń blokowych w pamięć, a znakowych nie?: Urządzenia blokowe da się sensownie odwzorować w pamięć (partycja dysku, VRAM). Urządzenia znakowe z natury są strumieniowe i zwykle nie implementują operacji mmap, dlatego zazwyczaj nie można ich odwzorować (albo byłoby to pozbawione sensu).