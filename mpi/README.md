
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


~~~~

mpi communication problem.
eg
echo $SLURM_JOB_NODELIST |sed s/\,/\\n/g > hostfile

where hostfile has:
n0027.savio2
n0030.savio2

but mpirun complain like:
ssh: Could not resolve hostname n0030: Name or service not known

it is cuz it is not heeding FQDN.
one work around is to use IP.

see
https://github.com/open-mpi/ompi/issues/4732


By default, ORTE uses the short hostname mpi-worker as it assumes that all hosts are using the same domain. You can change this by setting this MCA parameter -mca orte_keep_fqdn_hostnames t.


so, maybe mpi was just compiled incorrectly.
which is why sometime it works, some other time it doesn't.
cuz was using diff version of mpi that was compiled w/ or w/o such param?


or, maybe set like this:
mpirun --mca orte_keep_fqdn_hostnames t

# this export seems to have done the trick! :)
export OMPI_MCA_orte_keep_fqdn_hostnames=t
 

ref: https://docs.oracle.com/cd/E19708-01/821-1319-10/mca-params.html

% ompi_info --param groupname groupname
% ompi_info --param btl all
% ompi_info --param all all
% ompi_info --param mpi mpi

not sure what group  OMPI_MCA_orte_keep_fqdn_hostnames  is in...

Parameter Group 		Description
mca  Specify paths or functions for MCA parameters
mpi  Specify MPI behavior at runtime
orte Specify debugging functions and components for ORTE
opal Specify stack trace information

has option for 
reading from a param file
ompi_info --param mca mca_param_files

