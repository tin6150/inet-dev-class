

## slurm job script for running BEAST v1 
## in dev
## for now it is just a bash script for run directly on host
## eg run:
## n264s3>  bash -x slurm_job.sh | tee tut_flu/beast_job.OUT.TXT

# BEAAST processing xml (java program, need beagle lib, which could use accel from CUDA)
# ref README.rst and PDF for commands to run

export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$HOME/lib/pkgconfig:$PKG_CONFIG_PATH

# these are used to build beagle, likely needed for execution
module load cmake/3.22.0    # from consultsw
module load java/1.8.0_121
module load cuda/11.2

PID=$$

## I dont like this method and no longer used
run_rate_tut_cd_JAR_DIR() {
	BEAST_XML=/global/home/users/tin/tin-gh/inet-dev-class/epi_info/tut_rate/SnYFV.xml
	BEAST_JAR_DIR=/global/home/users/tin/tin-gh/inet-dev-class/epi_info/travHistProtocol/software/
	cd $BEAST_JAR_DIR
	java -cp beast.jar dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state YFV.checkpoint   $BEAST_XML
}

#### prefer to run on dir with input XML instead of cd to the jar dir.
#### so using the method below instead
BEAST_JAR=/global/home/users/tin/tin-gh/inet-dev-class/epi_info/travHistProtocol/software/beast.jar

## tutorial 1: Rate
run_tut_rate() {
	#### to make it run longer or shorter, change XML param chainLength="10000"
	cd /global/home/users/tin/tin-gh/inet-dev-class/epi_info/tut_rate
	java -cp $BEAST_JAR dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state Beast.chkpt -overwrite   ./SnYFV.xml
	exit $?
}


## tutorial 2: Influenza evo
run_tut_flu() {
    BEAST_XML=Sn_H1N1pdm_2009.xml
	cd /global/home/users/tin/tin-gh/inet-dev-class/epi_info/tut_flu
	java -cp $BEAST_JAR dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state Beast.chkpt -overwrite   $BEAST_XML
	exit $?
}


## the orig COVID paper with chainLength=200M  
run_SARS_CoV2() {
	##++ may try to rerun below in V100 as slurm job with the orig 200M chainLegth
	cd /global/home/users/tin/tin-gh/inet-dev-class/epi_info/travHistProtocol/files/Protocol3
    BEAST_XML=282_GISAID_sarscov2_travelHist_masked_Sn100k.xml
	java -cp $BEAST_JAR dr.app.beast.BeastMain -seed 2020 -beagle_double -beagle_gpu -save_every 1000000 -save_state Beast.chkpt  -overwrite  $BEAST_XML
## ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml   # cranking on n0262.s4, cuda 11.2
##travelHist.checkpoint ../files/Protocol3/282_GISAID_sarscov2_travelHist_masked.xml

}




####
#### "main" here
####
date
echo "====INFO===="
java -cp $BEAST_JAR dr.app.beast.BeastMain -beagle_info

echo "====Starting the BEAST===="
#run_tut_rate
#run_SARS_CoV2  ## chainLegth=100k  for now , n0264.s3
#run_tut_flu
# all commented out, dont want to rerun accidentally

echo $?
echo "====BEAST done===="
date

