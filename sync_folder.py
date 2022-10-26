import argparse

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

