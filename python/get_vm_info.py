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
   if (vm.name[:5] == 'ucspe' or vm.name[:9] == 'ubuntu-hx'):
      vm_instance = vsphere_client.vcenter.VM.get(vm.vm)
      print(vm.name, vm_instance)
