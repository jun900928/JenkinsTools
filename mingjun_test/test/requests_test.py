import requests

auth = requests.auth.HTTPBasicAuth('mingjunl', 'LMJ900928mg~')

request_args = {
                        'allow_redirects' : True,
                        'auth'            : auth,
                        'verify'          : False,
                       }
request = requests.get('https://jenkins.mot.com/job/LPH23.95-F1_clark-factory_userdebug_factory-clark-mlmp-mr1_8992_release-keys_continuous_cid/', **request_args)
print request

headers = {'content-type': 'application/xml'}
request = requests.post('https://jenkins.mot.com/job/z_mingjun_tools_LPB23.13-PD-Peregrine-ATT-signed_builda_09/config.xml',open('config.xml','rb'), **request_args)
print request
