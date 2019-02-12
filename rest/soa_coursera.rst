

coursera SOA class


video: 4.3.2 (from week 3)

URI:

provide filter and paging, eg as param after ?

GET /courses?department=computing+science
GET /courses?offset=10&limit=5
	implications?
	what if the course list changed?
	client not sending a lit of classes... 



* use plural nouns for URI
* best practices also says to provide with filtering and paging for collection
* and remember proper http status code
* parent/child should be relations b/w resources.  eg students/SID, teachers/TID
  thus, it should be viewed as df/dirName , where dirName is like the ID, being a list {scratch, tmp, local, ...}





* should one call be get client list
* next call to get status against the list?
* SOA coursera class with student/SID for specific seems to imply such case (p69 of pdf)
    - but would this generate too much traffic??
    - really feel like each type of check should be a micro service URI (eg, one for ssh, one for ipmi)
      since each is very diff coding, and make sense to parallelize query to all host at once.



sub-resources relationship

GET /students/3/courses/2

I guess that's just a URI formatted "sql query", how server respond need not be exclusive of other queries.
"state" info is what's in the database.

for bofhbot_django, sinfo -RSE becomes the database, along with pdsh groups.




