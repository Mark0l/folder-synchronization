import argparse
import filecmp

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


folder_source = args.folder_source
folder_replica = args.folder_replica
sync_interval = args.sync_interval
log_file = args.log_file

# Compare Source and Replica folders
diff_result = filecmp.dircmp(folder_source, folder_replica, ignore=None, hide=None)
diff_result.report

to_copy = list(diff_result.diff_files + diff_result.left_only)
to_remove = diff_result.right_only

print(f'Files to copy: {to_copy}')
print(f'Files to remove: {to_remove}')
