'''
A module for interacting with a user's crontab.
'''

import subprocess


def list_crontab(user):
    '''
    Return the cron entries for the named user, in this format:

    ['entry line', 'entry line', ...]

    CLI Example:
    salt '*' cron.list_crontab <username>
    '''
    cmd = 'crontab -u %s -l' % user

    # TODO: Make sure errors are handled appropriately
    output = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE).communicate()[0]
    return output.splitlines()
