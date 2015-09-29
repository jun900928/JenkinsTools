print "group name"
g=raw_input()
print "input NPI"
n=raw_input()
print "input prefix"
p=raw_input()

print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl -product_group %s "\
      " -task add_product_group -test_db" %g
print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl -product_group %s "\
      " -task add_product_group " %g     
print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl -jira_prefix %s "\
      "-family %s -product %s -product_group %s -task add -test_db " %(p,n,g,g)
print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl -jira_prefix %s "\
      "-family %s -product %s -product_group %s -task add  " %(p,n,g,g)
