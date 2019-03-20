import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client
session = requests.session()

# Disable cert verification for demo purpose. 
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server='10.10.40.114', username='administrator@vsphere.local', password='C!sco12345', session=session)

# List all VMs inside the vCenter Server
vms = vsphere_client.vcenter.VM.list()

for vm in vms:
   if (vm.name[:5] == 'ucspe'):
      vm_instance = vsphere_client.vcenter.VM.get(vm.vm)
#      print(vm.name+" : ")
#      print(vm_instance.nics['4000'].label, vm_instance.nics['4000'].mac_address)
#      print(vm_instance.nics['4001'].label, vm_instance.nics['4001'].mac_address)
#      print(vm_instance.nics['4002'].label, vm_instance.nics['4002'].mac_address)
      num = int(vm.name[5:7])
      if (num < 31 ):
         print("host "+vm.name + "-1 { \n "+ "   hardware ethernet "+ vm_instance.nics[u'4000'].mac_address+"; \n"+"   fixed-address 10.10.85."+str(100+num)+"; \n }")
         print("host "+vm.name + "-2 { \n "+ "   hardware ethernet "+ vm_instance.nics[u'4001'].mac_address+"; \n"+"   fixed-address 10.10.85."+str(130+num)+"; \n }")
         print("host "+vm.name + "-3 { \n "+ "   hardware ethernet "+ vm_instance.nics[u'4002'].mac_address+"; \n"+"   fixed-address 10.10.85."+str(160+num)+"; \n }")
      else:
         print("host "+vm.name + "-1 { \n "+ "   hardware ethernet "+ vm_instance.nics[u'4000'].mac_address+"; \n"+"   fixed-address 10.10.86."+str(70+num)+"; \n }")
         print("host "+vm.name + "-2 { \n "+ "   hardware ethernet "+ vm_instance.nics[u'4001'].mac_address+"; \n"+"   fixed-address 10.10.86."+str(100+num)+"; \n }")
         print("host "+vm.name + "-3 { \n "+ "   hardware ethernet "+ vm_instance.nics[u'4002'].mac_address+"; \n"+"   fixed-address 10.10.86."+str(130+num)+"; \n }")
