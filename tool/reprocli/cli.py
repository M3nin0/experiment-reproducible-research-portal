
import click
import emoji

from reprocli import packer
from reprocli import invenio


@click.group()
def cli():
    """
    :return:
    """
    pass


@cli.command(name="ingest", help="Function to ingest a Research Compendium in a invenio instance")
@click.option('--compendium', required=True, help='Research Compendium path')
@click.option('--invenio-access-token', required=True, help='Invenio RDM Access Token')
@click.option('--invenio-service-url', required=True, help='Invenio RDM URL')
def ingest_to_invenio_cli(compendium: str, invenio_access_token: str, invenio_service_url: str):
    """Function to ingest a Research Compendium in a invenio instance
    """

    print(emoji.emojize(':package: Welcome to ReproCLI. We will ingest your package'))
    print(emoji.emojize(':package: Creating the BagIt'))
    compendium_pack = packer.compendium_pack(compendium)

    print(emoji.emojize(':package: Upload to Invenio'))
    invenio.compendium_ingest(invenio_service_url, compendium_pack, invenio_access_token)

    print(emoji.emojize(':rocket: Done!'))
