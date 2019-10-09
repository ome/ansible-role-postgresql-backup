import os
from datetime import datetime

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_run_backup_script(host):
    # Note there's a small chance this test will incorrectly fail if it's run
    # run at midnight
    d = datetime.now()
    expected = '/backup/postgresql/database-%s.pgdump' % d.strftime('%Y%m%d')

    with host.sudo():
        out = host.check_output('/etc/cron.daily/postgresql-backup')
    assert not out

    f = host.file(expected)
    assert f.is_file
    assert f.size > 2000
