import importlib.metadata as pkg_metadata
import logging

logger = logging.getLogger(__name__)

class MissingPackageError(Exception):
    """
    Exception raised when one or more required packages from project dependencies are missing.
    """

class WrongVersionPackageError(Exception):
    """
    Exception raised when one or more versions of the required packages from project dependencies are wrong.
    """


def check_installed_packages(
        requirements: str = 'requirements.in',
        stop_on_failure: bool = True,
):

    missing_packages = []
    wrong_version_packages = []
    packages = read_requirements_txt(requirements)

    for package_name, expected_version in packages.items():
        try:
            installed_version = pkg_metadata.version(package_name)
            if expected_version:
                if installed_version != expected_version:
                    wrong_version_packages.append((package_name, installed_version, expected_version))

        except pkg_metadata.PackageNotFoundError:
            missing_packages.append(package_name)

    if missing_packages:
        logger.warning("Required packages are missing: %s", ', '.join(missing_packages))
        if stop_on_failure:
            raise MissingPackageError

    if wrong_version_packages:
        for package, actual, expected in wrong_version_packages:
            logger.warning("Required package with wrong version: %s (Installed: %s, Expected: %s)", package, actual, expected)
        if stop_on_failure:
            raise WrongVersionPackageError


def read_requirements_txt(file_path):
    packages_to_check = {}

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        # remove comments of requirements.txt
        lines = [line.strip() for line in lines if
                 line.strip() and not line.startswith('#') and not line.startswith('    #')]
        for line in lines:

            packages_to_check.update(parse_requirement(line))

    return packages_to_check


def parse_requirement(req):

    req = req.replace(' ', '')  # requirements allow spaces, best to avoid.

    if not req.strip().startswith('#'):
        if '[' in req:
            parts = list(map(lambda x: x.replace(']', ''), req.split('[')))
            extras_parts = parts[1].split('==')
            if len(extras_parts) == 2:
                package_name, package_version = parts[0], extras_parts[1]
                return {package_name: package_version}

            elif len(extras_parts) == 1:
                return {parts[0]: None}


        if req.startswith('git+https://github.com/') or '@' in req:
            req = req.split(' ')[-1]
            parts = req.split('.git@')
            if len(parts) == 2:
                package_name = parts[0].split('/')[-1]
                package_version = parts[1].replace('v', '') if parts[1].startswith('v') else None
                return {package_name : package_version}

        else:
            parts = req.split('==')

            if len(parts) == 2:
                package_name, package_version = parts
                return {package_name: package_version}

            elif len(parts) == 1:
                return {parts[0]: None}


if __name__ == '__main__':
    check_installed_packages()

