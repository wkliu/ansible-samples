from ucsmsdk.utils.ucsbackup import backup_ucs
from ucsmsdk.ucshandle import UcsHandle

backup_dir = "/home/cisco/backup_ucs"
backup_filename = "config_backup.xml"

handle = UcsHandle("10.10.86.191", "admin", "cisco123")
handle.login()
backup_ucs(handle, backup_type="config-logical", file_dir=backup_dir, file_name=backup_filename)
handle.commit()
handle.logout()
