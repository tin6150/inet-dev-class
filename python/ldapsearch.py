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

def found_alias_in_ldap( user ):
		con = ldap.initialize('ldap://identity.lbl.gov:389')
		ldap_base = "ou=people,dc=lbl,dc=gov"
		#searchAttribute = ["uid","cn","lblGoogleAccountName", "lblAccountStatus"]
		searchAttribute = ["lblGoogleAccountName"]
		#searchAttribute = ["mail"]
		query = "(lblAccountUsernameAlias=%s)" % user		# 
		#result_set = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)    # unfiltered results
		result_set = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query, searchAttribute)
		#print( result_set )
		#print( len(result_set) )	# number of matches
		if( len(result_set) > 0 ) :
			#return result_set[0]
			(a,b) = result_set[0]
			#print( "a==>%s<==" % a )
			#print( "b==>%s<==" % b )
			print( "dict==>%s<==" % b['lblGoogleAccountName'] )
			return b['lblGoogleAccountName']
		else :
			#return "Username Not Found"
			return False
# END found_alias_in_ldap( user )



def found_in_ldap( user ):
		#print ldap.__file__
		con = ldap.initialize('ldap://identity.lbl.gov:389')
		ldap_base = "ou=people,dc=lbl,dc=gov"
		#searchAttribute = ["uid","cn","mail"]
		#searchAttribute = ["mail"]
		searchAttribute = ["lblGoogleAccountName"]
		#query = "(uid=wavalos)"
		query = "(uid=%s)" % user		# uid is loginname eg "wavalos"
		#query = "(sn=%s)" % user		# sn is "surname"
		#query = "(givenname=%s)" % user
		#result_set = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)    # unfiltered results
		result_set = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query, searchAttribute)
		print( result_set )
		#print( len(result_set) )	# number of matches
		
		if( len(result_set) > 0 ) :
			#return result_set[0]
			(a,b) = result_set[0]
			#print( "a==>%s<==" % a )
			#print( "b==>%s<==" % b )
			print( "dict==>%s<==" % b['lblGoogleAccountName'] )
			return b['lblGoogleAccountName']
		else :
			#return "Username Not Found"
			return False
			#return len(result_set)
		#return len(result_set)
# END found_in_ldap( user )



def main():
    print( "==Looking for alias==" )
    result_set = found_alias_in_ldap("zmk")
    print( result_set )

    print( "*************" )
    print( "==Looking for mhg in 2 step...==" )
    result = found_in_ldap("mhg")
    if result : 
       print( "found mhg" )
    else : 
       print( "user not found, searching for alias" )
       result = found_alias_in_ldap("mhg")
       if result : 
           print( result )
       else :
           print( "no alias found either" )
    print( "*************" )


    result = found_alias_in_ldap("mhg")
    print( result_set )

    print( "==Looking for tin==" )
    result = found_in_ldap("tin")
    print( "got response of: %s" % result )

    print( "==Looking for foobar==" )
    result = found_in_ldap("foobar")
    print( "got response of: %s" % result )

    print( "==Looking for wendy==" )
    if found_in_ldap("wendy") :
       print( "found wendy" )
    else : 
       print( "not found wendy" )

    print( "==Looking for wavalos==" )
    if found_in_ldap("wavalos") :
       print( "found wavalos" )

    return 0 
# END main()


if __name__ == '__main__':
    main()

