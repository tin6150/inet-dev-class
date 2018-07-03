#!/usr/bin/env python

# ref: https://www.adimian.com/blog/2014/10/basic-ldap-actions-using-python/
# pip install python-ldap
# https://www.python-ldap.org/en/latest/installing.html#build-prerequisites
import ldap


def found_in_ldap( user ):
		con = ldap.initialize('ldap://identity.lbl.gov:389')

		ldap_base = "ou=people,dc=lbl,dc=gov"
		#query = "(uid=maarten)"
		query = "(uid=%s)" % user
		result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
		return 0
		#print( result )
		#retrun True 
		#exit 0
# END found_in_ldap( user )



def main():
    found_in_ldap("wavalos")
    return 7 
# END main()


if __name__ == '__main__':
    main()

