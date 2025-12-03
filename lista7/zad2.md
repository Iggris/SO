Scenariusze użycia odwzorowań:

Prywatne odwzorowanie pliku: głównym zastosowaniem jest zainicjalizowanie obszaru pamięci z zawartości pliku, np. inicjalizacja sekcji text lub data procesu z pliku wykonywalnego lub biblioteki współdzielonej.

Prywatne odwzorowanie anonimowe: alokacja nowej pamięci (pustej, tzn. wypełnionej zerami) dla procesu, np. używając malloc(3), który wykorzystuje mmap(2).

Dzielone odwzorowanie pliku:
przy I/O dla plików dostarczana jest alternatywa dla używania read(2) oraz write(2),
umożliwienie szybkiej komunikacji międzyprocesowej dla procesów niepowiązanych ze sobą

Dzielone odzworowanie anonimowe: umożliwienie szybkiej komunikacji międzyprocesowej dla procesów powiązanych ze sobą

Aby stworzyć odwzorowanie, należy użyć procedury mmap(2). Zleca ona zmapowanie length bajtów przesuniętych o offset bajtów (0 dla pamięci anonimowej) pliku zadanego przez deskryptor fd (-1 dla pamięci anonimowej) do pamięci pod adres addr (jednak ten adres jest tylko propozycją i zwykle jest przekazywany jako 0). Argument prot opisuje oczekiwany sposób ochrony pamięci (nie może być sprzeczny z trybem otwarcia pliku). Może on być równy PROT_NONE lub alternatywą jednego lub więcej znaczników PROT_*: PROT_EXEC, PROT_READ, PROT_WRITE, PROT_NONE. Parametr flags określa rodzaj mapowanego obiektu, opcje mapowania oraz czy modyfikacje powinny być prywatne czy współdzielone. Są to odpowiednio flagi MAP_FIXED, MAP_SHARED, MAP_PRIVATE, jednak sam Linux obsługuje jeszcze znaczniki niestandardowe (których jest znacznie więcej). Poniżej sygnatura funkcji, jak i sposób tworzenia odwzorowań

// sygnatura funkcji
void *mmap(void *addr, size_t length, int prot, int flags,int fd, off_t offset);

// prywatne odwzorowanie pliku
void *private_file = mmap(NULL, [size], [prot], MAP_PRIVATE | MAP_FILE, [fd], [offset]);
// prywatne odwzorowanie anonimowe
void *private_anon = mmap(NULL, [size], [prot], MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
// dzielone odwzorowanie pliku
void *shared_file = mmap(NULL, [size], [prot], MAP_SHARED | MAP_FILE, [fd], [offset]);
// dzielone odwzorowanie anonimowe
void *shared_anon = mmap(NULL, [size], [prot], MAP_SHARED | MAP_ANONYMOUS, -1, 0);

Po wywołaniu fork(2) wszystkie odwzorowania są dziedziczone na zasadzie kopiowania przy zapisie. Z podręcznika execve(2) wiemy, że odzworowania pamięci nie są zachowywane.


Kiedy proces z odwzorowaniem pliku dostanie SIGBUS?: jeśli utworzymy odwzorowanie mmap() pliku większe niż sam plik zaokrąglony w górę do rozmiaru strony (albo później skrócimy plik truncate() tak, że część odwzorowania nie ma już odpowiednika w pliku), i proces spróbuje odczytać lub zapisać bajty w stronach, dla których nie istnieje już odpowiadający fragment pliku (tzn. wewnątrz obszaru odwzorowania, ale logicznie „za końcem pliku”), to jądro generuje dla tego procesu sygnał SIGBUS – informując, że nie ma odpowiedniego fragmentu pliku, którym można by podpiąć daną stronę.

Dla porównania: dostęp poza obszar odwzorowania w ogóle powoduje SIGSEGV, a nie SIGBUS.


Automatyczne zwiększanie stosu
Jądro zakłada od razu maksymalny możliwy obszar stosu (ograniczony m.in. RLIMIT_STACK)
Gdy program zaczyna używać więcej stosu i zapisuje pod adresem tuż poniżej aktualnie zmapowanej strony, powstaje page fault. Obsługa tego błędu w jądrze widzi, że adres leży w dozwolonym zakresie dla stosu, więc:
rozszerza obszar stosu w dół o kolejną stronę,przydziela jej fizyczną pamięć.

Tak powtarza się aż do osiągnięcia limitu (np. RLIMIT_STACK). Gdy adres jest już poza tym limitem, jądro nie rozszerza stosu i kończy proces sygnałem SIGSEGV.

