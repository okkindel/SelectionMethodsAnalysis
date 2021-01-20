---
title: "Wydział Elektroniki"
author: [Maciej Hajduk, Politechnika Wrocławska]
date: "Wrocław 2021"
geometry: margin=3cm
numbersections: true
indent: true
header-includes: |
  \usepackage{tcolorbox}
  \usepackage{pdfpages}
  \usepackage[]{algorithm2e}
  \newcommand\qed{\hfill\rule{1em}{1em}}
---

\newtheorem{theorem}{Twierdzenie}
<!-- -------------------------------- -->

\tableofcontents

\newpage\null\newpage

# Wstęp

## Wprowadzenie

__Celem pracy jest porównanie różnych metod selekcji cech w problemie trenowania algorytmów uczenia maszynowego na danych niezbalansowanych. W jej ramach, przedstawione i opisane zostaną popularne obecnie metody selekcji oraz przeprowadzone zostaną eksperymenty dla przykadowych zbiorów danych, zarówno naturalnych jak i sztucznie wygenerowanych, celem których będzie stworzenie rankingu algorytmów. Autor sprawdzi, jak właściwie przeprowadzona selekcja wpływa na jakość wyników dostarczanych przez klasyfikator i jak przytoczone przez niego metody radzą sobie z danymi, w których występuje znaczna przewaga liczebności jednej
bądź kilku klas. Aspekt inżynieryjny opierać się będzie na implementacji zaproponowanych w pracy eksperymentów, co pozwoli na kompleksowe porównanie algorytmów..__
\vspace{3mm}

Praca swoim zakresem obejmie eksperymenty...

\vspace{3mm}
__Praca składa się z sześciu rozdziałów:__

\vspace{3mm}
__Rozdział pierwszy__: Omówienie analizy wybranego problemu, przedstawienie motywacji podjęcia tego tematu oraz...

\vspace{3mm}
__Rozdział drugi__: Przegląd literaturowy...

\vspace{3mm}
__Rozdział trzeci__: Szczegółowa charakterystyka zagadnienia...

\vspace{3mm}
__Rozdział czwarty__: Założenia i plan eksperymentu...

\vspace{3mm}
__Rozdział piąty__: Wyniki eksperymentów...

\vspace{3mm}
__Rozdział szósty__: Podsumowanie otrzymanych wyników, wnioski...

\vspace{3mm}
Udało się zrealizować wszystkie postawione cele.

\newpage\null\newpage

# Analiza problemu

__W tym rozdziale przedstawiona będzie analiza problemu...__

\vspace{3mm}
Uczenie maszynowe to bardzo dynamicznie rozwijająca się gałąź informatyki. Niezwykła ekspansja wynika z zapotrzebowania na wykrywanie prawidłowości, uogólnianie oraz precyzowanie danych. Takie możliwości pozwoliły znaleźć zastosowanie dla algorytmów sztucznej inteligencji w bardzo wielu różnych branżach - począwszy od medycyny, poprzez finanse, produkcję i branżę rozrywkową. Tak duży przekrój różnych zastosowań wymaga ciągłego ulepszania istniejących już wzorców oraz wymyślania nowych, lepszych i bardziej efektywnych algorytmów. Jednym z podstawowych etapów każdego programu bazującego na uczeniu maszynowym jest selekcja cech. Jest odpowiedzialna za wybór najbardziej istotnych atrybutów badanych obiektów, co przekłada się bezpośrednio na poprawne działanie klasyfikatora. Dyspozycja coraz większymi bazami danych zmusza do optymalizacji tego procesu. Gwałtownie rosnąca liczba cech stanowi poważny problem - powoduje nie tylko wydłużenie procesu uczenia oraz wzrost złożoności klasyfikatora, ale niesie ze sobą także ryzyko spadku poprawnej klasyfikacji. Związane jest to z tak zwanym ”przekleństwem wymiarowości”. Zjawisko to zachodzi, gdy ilość cech znacznie przewyższa liczebność samego zbioru danych.
Zadaniem selekcji cech jest również lepsze zrozumienie problemu oraz zmniejszenie kosztów archiwizacji przyszłych danych. W kolejnych rozdziałach opisane zostaną trzy główne metody tworzenia algorytmów selekcji: metody rankingowe - zwane filtrami, metody opakowane oraz metody wbudowane. Dla każdej z wymienionych metod zostanie określona idea, oraz przedstawione zostaną algorytmy reprezentujące daną metodologie.

