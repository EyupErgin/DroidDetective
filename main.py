import sys
from core.banner import print_banner
from core.analyzer import analyze_all, analyze_apk, get_file_info, get_file_hash, get_apk_info, get_apk_version_info, get_extended_info, print_list_info
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description="DroidDetective: Extended Static Analysis Tool for Analyzing Android APK Files.")
parser.add_argument("PATH", help="USAGE: python3 main.py file.apk")
parser.add_argument("-a", "--all", action="store_true", help="Run all options (suggested argument by developer)")
parser.add_argument("-fs", "--filesize", action="store_true", help="Display file size")
parser.add_argument("-fn", "--filename", action="store_true", help="Display file name")
parser.add_argument("-ft", "--filetype", action="store_true", help="Display file type")
parser.add_argument("-md5", "--md5hash", action="store_true", help="Display MD5 hash")
parser.add_argument("-sha1", "--sha1hash", action="store_true", help="Display SHA1 hash")
parser.add_argument("-sha256", "--sha256hash", action="store_true", help="Display SHA256 hash")
parser.add_argument("-an", "--appname", action="store_true", help="Include Application Name in output")
parser.add_argument("-pn", "--packname", action="store_true", help="Include Package Name in output")
parser.add_argument("-iv", "--intversion", action="store_true", help="Include Internal Version in output")
parser.add_argument("-dv", "--disversion", action="store_true", help="Include Displayed Version in output")
parser.add_argument("-tsdk", "--targetsdk", action="store_true", help="Include Target SDK Version in output")
parser.add_argument("-misdk", "--minsdk", action="store_true", help="Include Minimum SDK Version in output")
parser.add_argument("-masdk", "--maxsdk", action="store_true", help="Include Maximum SDK Version in output")
parser.add_argument("-perm", "--permissions", action="store_true", help="Include Permissions in output")
parser.add_argument("-acts", "--activities", action="store_true", help="Include Activities in output")
parser.add_argument("-serv", "--services", action="store_true", help="Include Services in output")
parser.add_argument("-recs", "--receivers", action="store_true", help="Include Receivers in output")
parser.add_argument("-json", "--json", action="store_true", help="Save outputs as JSON.")

args = parser.parse_args()

# Print banner
print_banner()

# Analyze APK
print("\n[+] [INFO] APK Analyze Started.")
if args.all:
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    analyze_all(args.PATH, args)
else:
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    analyze_apk(args.PATH, args)
print("\n[+] [INFO] APK Analyze Finished.")

