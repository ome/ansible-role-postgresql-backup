MySQL Backup
============

Setup a cron job for regular full Mysql/Mariadb database dumps.

Assumes `root` has password-less access to all databases.


Dependencies
------------

This requires a cron daemon to already be running.
This should be the default on most systems.


Role Variables
--------------

Required:
- `mysql_backup_dir`: Save backups in this directory

Optional:
- `mysql_backup_filename_format`: A filename containing unix `date` format sequences, default `{{ ansible_hostname }}-%Y%m%d-%H%M%S.mysqldump`.
  This can be used to automatically overwrite backups on a rolling basis.
- `mysql_backup_frequency`: This must match one of the standard `/etc/cron.*` directories, typically either `daily` (default), `hourly`, `weekly` or `monthly`.
- `mysql_backup_minimum_expected_size`: The minimum size in bytes of the backup file.
  The cron job will return an error if the file is smaller than this.


Example playbook
----------------

    # This will name the backup file /nfs/backups/HOSTNAME-Mon.mysqldump
    # where Mon will be replaced by the abbreviated day of the week, resulting
    # in daily backups on a rolling weekly cycle
    - hosts: mysql-servers
      roles:
      - role: mysql-backup
        mysql_backup_dir: /nfs/backups
        mysql_backup_filename_format: "{{ ansible_hostname }}-%a.mysqldump"
        mysql_backup_minimum_expected_size: 100000


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
