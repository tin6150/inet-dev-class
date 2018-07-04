#!/usr/bin/env python

# example function to search ldap for user
#
# some strange problem with python3, so sticking with python2 for now.
# ref: 
# https://www.adimian.com/blog/2014/10/basic-ldap-actions-using-python/
# https://www.python-ldap.org/en/latest/installing.html#build-prerequisites
# https://www.python-ldap.org/en/latest/reference/ldap.html?highlight=initialize


# one-time setup:
# module load python/2.7
# virtualenv ~/local_python_2.7
# source ~/local_python_2.7/bin/activate
# pip install python-ldap
#
# pip uninstall ldap # if it complains don't have ldap.initialize()


import ldap


def found_in_ldap( user ):
		#print ldap.__file__
		con = ldap.initialize('ldap://identity:389')
		ldap_base = "ou=people,dc=lbl,dc=gov"
		#searchAttribute = ["uid","cn","mail"]
		searchAttribute = ["mail"]
		#query = "(uid=wavalos)"
		query = "(uid=%s)" % user		# uid is loginname eg "wavalos"
		#query = "(sn=%s)" % user		# sn is "surname"
		#query = "(givenname=%s)" % user
		#result_set = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)    # unfiltered results
		result_set = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query, searchAttribute)
		print( result_set )
		print( len(result_set) )	# number of matches
		#return result_set		# could return full result for caller to handle if desired
		return len(result_set)
# END found_in_ldap( user )



def main():
    found_in_ldap("wendy")
    result_set = found_in_ldap("tin")
    print( result_set )
    print( "===" )
    found_in_ldap("foobar")
    if found_in_ldap("wavalos") :
       print( "found wavalos" )
    return 0 
# END main()


if __name__ == '__main__':
    main()

