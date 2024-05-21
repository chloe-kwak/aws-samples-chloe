import importlib.metadata

def check_version(package_name):
    try:
        version = importlib.metadata.version(package_name)
        print(f"{package_name} version: {version} (type: {type(version)})")
        return version
    except importlib.metadata.PackageNotFoundError:
        print(f"Package {package_name} is not installed.")
    except Exception as e:
        print(f"Error checking version for {package_name}: {e}")

# List of packages to check
packages = ["fsspec", "datasets", "boto3", "mteb", "packaging"]

# Check versions
for package in packages:
    check_version(package)