\newpage\null\newpage

# Przegląd literaturowy

__W tym rozdziale zostaną pokrótce opisane wybrane artykuły naukowe zajmujące się tematyką selekcji cech. Jest to, szczególnie ostatnio, często poruszany 1problem, co skutkuje dużym przekrojem prac, również w ujęciu czysto dziedzinowym - jak wykorzystanie konkretnych algorytmów dla bardzo konkretnych zastosowań.__

Wstępną analizę problemu proponuje Jakub  Piątkowski w pracy _Analiza i rozwój metod selekcji cech dla dużych problemów klasyfikacyjnych_. Autor opisuje w pracy istniejące już, popularne metody selekcji cech z dokładnym opisem każdej z nich. Jest to dobry wstęp do samego problemu klasyfikacji i selekcji cech, każda z metod posiada również opisane wzorami zaplecze matematyczne. W podobnej pracy - _Redukcja wymiarowości i selekcja cech w zadaniach klasyfikacji i regresji z wykorzystaniem uczenia maszynowego_, twórca przytacza wyniki przeprowadzonych przez siebie eksperymentów, co pozwala mu na stworzenie rankingu algorytmów. Tezy postawione przez autora zostaną sprawdzone w niniejszej pracy. Bardzo szczegółowo do zagadnienia podszedł mgr Wiesław Chmielnicki, pisząc rozprawę _Efektywne metody selekcji cech i rozwiązywania problemu wieloklasowego w nadzorowanej klasyfikacji danych_. Poza opisem znanych metod, rozprawa zawiera propozycje nowych algorytmów hybrydowych, które pozwoliły uzyskać w niektórych przypadkach lepsze efekty, niż najpopularniejsze, używane zazwyczaj. Interesujący temat poruszył Mark A. Hall w swojej książe _Correlation-based Feature Selection for Machine Learning_, badając wartość zestawu cech na podstawie korelacji pomiędzy nimi. Autor prowadzi szereg eksperymentów porównując swoje metody do metod stosowanych ogólnie, starając się między innymi wyodrębnić problemy, dla których jego algorytm jest najbardziej skuteczny. Twórcy pracy _A Survey on Evolutionary Computation Approaches to Feature Selection_ zajęli się przeglądem znanych metod tworząc dokument podsumowujący każdą z nich, z jej wadami oraz zaletami. Artykuł jest oparty na przeglądzie najnowszych prac w zadanej dziedzinie i pozwala na dobranie odpowiedniej metody do zadanego zadania. Ważna dla tematu niniejszej pracy jest również rozprawa _Zastosowanie wybranych metod przekształcania i selekcji danych oraz konstrukcji cech w zadaniach klasyfikacji i klasteryzacji_ mgr inż. Piotra Płońskiego \cite{b3}, podsumowująca niejako cały proces uczenia maszynowego i roli, jaką pełni selekcja cech w kontekscie dobrze działającego systemu analizy danych.

\newpage\null\newpage

# Szczegółowa charakterystyka zagadnienia

__W tym rozdziale omówiona zostanie szczegółowa analiza zagadnienia.__

## Metody Rankingowe

Najprostsze podejście do problemu selekcji cech reprezentowane jest właśnie poprzez metody rankingowe, nazywane też filtrami. Jak sama nazwa wskazuje do zadania selekcji przy pomocy metod rankingowych podchodzimy wyróżniając w zbiorze cech następujące grupy: cechy istotne, nieistotne i redundantne. Istotne to takie cechy, które odróżniają od siebie klasy, nieistotne to takie których wartości dla problemu klasyfikacji są przypadkowe, a cechy redundantne to takie których role z powodzeniem mogą przyjąć inne cechy. Metody rankingowe polegają więc na znalezieniu pewnej miary pozwalającej stworzyć taki ranking cech, a potem wybrać najlepsze cechy, a odrzucić najgorsze.
Metody rankingowe zazwyczaj są najszybsze i - co istotne - nie zależą one od używanej metody analizy danych. Ich istotną wadą stanowi brak możliwości uwzględnienia zależności pomiędzy cechami. Kolejne opisane typy metod selekcji cech tej wady nie posiadają. 

## Metody opakowane

