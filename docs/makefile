all:
	make withtemplate

withtemplate:
	pdflatex header
	pandoc -f markdown+tex_math_dollars+tex_math_single_backslash --filter pandoc-xnos --bibliography bibliography.bib --citeproc --csl ./template/ieee.csl --template ./template/eisvogel -V lang=pl-PL -o temp.pdf praca_magisterska_maciej_hajduk.md
	# pandoc -o temp.pdf -V lang=pl-PL praca_magisterska_maciej_hajduk.md
	pdfunite header.pdf temp.pdf praca_magisterska_maciej_hajduk.pdf
	make clean

clean:
	rm temp.pdf header.pdf header.aux header.log || true
