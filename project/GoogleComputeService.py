import os
from pprint import pprint

import time
from google.oauth2 import service_account
from googleapiclient.discovery import build


CLIENT_SECRET_FILE = '/Users/yasirjasim/.cloudmesh/google1.json'
COMPUTE_API_SERVICE_NAME = 'compute'
STORAGE_API_SERVICE_NAME = 'storage'
COMPUTE_API_VERSION = 'v1'
COMPUTE_API_SCOPES = ['https://www.googleapis.com/auth/compute', 'https://www.googleapis.com/auth/cloud-platform']
STORAGE_API_SCOPES = ['https://www.googleapis.com/auth/cloud-platform.read-only',
                      'https://www.googleapis.com/auth/devstorage.read_write']
PROJECT_ID = 'cloudmesh-270102'
ZONE = 'us-east1-b'
MACHINE_TYPE = 'n1-standard-1'

def _get_credentials(client_secret_file, scopes):
    # Authenticate using service account.
    print("start here- ------------------------------")
    print(client_secret_file)
    print(scopes)
    _credentials = service_account.Credentials.from_service_account_file(filename=client_secret_file,
                                                                             scopes=scopes)
    return _credentials


def _get_compute_service(service_account_credentials):
    compute_service = None



    # Authenticate using service account.
    if service_account_credentials is None:
        print('Credentials are required')
    else:
        # print(service_account_credentials)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_credentials

        compute_service = build(COMPUTE_API_SERVICE_NAME, COMPUTE_API_VERSION)

        # print(compute_service)
    return compute_service


def _get_storage_service(service_account_credentials):
    storage_service = None
    # Authenticate using service account.
    if service_account_credentials is None:
        print('Credentials are required')
    else:
        storage_service = build(STORAGE_API_SERVICE_NAME, STORAGE_API_SCOPES, credentials=service_account_credentials)

    return storage_service

def flavor(self, name):
    """
    Gets the flavor with a given name
    :param name: The name of the flavor
    :return: The dict of the flavor
    """
    comput_servce = _get_compute_service(CLIENT_SECRET_FILE)
    flavor = _get_flavor(comput_servce, PROJECT_ID, ZONE, name)
    return flavor

def _get_flavor(compute_service, project_id, zone, name):
    # Get the flavor for the project_id.
    flavor = None;
    try:
        flavor = compute_service.machineTypes().get(project=project_id, zone=zone, machineType=name).execute()
    except Exception as e:
        print(f'Error in get_flavors {e}')
    return flavor



def flavors(self, **kwargs):
    """
    Lists the flavors on the cloud

    :return: dict of flavors
    """
    comput_servce = _get_compute_service(CLIENT_SECRET_FILE)
    project_id = kwargs.get('project_id',PROJECT_ID)
    zone = kwargs.get('zone', ZONE)
    return _get_flavors(comput_servce, project_id, zone)

def _get_flavors(compute_service, project_id, zone):
    source_disk_flavor = None
    # Get the flavors for the image project.
    try:
        # Get list of images related to image project.
        flavor_response = compute_service.machineTypes().list(project=project_id, zone=zone).execute()
        # Extract the items.
        source_disk_flavor = flavor_response['items']
        # print('flavors 2')
    except Exception as e:
        print(f'Error in get_flavors {e}')
    return source_disk_flavor

if __name__ == "__main__":

    # print('flavor1 :')
    # pprint(flavor(MACHINE_TYPE, name='n1-standard-1'))
    #
    # print('flavor2 :')
    # pprint(flavor(MACHINE_TYPE, name='n1-standard-2'))

    print('flavors')
    print('Enter Zone:')
    ZONE = input()
    args={"project_id":PROJECT_ID, "zone":ZONE}
    pprint(flavors(args))

    # us-central1   a, b, c, f
    # us-east1      b, c, d
    # us-east4      a, b, c
    # us-west1      a, b, c
    # us-west2      a, b, c
    # us-west3      a, b, c










