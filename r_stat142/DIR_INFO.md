


====>> **consider moving this to my fork under phw142-sp22**  <<===
if do, this and other annotabion may want to be in a "tin" branch
	But adding class project here, under prj/
	working from inside Rstudio, under tin@wombat:/mnt/c/Users/tin61/tin-gh/inet-dev-class/r_stat142 wsl bash


R lab (required) and assignments (optional) for Stat 142 (Spring 2022)
from datahub terminal, in 

careful not to copy the .git from the source, as they are also using git to create these files.
hmm... maybe i should just fork it!
see https://github.com/tin6150/phw142-sp22

rstudio@jupyter-tin:~/phw142-sp22$ scp -pr /home/rstudio/phw142-sp22/* tin@bofh.lbl.gov:~/tin-gh/inet-dev-class/r_stat142

``` {bash}
find . -name '*md' -exec git add {} \;
find . -name '*csv' -exec git add {} \;
find . -name '*PNG' -exec git add {} \;
# might need lower case png?  
```

~~~~~


IP of datahub is??   probably in the cloud, tmp: ufw disable

https://publichealth.datahub.berkeley.edu/user/tin/rstudio/


first copy on 2022.0122, beginning of the semester, most files are not released yet.
i have done edit to lab01.Rmd, about to submit to autograder.
no work on hw yet.
may be won't be syncing them unless really want to use local Rstudio, which i likely won't, as submission may become a mess.

consider copying files at end of semester... 



rstudio@jupyter-tin:~/phw142-sp22$ ifconfig -a | less
bash: ifconfig: command not found
rstudio@jupyter-tin:~/phw142-sp22$ 
rstudio@jupyter-tin:~/phw142-sp22$ ls
hw  lab  lec  Welcome-To-PH142.md
rstudio@jupyter-tin:~/phw142-sp22$ pwd
/home/rstudio/phw142-sp22
rstudio@jupyter-tin:~/phw142-sp22$ scp -pr /home/rstudio/^C
rstudio@jupyter-tin:~/phw142-sp22$ df -h .
Filesystem                                        Size  Used Avail Use% Mounted on
nfsserver-01:/export/ischool-2021-07-01/prod/tin  1.0T  457G  568G  45% /home/rstudio
rstudio@jupyter-tin:~/phw142-sp22$ pwd -P
/home/rstudio/phw142-sp22
rstudio@jupyter-tin:~/phw142-sp22$ scp -pr /home/rstudio/phw142-sp22/* tin@bofh.lbl.gov:~/tin-gh/inet-dev-class/r_stat142