#!/bin/bash
#
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -M tin.ho@novartis.com
## #$ -pe orte 4    # has 0 slot, something not configured?
#$ -pe openmpi 4
#$ -l m_mem_free=1G
#$ -l h_rt=600
  
  #
  # Use modules to setup the runtime environment
  #
  export MODULEPATH=/usr/prog/modules/all:$MODULEPATH
  module purge
  module load openmpi/open64/64/1.8.1

  # Execute the run
  mpirun -np 4 sh ./worker_script.sh
