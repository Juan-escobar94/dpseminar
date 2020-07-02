pdflatex -shell-escape dynamicprogramming &&
bibtex dynamicprogramming &&
pdflatex -shell-escape dynamicprogramming &&
pdflatex -shell-escape dynamicprogramming &&
evince dynamicprogramming.pdf

# optionally use 
#  latexmk -pdf -shell-escape dynamicprogramming.texx