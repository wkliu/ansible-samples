import requests
import urllib3
from com.vmware.vcenter.vm_client import Power
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
      vm_instance_status = vsphere_client.vcenter.vm.Power.get(vm.vm)
      if vm_instance_status == Power.Info(state=Power.State.POWERED_ON):
         print(vm.name+": Power ON")
      else: 
         print(vm.name+": "+str(vm_instance_status))
         vm_instance_status = vsphere_client.vcenter.vm.Power.start(vm.vm)
      #print(vm.name, vm_instance)
