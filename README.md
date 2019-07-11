PostgreSQL Backup
=================

[![Build Status](https://travis-ci.org/ome/ansible-role-postgresql-backup.svg)](https://travis-ci.org/ome/ansible-role-postgresql-backup)
[![Ansible Role](https://img.shields.io/ansible/role/42001.svg)](https://galaxy.ansible.com/ome/postgresql_backup/)

Setup a cron job for regular full PostgreSQL database dumps.

Assumes the local `postgres` has password-less access to all databases (this is the default when installing PostgreSQL server).


Dependencies
------------

This requires a cron daemon to already be running.
This should be the default on most systems.


Role Variables
--------------

Required:
- `postgresql_backup_dir`: Save backups in this directory

Optional:
- `postgresql_backup_filename_format`: A filename containing unix `date` format sequences, default `{{ ansible_hostname }}-%Y%m%d-%H%M%S.pgdump`.
  This can be used to automatically overwrite backups on a rolling basis.
- `postgresql_backup_frequency`: This must match one of the standard `/etc/cron.*` directories, typically either `daily` (default), `hourly`, `weekly` or `monthly`.
- `postgresql_backup_minimum_expected_size`: The minimum size in bytes of the backup file.
  The cron job will return an error if the file is smaller than this.


Example playbook
----------------

    # This will name the backup file /nfs/backups/HOSTNAME-Mon.pgdump
    # where Mon will be replaced by the abbreviated day of the week, resulting
    # in daily backups on a rolling weekly cycle
    - hosts: postgresql-servers
      roles:
      - role: ome.postgresql_backup
        postgresql_backup_dir: /nfs/backups
        postgresql_backup_filename_format: "{{ ansible_hostname }}-%a.pgdump"
        postgresql_backup_minimum_expected_size: 100000


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
