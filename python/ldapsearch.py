#!/usr/bin/env python3 

# ref: https://stackoverflow.com/questions/4784775/ldap-query-in-python
import ldap
def found_in_ldap( user ):
        l = ldap.initialize('ldap://identity.lbl.gov:389')
        #binddn = "ou=people,dc=lbl,dc=gov"
        #pw = "myPassword"
        basedn = "ou=people,dc=lbl,dc=gov"
        #searchFilter = "(&(gidNumber=123456)(objectClass=posixAccount))"
        #searchFilter = "uid=wavalos"
        searchFilter = "uid=" . user
        searchAttribute = []
        #searchAttribute = ["mail","department"]
        #this will scope the entire subtree under UserUnits
        searchScope = ldap.SCOPE_SUBTREE
        #Bind to the server
        #try:
        #    l.protocol_version = ldap.VERSION3
        #    l.simple_bind_s(binddn, pw)
        #except ldap.INVALID_CREDENTIALS:
        #  print "Your username or password is incorrect."
        #  sys.exit(0)
        ##except ldap.LDAPError, e:
        #  if type(e.message) == dict and e.message.has_key('desc'):
        #      print e.message['desc']
        #  else:
        #      print e
        #  sys.exit(0)
        try:
            ldap_result_id = l.search(basedn, searchScope, searchFilter, searchAttribute)
            result_set = []
            while 1:
                result_type, result_data = l.result(ldap_result_id, 0)
                if (result_data == []):
                    break
                else:
                    ## if you are expecting multiple results you can append them
                    ## otherwise you can just wait until the initial result and break out
                    if result_type == ldap.RES_SEARCH_ENTRY:
                        result_set.append(result_data)
            #print result_set
        except ldap.LDAPError, e:
            print e
        l.unbind_s()
# END found_in_ldap( user )



def main():

    found_in_ldap(wavalos)
    exit( 007 )


if __name__ == '__main__':
    main()

