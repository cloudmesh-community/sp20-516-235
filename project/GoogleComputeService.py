import os
from pprint import pprint as pp

import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

# CLIENT_SECRET_FILE = '/e516/cm/sp20-516-223/project/prefab-manifest-269104-744f67274f4b.json'
CLIENT_SECRET_FILE = '/e516/cm/<<HID>>/project/<<gcp_project>>-xxx.json'
COMPUTE_API_SERVICE_NAME = 'compute'
STORAGE_API_SERVICE_NAME = 'storage'
COMPUTE_API_VERSION = 'v1'
COMPUTE_API_SCOPES = ['https://www.googleapis.com/auth/compute', 'https://www.googleapis.com/auth/cloud-platform']
STORAGE_API_SCOPES = ['https://www.googleapis.com/auth/cloud-platform.read-only',
                      'https://www.googleapis.com/auth/devstorage.read_write']
PROJECT_ID = 'cloudmesh-270102'
BUCKET_NAME = 'cloudmesh-bucket'
ZONE = 'us-east'
MACHINE_TYPE = 'n1-standard-1'
SERVICE_ACCOUNT_EMAIL = 'cloudmesh-service-account@prefab-manifest-269104.iam.gserviceaccount.com'
START_UP_SCRIPT_PATH = '/e516/cm/sp20-516-235/project/'
START_UP_SCRIPT_FILE = 'gcp_vm_startup_script.sh'

def _get_credentials(client_secret_file, scopes):
    # Authenticate using service account.
    _credentials = service_account.Credentials.from_service_account_file(filename=client_secret_file,
                                                                         scopes=scopes)
    return _credentials


def _get_compute_service(service_account_credentials):
    compute_service = None
    # Authenticate using service account.
    if service_account_credentials is None:
        print('Credentials are required')
    else:
        compute_service = build(COMPUTE_API_SERVICE_NAME, COMPUTE_API_VERSION, credentials=service_account_credentials)

    return compute_service


def _get_storage_service(service_account_credentials):
    storage_service = None
    # Authenticate using service account.
    if service_account_credentials is None:
        print('Credentials are required')
    else:
        storage_service = build(STORAGE_API_SERVICE_NAME, STORAGE_API_SCOPES, credentials=service_account_credentials)

    return storage_service


def get_flavor(compute_service, flavor_project, family):
    source_disk_flavor = None
    # Get the images for the image project.
    try:
        flavor = compute_service.flavors().getFromFamily(project=flavor_project, family=family).execute()

    except Exception as e:
        print(f'Error in get_flavors {e}')
    return flavor


def get_flavors(compute_service, flavor_project):
    source_disk_flavor = None
    # Get the images for the image project.
    try:
        # Get list of images related to image project.
        flavor_response = compute_service.flavors().list(project=flavor_project).execute()
        # Extract the items.
        source_disk_flavor = flavor_response['items']

    except Exception as e:
        print(f'Error in get_flavors {e}')
    return source_disk_flavor