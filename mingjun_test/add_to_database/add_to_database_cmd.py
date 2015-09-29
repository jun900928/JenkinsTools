"""
This tools is to generate the build coomands by other build tools
"""
n=raw_input("Family(Lux): ")	#Lux

with open("job_list","r") as jobs:
	for job in jobs.readlines():
		group=job.strip()
		g=group.rsplit('.',1)[0].split('_',1)[-1]
		print "/apps/tools/scm_tools/hudson_tools/format_ProductConfig_files.pl %s" %group

		print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl -product_group %s "\
		      " -task add_product_group -test_db" %g
		print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl -product_group %s "\
		      " -task add_product_group " %g     
		print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl "\
		      "-family %s -product %s -product_group %s -task add -test_db " %(n,g,g)
		print "/apps/tools/scm_tools/hudson_tools/add_product_to_database.pl "\
		      "-family %s -product %s -product_group %s -task add  " %(n,g,g)
