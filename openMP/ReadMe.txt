
# http://www.dartmouth.edu/~rc/classes/intro_openmp/compile_run.html
# gcc 4.4 and above
cc  -fopenmp hello_llbl.c
gcc -fopenmp hello_llbl.c
icc -openmp  hello_slac.c

export OMP_NUM_THREADS=4    
# if not specified, run as many threads as available cpu cores (or hyperthreads if enabled)
# if ask for more threads than avail cores, the OS will sequentialize them.
./a.out


# slac example is good for sequential code when openMP not avail.
# llbl example is good that it fails when openMP not avail, easier to learn.
#


# ref:
# http://pawangh.blogspot.com/2014/05/mpi-vs-openmp.html
# https://tin6150.github.io/psg/mpi.html 
