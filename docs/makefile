all:
	make withtemplate

withtemplate:
	pdflatex header
	pandoc -f markdown+tex_math_dollars+tex_math_single_backslash --filter pandoc-fignos --filter pandoc-eqnos --filter pandoc-tablenos --template eisvogel -V lang=pl-PL -o temp.pdf praca_magisterska_maciej_hajduk.md
	# pandoc -o temp.pdf -V lang=pl-PL praca_magisterska_maciej_hajduk.md
	pdfunite header.pdf temp.pdf praca_magisterska_maciej_hajduk.pdf
	make clean
	make cleanmd

clean:
	rm temp.html temp.pdf header.pdf header.aux header.log || true

cleanmd:
	rm temp.pdf
