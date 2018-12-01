# this crated a smaller csv, but turns out all csv data is considered string, not number.  
# so need to create geojson instead 

# -rwxrwxrwx 1 root root 1709826 Nov 29 22:16 ZWEDC_Biofilter_10X_2016_LongLat.csv
# tin@Tin-T55:~/tin-gh/inet-dev-class/mapbox/TMP_DATA$ head -5 *csv
#  1  2     3     4   5   6
# "","lon","lat","x","y","aveconc","zelev","zhill","zflag","aveperiod","grp","rank","netid","date"
# "1",-121.985002139616,37.4079452829464,589827,4140612,0.18577,2.9,2.9,0,"1-HR","BIOFILTR","1ST","CART1","16122219"
# "2",-121.984437247048,37.4079404316778,589877,4140612,0.18817,3.4,3.4,0,"1-HR","BIOFILTR","1ST","CART1","16122219"


## cat ZWEDC_Biofilter_10X_2016_LongLat.csv | awk -F, '/^"\d/ {print $2 "," $3 "," $6}' > ZWEDC_3col.csv
cat ZWEDC_Biofilter_10X_2016_LongLat.csv | awk -F, '{print $2 "," $3 "," $6}' > ZWEDC_3col.csv
# vi and remove header line
# mapbox expects seq as lon lat

