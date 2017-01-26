#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe orte 4    
## #$ -pe openmpi 4
#$ -l m_mem_free=1G
#$ -l h_rt=600
  
  #
  # Use modules to setup the runtime environment
  #
  export MODULEPATH=/prog/modules/all:$MODULEPATH
  module purge
  #module load openmpi/open64/64/1.8.1
  module load OpenMPI/1.6.5-GCC-4.8.2-X

  # Execute the run
  mpirun -np 4 ./a.out
