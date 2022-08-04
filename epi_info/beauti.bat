:: this batch script successfully run beauti java gui on wombat.  run from dos prompt
:: program run, it is a windows java gui rather than unix java gui, but still cannot save xml :-\
:: 2022.0803
::
:: BEAST_LIB="$BEAST/lib"
:: #java -Xms64m -Xmx1024m -Djava.library.path="$BEAST_LIB" -jar "$BEAST_LIB/beauti.jar" $*
set BEAST_LIB="C:\Users\tin61\tin-gh-inet-class-only\inet-dev-class\epi_info\BEASTv1.10.5pre_thorney_0.1.0\lib"
:: set BEAST_LIB="BEASTv1.10.5pre_thorney_0.1.0\lib"
java -Xms64m -Xmx1024m -Djava.library.path="%BEAST_LIB%" -jar "%BEAST_LIB%/beauti.jar"


