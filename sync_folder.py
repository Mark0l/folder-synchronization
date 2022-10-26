import argparse
import filecmp
import os
import shutil
import time
from datetime import datetime


def compare_folders(folder1, folder2, pout=False):
    """
    Compare folder contents for src and dst

    :param folder1: first folder path
    :param folder2: second folder path
    :param pout: option to print items to copy/remove, default is False
    :return:
    """
    diff_result = filecmp.dircmp(folder1, folder2, ignore=None, hide=None)
    diff_result.report
    files_to_copy = list(diff_result.diff_files + diff_result.left_only)
    files_to_remove = diff_result.right_only
    if pout:
        print(f'Files to copy: {files_to_copy}')
        print(f'Files to remove: {files_to_remove}')

    return files_to_copy, files_to_remove


# Setting-up cmd line interaction
parser = argparse.ArgumentParser(description='Set up one-way folder synchronization and create operations log.')
parser.add_argument('folder_source', metavar='source', type=str, nargs=1,
                    help='source folder path to be synced from')
parser.add_argument('folder_replica', metavar='replica', type=str, nargs=1,
                    help='replica folder path to be synced to')
parser.add_argument('sync_interval', metavar='interval', type=int, nargs=1,
                    help='synchronization interval in which are folders compared')
parser.add_argument('log_file', metavar='log', type=str, nargs=1,
                    help='path to log file location')

args = parser.parse_args()

folder_source = args.folder_source[0]
folder_replica = args.folder_replica[0]
sync_interval = args.sync_interval[0]
log_file = args.log_file[0]
sync = 1

while sync:
    # Compare Source and Replica folders
    to_copy, to_remove = compare_folders(folder_source, folder_replica, False)

    if len(to_copy) != 0 or len(to_remove) != 0:
        # Sync folders
        for file in to_copy:
            shutil.copy2(os.path.join(folder_source, file), folder_replica)

        for file in to_remove:
            os.remove(os.path.join(folder_replica, file))

    # Log to cmd line
    time_now = datetime.utcnow()
    change_report = f'{time_now} UTC\n------------------------------\n{to_copy} copied\n{to_remove} removed\n'
    print(change_report)

    # Log to specified file
    with open(log_file, 'a') as log:
        log.write(change_report)

    # Synchronization interval 0 s means the sync is one-time only
    if sync_interval == 0:
        sync = 0
    else:
        time.sleep(sync_interval)