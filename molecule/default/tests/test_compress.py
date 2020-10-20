import os
from datetime import datetime

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('postgresql-backupgz')


def test_run_backup_script(host):
    # Note there's a small chance this test will incorrectly fail if it's run
    # run at midnight
    d = datetime.now()
    expected = ('/backup/postgresql/postgresql-backupgz-%s.pgdump.gz' %
                d.strftime('%Y%m%d'))

    with host.sudo():
        out = host.run('/etc/cron.daily/postgresql-backup')
    assert out.rc == 0
    assert out.stdout == ''

    f = host.file(expected)
    assert f.is_file

    with host.sudo():
        content = host.check_output('gunzip -c %s', expected)
    assert content.startswith(
        '--\n-- PostgreSQL database cluster dump\n--\n')