Podstawowymi metodami selekcji cech są metody opakowane, tak zwane wrappery. W przeciwieństwie do metod rankingowych, w których selekcja cech i klasyfikator pozostają niezależne, w algorytmach opakowanych selekcji, ocena atrybutów dokonuje się przy użyciu konkretnego modelu. To właśnie efektywność samego klasyfikatora służy za miarę skuteczności metody. Zaletą tej metody jest jej uniwersalność i dokładność, natomiast wadą - wysoka złożoność obliczeniowa. Dla efektywności tych algorytmów istotny jest sposób ustalania podzbioru cech. Wśród wielu metod wyszukiwania tegoż, wyróżnić można najprostszą - przeszukanie całego zbioru podzbiorów. Jest to jednak rozwiązanie bardzo kosztowne. Wobec tego typowymi strategiami są: przeszukiwanie w przód, przeszukiwanie wstecz oraz tworzenie indywidualnego rankingu.

## Metody wbudowane

Metody wbudowane zawierają się w algorytmie klasyfikacji i to na etapie tworzenia modelu przypisuje się poszczególnym cechom wagi lub przeprowadza się ich eliminację. Do algorytmów klasyfikacji z wbudowaną metodą selekcji zaliczyć można popularne LASSO i RIDGE. W literaturze natknąć się też można na przypasowanie do tej kategorii metody wektorów nośnych (SVM) czy też analizy składowych głównych (PCA). Zaletą tych metod jest ich szybkość, ponieważ użycie ich nie wiąże się z dodatkowymi operacjami na zbiorze. 

\newpage\null\newpage

# Założenia i plan eksperymentu

__Temat projektu zakłada przeprowadzenie serii eksperymentów porównujących efektywność popularnych metod selekcji cech. Bazy danych użyte do eksperymentów zakładają skupienie się na problemach wieloklasowych, których elementy są opisywane przez dużą ilość cech. Hipoteza, z którą twórcy będą konfrontować wyniki eksperymentów to założenie, że wszystkie metody selekcji cech poradzą sobie podobnie z postawionym zadaniem i poza względami wydajnościowymi, nie ma znaczenia funkcja, która zostanie użyta. W celu sprawdzenia hipotezy, postanowiono skorzystać skorzystać zarówno z gotowych rozwiązań pozwalających na generowanie syntetycznych problemów klasyfikacyjnych. Badania zostaną przeprowadzone z pomocą języka Python w wersji 3.8 oraz bibliotek: pandas, sklern i numpy. Sposób  generowania danych opisany został w rozdziale __Generowanie danych__. Kolejne eksperymenty zostały opisane poniżej..__

# Wyniki

\newpage\null\newpage

# Wnioski

\newpage\null\newpage

# Bibliografia

[1] \hspace{3mm} Feature Selection for High-Dimensional and Imbalanced Biomedical Data Based on Robust Correlation Based Redundancy and Binary Grasshopper Optimization Algorithm, Garba Abdulrauf Sharifai and Zurinahni Zaino; 2020.
\vspace{3mm}

[2] \hspace{3mm} A Survey on Evolutionary Computation Approaches to Feature Selection, Bing Xue; Mengjie Zhang; Will N. Browne; Xin Yao, 2015.
\vspace{3mm}

[3] \hspace{3mm} Correlation-based Feature Selection for Machine Learning, Mark A Hall, University of Waikato, 1999.
\vspace{3mm}

[4] \hspace{3mm} Efektywne metody selekcji cech i rozwiazywania problemu wieloklasowego w nadzorowanej klasyfikacji danych, Wieszław Chmielnicki, IPPT PAN, 2012
\vspace{3mm}

[6] \hspace{3mm} Zastosowanie wybranych metod przekształcania i selekcji danych oraz konstrukcji cech w zadaniach klasyfikacji i klasteryzacji, Piotr Płoński, Politechnika Warszawka, 2016.
\vspace{3mm}

[7] \hspace{3mm} Analiza i rozwój metod selekcji cech dla dużych problemów klasyfikacyjnych, Jakub Piątkowski, Uniwersytet Mikołaja Kopernika, 2006.
\vspace{3mm}

[8] \hspace{3mm} Feature Selection in Imbalance data sets, International Journal of Computer Science Issues, 2013.
\vspace{3mm}

\newpage\null\newpage

# Zawartość płyty CD

Do pracy dołączono płytę CD o następującej zawartości:

- kod źródłowy programu znajdujący się w folderze `/src`
\vspace{3mm}
- gotową, zbudowaną w katalogu `/dist` aplikację
\vspace{3mm}
- katalog `/docs` zawierający kod źródłowy tej pracy
\vspace{3mm}
- plik w formacie `pdf` zawierający pracę
