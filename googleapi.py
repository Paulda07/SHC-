from googleapiclient import discovery
from google.oauth2 import service_account
from google.auth.transport import requests
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import boto3

api_key=AIzaSyA39s4YUC9wuMjZiyIRRo3spidQadqlDsc

def get_client(service_account_json, api_key):
    api_scopes = ['https://www.googleapis.com/auth/cloud-platform']
    api_version = 'v1beta1'
    discovery_api = 'https://healthcare.googleapis.com/$discovery/rest'
    service_name = 'healthcare'
    credentials = service_account.Credentials.from_service_account_file(service_account_json)
    scoped_credentials = credentials.with_scopes(api_scopes)

    discovery_url = '{}?labels=CHC_BETA&version={}&key={}'.format(
        discovery_api, api_version, api_key)

    return discovery.build(
        service_name,
        api_version,
        discoveryServiceUrl=discovery_url,
        credentials=scoped_credentials)
def get_session(service_account_json):

    credentials=service_account.Credentials.from_service_account_file(service_account_json)
    scoped_credentials= credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
    session = requests.AuthorizedSession(scoped_credentials)


    return session

