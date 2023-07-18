import os
import sys
import json
import hashlib
from androguard.core.bytecodes.apk import APK
from datetime import datetime

def get_file_info(PATH):
    apk = APK(PATH)
    file_name = apk.get_filename()
    file_type = "APK"
    file_size = os.path.getsize(PATH)  # in bytes
    return file_name, file_type, file_size

def get_file_hash(PATH):
    with open(PATH, "rb") as file:
        file_data = file.read()

    hash_md5 = hashlib.md5(file_data).hexdigest()
    hash_sha1 = hashlib.sha1(file_data).hexdigest()
    hash_sha256 = hashlib.sha256(file_data).hexdigest()

    return hash_md5, hash_sha1, hash_sha256

def get_apk_info(PATH):
    apk = APK(PATH)
    app_name = apk.get_app_name()
    package_name = apk.get_package()
    return app_name, package_name

def get_apk_version_info(PATH):
    apk = APK(PATH)
    internal_version = apk.get_androidversion_code()
    displayed_version = apk.get_androidversion_name()
    target_sdk_version = apk.get_target_sdk_version()
    min_sdk_version = apk.get_min_sdk_version()
    max_sdk_version = apk.get_max_sdk_version()

    return internal_version, displayed_version, target_sdk_version, min_sdk_version, max_sdk_version

def get_extended_info(PATH):
    apk = APK(PATH)
    permissions = apk.get_permissions()
    activities = apk.get_activities()
    services = apk.get_services()
    receivers = apk.get_receivers()
    return permissions, activities, services, receivers

def print_list_info(title, items):
    sorted_items = sorted(items)  # Verileri alfabetik olarak sırala
    print(f"\n    {title}:")
    for item in sorted_items:
        print(f"       {item}")

def analyze_all(PATH, args):
    if args.all:
        file_name, file_type, file_size = get_file_info(PATH)
        file_hash_md5, file_hash_sha1, file_hash_sha256 = get_file_hash(PATH)
        app_name, package_name = get_apk_info(PATH)
        internal_version, displayed_version, target_sdk_version, min_sdk_version, max_sdk_version = get_apk_version_info(PATH)
        permissions, activities, services, receivers = get_extended_info(PATH)

        output = {}

        output["basicInfo"] = {}
        output["basicInfo"]["fileName"] = file_name
        output["basicInfo"]["fileSize"] = file_size
        output["basicInfo"]["fileType"] = file_type
        
        output["hashInfo"] = {}
        output["hashInfo"]["MD5"] = file_hash_md5
        output["hashInfo"]["SHA1"] = file_hash_sha1
        output["hashInfo"]["SHA256"] = file_hash_sha256

        output["apkInfo"] = {}
        output["apkInfo"]["applicationName"] = app_name
        output["apkInfo"]["packageName"] = package_name

        output["apkVersion"] = {}
        output["apkVersion"]["internalVersion"] = internal_version
        output["apkVersion"]["displayedVersion"] = displayed_version
        output["apkVersion"]["targetSDKVersion"] = target_sdk_version
        output["apkVersion"]["minimumSDKVersion"] = min_sdk_version
        output["apkVersion"]["maximumSDKVersion"] = max_sdk_version


        output["extendedAPKInfo"] = {}
        output["extendedAPKInfo"]["permissions"] = permissions
        output["extendedAPKInfo"]["activities"] = activities
        output["extendedAPKInfo"]["services"] = services
        output["extendedAPKInfo"]["receivers"] = receivers

    if args.json:
        timestamp = datetime.now().strftime("%d-%m-%Y")
        output_filename = f"{file_name}-{timestamp}.json"
        with open(output_filename, "w") as file:
            json.dump(output, file, indent=4)
        print(f"\n[+] [INFO] Output saved as JSON: {output_filename}")
        return
    
    if output:
        print("[+] Basic Info:")
        print("    - File Size:", file_size)
        print("    - File Name:", file_name)
        print("    - File Type:", file_type)

        print("\n[+] Hash Info:")
        print("    - MD5:", file_hash_md5)
        print("    - SHA-1:", file_hash_sha1)
        print("    - SHA-256:", file_hash_sha256)

        print("\n[+] APK Info:")
        print("    - Application Name:", app_name)
        print("    - Package Name:", package_name)

        print("\n[+] APK Version:")
        print("    - Internal Version:", internal_version)
        print("    - Displayed Version:", displayed_version)
        print("    - Target SDK Version:", target_sdk_version)
        print("    - Minimum SDK Version:", min_sdk_version)
        print("    - Maximum SDK Version:", max_sdk_version)
        

        print("\n[+] Extended APK Info:")
        sys.stdout.write("\033[F")
        print_list_info("- Permissions", permissions)
        print_list_info("- Activities", activities)
        print_list_info("- Services", services)
        print_list_info("- Receivers", receivers)

