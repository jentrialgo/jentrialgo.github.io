Title: A latex makefile: latexmk
Date: 2024-11-07 12:00
Category: LaTeX
Tags: LaTeX, makefile

I have been using LaTeX for a while now and I have always been annoyed by the fact that I
have to run the `pdflatex` command multiple times to get the references and the table of
contents right. Today, I colleague of mine told me about the `latexmk` command. It is a
tool that takes care of all the dependencies and runs the necessary commands to generate
the PDF file.

You can run:

```bash
latexmk -pdf yourfile.tex
```

And it will take care of everything. It will run `pdflatex` multiple times if necessary,
it will run `bibtex` if you have a bibliography, and it will generate the PDF file.
