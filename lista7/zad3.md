cat /proc/$(pgrep Xorg)/status | egrep 'Vm|Rss'
VmPeak:   579028 kB maksymalny (historyczny) rozmiar przestrzeni wirtualnej procesu (kB).
VmSize:   579028 kB aktualny rozmiar przestrzeni wirtualnej (kod, dane, stos, mapowania plików, itp.).
VmLck:         0 kB pamięć zablokowana w RAM (mlock), której nie wolno wymieść na dysk
VmPin:         0 kB pamięć „przypięta”, której jądro nie może przenieść czy zwolnić.
VmHWM:    236124 kB „high water mark” RSS, czyli największy kiedykolwiek rozmiar zbioru rezydentnego.
VmRSS:    236124 kB aktualny zbiór rezydentny: ile pamięci tego procesu faktycznie jest w RAM (bez części wy-swappowanej).
RssAnon:          131884 kB część RSS, która jest anonimowa (heap, stos, malloc, brk, mmap(MAP_ANONYMOUS) itp.).
RssFile:           51200 kB część RSS pochodząca z mapowanych plików (kod programu, biblioteki, zwykłe mmap plików).
RssShmem:          53040 kB część RSS pochodząca ze współdzielonej pamięci (SysV SHM, tmpfs, itp.).
VmData:   139208 kB segment danych + sterta (heap).
VmStk:       132 kB stos
VmExe:      1688 kB kod wykonywalny programu
VmLib:    175928 kB kod bibliotek współdzielonych
VmPTE:       764 kB pamięć zajęta przez tablice stron tego procesu.
VmSwap:        0 kB ilość pamięci tego procesu, która aktualnie leży w swapie.


2. Zbiór roboczy vs zbiór rezydentny

Zbiór rezydentny (resident set, RSS) – wszystkie strony tego procesu, które aktualnie są w RAM.

Zbiór roboczy (working set) – strony, które były używane w ostatnim przedziale czasu (np. w ostatnich kilkuset milisekundach / sekundach).

Czyli:
working set ⊆ resident set, w zbiorze rezydentnym mogą być strony dawno nieużywane, które jeszcze nie zostały wyparte.

Czemu suma VmRSS ≠ używana pamięć z vmstat -s?:
Strony współdzielone są liczone wiele razy