def analyze_apk(PATH, args):
    file_name, file_type, file_size = get_file_info(PATH)
    file_hash_md5, file_hash_sha1, file_hash_sha256 = get_file_hash(PATH)
    app_name, package_name = get_apk_info(PATH)
    internal_version, displayed_version, target_sdk_version, min_sdk_version, max_sdk_version = get_apk_version_info(PATH)
    permissions, activities, services, receivers = get_extended_info(PATH)

    if args.filename or args.filesize or args.filetype:
        print("[+] Basic Info:")
        if args.filename:
            print("    - File Name:", file_name)
        if args.filesize:
            print("    - File Size:", file_size)
        if args.filetype:
            print("    - File Type:", file_type)

    if args.md5hash or args.sha1hash or args.sha256hash:
        print("\n[+] Hash Info:")
        if args.md5hash:
            print("    - MD5:", file_hash_md5)
        if args.sha1hash:
            print("    - SHA-1:", file_hash_sha1)
        if args.sha256hash:
            print("    - SHA-256:", file_hash_sha256)

    if args.appname or args.packname:
        print("\n[+] APK Info:")
        if args.appname:
            print("    - Application Name:", app_name)
        if args.packname:
            print("    - Package Name:", package_name)

    if args.intversion or args.disversion or args.targetsdk or args.minsdk or args.maxsdk:
        print("\n[+] APK Version:")
        if args.intversion:
            print("    - Internal Version:", internal_version)
        if args.disversion:
            print("    - Displayed Version:", displayed_version)
        if args.targetsdk:
            print("    - Target SDK Version:", target_sdk_version)
        if args.minsdk:
            print("    - Minimum SDK Version:", min_sdk_version)
        if args.maxsdk:
            print("    - Maximum SDK Version:", max_sdk_version)

    if args.permissions or args.activities or args.services or args.receivers:
        print("\n[+] Extended APK Info:")
        if args.permissions:
            print_list_info("- Permissions", permissions)
        if args.activities:
            print_list_info("- Activities", activities)
        if args.services:
            print_list_info("- Services", services)
        if args.receivers:
            print_list_info("- Receivers", receivers)

    output = {}

    if output:
        print("[+] Basic Info:")
        print("    - File Size:", file_size)
        print("    - File Name:", file_name)
        print("    - File Type:", file_type)

        print("\n[+] Hash Info:")
        print("    - MD5:", file_hash_md5)
        print("    - SHA-1:", file_hash_sha1)
        print("    - SHA-256:", file_hash_sha256)

        print("\n[+] APK Info:")
        print("    - Application Name:", app_name)
        print("    - Package Name:", package_name)

        print("\n[+] APK Version:")
        print("    - Internal Version:", internal_version)
        print("    - Displayed Version:", displayed_version)
        print("    - Target SDK Version:", target_sdk_version)
        print("    - Minimum SDK Version:", min_sdk_version)
        print("    - Maximum SDK Version:", max_sdk_version)
        

        print("\n[+] Extended APK Info:")
        sys.stdout.write("\033[F")
        print_list_info("- Permissions", permissions)
        print_list_info("- Activities", activities)
        print_list_info("- Services", services)
        print_list_info("- Receivers", receivers)

