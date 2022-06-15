

## slurm job script for running BEAST v1 
## in dev


# see README.rst and PDF for commands to run
# BEAAST processing xml (java program, need beagle lib, which could use accel from CUDA)

export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$HOME/lib/pkgconfig:$PKG_CONFIG_PATH

# these are used to build beagle, likely needed for execution
module load cmake/3.22.0    # from consultsw
module load java/1.8.0_121
module load cuda/11.2


## may need to cd
## and check path...
cd /global/home/users/tin/tin-gh/inet-dev-class/epi_info/tut_rate


BEAST_JAR=/global/home/users/tin/tin-gh/inet-dev-class/epi_info/travHistProtocol/software/beast.jar

java -cp beast.jar dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state YFV.checkpoint   \
 ./SnYFV.xml
 ##  ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml   # cranking on n0262.s4, cuda 11.2
