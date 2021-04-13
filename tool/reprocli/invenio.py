
import os
import json
import urllib
import requests

from .models import CompendiumPack

INVENIO_RDM_RECORD_PATH = "/api/records"
INVENIO_RDM_RECORD_DRAFT_PATH = "/api/records/{rid}/draft/files"
INVENIO_RDM_RECORD_DRAFT_PATHS= "/api/records/{rid}/draft/files/{filename}/{method}"
INVENIO_RDM_RECORD_PUBLISH = "/api/records/{rid}/draft/actions/publish"


def compendium_ingest(invenio_url: str, compendium_pack: CompendiumPack, access_token: str) -> object:
    """Ingest a research compendium in a InvenioRDM server

    Args:
        invenio_url (str): InvenioRDM URL

        compendium_pack (CompendiumPack): CompendiumPack object with data and metadata
        information
        
        access_token (str): Token to access Brazil Data Cube provider
    Returns:
        object: HTTP-GET response
    """

    # general informations...   
    requests_header_in_json = {
        "Authorization": f"Bearer {access_token}"
    }

    # load compendium metadata
    with open(compendium_pack.metadata, "r") as f:
        metadata = json.load(f)

    # register upload material
    rh = requests_header_in_json.copy()
    rh["content-type"] = "application/json"
    
    records_endpoint = urllib.parse.urljoin(f"{invenio_url}", f"{INVENIO_RDM_RECORD_PATH}")
    
    metadata_record = requests.post(records_endpoint,
                                data=json.dumps(metadata),
                                headers=requests_header_in_json,
                                verify=False).json()

    rid = metadata_record["id"]
    
    # create a compendium
    file_basename = os.path.basename(compendium_pack.file)
    payload = [{
        "key": file_basename
    }]
    
    # register material that will be loaded
    records_draft_endpoint = INVENIO_RDM_RECORD_DRAFT_PATH.format(rid = rid)
    records_draft_endpoint = urllib.parse.urljoin(f"{invenio_url}", f"{records_draft_endpoint}")
    
    rh = requests_header_in_json.copy()
    rh["content-type"] = "application/json"
    
    requests.post(records_draft_endpoint,
                         data=json.dumps(payload),
                         headers=requests_header_in_json,
                         verify=False)

    # upload data
    records_upload_endpoint = INVENIO_RDM_RECORD_DRAFT_PATHS.format(
        rid = rid, 
        filename = file_basename,
        method = "content"
    )
    records_upload_endpoint = urllib.parse.urljoin(f"{invenio_url}", f"{records_upload_endpoint}")
        
    rh = requests_header_in_json.copy()
    rh["content-type"] = "application/octet-stream"
    
    requests.put(records_upload_endpoint,
                            data = open(compendium_pack.file, 'rb'),
                            headers = rh,
                            verify = False)

    # commit the draft
    records_commit_endpoint = INVENIO_RDM_RECORD_DRAFT_PATHS.format(
        rid = rid, 
        filename = file_basename,
        method = "commit"
    )
    records_commit_endpoint = urllib.parse.urljoin(f"{invenio_url}", f"{records_commit_endpoint}")

    requests.post(records_commit_endpoint, 
                 headers = requests_header_in_json,
                 verify = False)

    # publish the compendia!!
    records_publish = INVENIO_RDM_RECORD_PUBLISH.format(rid = rid)
    records_publish = urllib.parse.urljoin(f"{invenio_url}", f"{records_publish}")
    
    requests.post(records_publish,
                  headers = requests_header_in_json,
                  verify=False)
