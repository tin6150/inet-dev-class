
# MPI example codes


https://computing.llnl.gov/tutorials/mpi/exercise.html
https://computing.llnl.gov/tutorials/mpi/samples/C/mpi_hello.c

mpicc https://computing.llnl.gov/tutorials/mpi/samples/C/mpi_hello.c
/prog/OpenMPI/1.6.5-GCC-4.8.2/bin/mpicc 

/cm/shared/apps/openmpi/open64/64/1.8.1/bin/mpirun
mpirun -n 4 a.out 
qsub -pe orte 4 -cwd -j y -b y mpirun -np 4 a.out 
qsub -pe openmpi 4 -cwd -j y -b y -V mpirun -n 4 a.out 
qsub run_mpi_in_hpc.sh



eg https://people.sc.fsu.edu/~jburkardt/cpp_src/mpi/mpi.html
https://people.sc.fsu.edu/~jburkardt/cpp_src/hello_mpi/hello_mpi.cpp
hello_mpi.cpp ::

(the above cpp code use c binding.  
there are mpi bindings for c, python, fortran, etc)
