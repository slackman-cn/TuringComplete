/* 正如 Unix 的 wc 程序 */
%{
int chars = 0;
int words = 0;
int lines = 0;
%}
%%
[a-zA-Z]+   { words++; chars += strlen(yytext); }
\n          { chars++; lines++; }
.           { chars++; }
%%

main(int argc, char **argv)
{
yylex();
printf("lines=%d, words=%d, chars=%d\n", lines, words, chars);
}