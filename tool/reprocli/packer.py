import os
import bagit
import shutil
import tempfile

from .models import CompendiumPack


def compendium_pack(compendium_directory: str, compendium_out: str = None) -> CompendiumPack:
    """BagIt a Compendium

    Args:
        compendium_directory (str): Research Compendium Path

        compendium_out (str): output directory for compendium
    Returns:
        CompendiumPack: object with general informations about the created pack
    """

    # temporary file
    tmp = tempfile.mkdtemp()

    # extract metadata
    compendium_metadata = os.path.join(compendium_directory, "metadata.json")
    compendium_metadata_tmp = os.path.join(tmp, "metadata.json")

    shutil.copy(compendium_metadata, compendium_metadata_tmp)

    # ToDo: Change this "processos" to a arg
    bag = bagit.make_bag(compendium_directory, processes = 6)

    if not compendium_out:
        compendium_out = f"{os.path.abspath(compendium_directory)}_bagit"
        os.makedirs(compendium_out, exist_ok=True)
    
    shutil.make_archive(compendium_directory, "zip", bag.path)
    shutil.copy(compendium_metadata_tmp, compendium_out)

    # Move compendium bagited
    compendium_bagit = f"{compendium_directory}.zip"
    compendium_bagit = os.path.join(compendium_out, compendium_bagit)
    
    shutil.move(compendium_bagit, compendium_bagit)

    return CompendiumPack(
        compendium_bagit, os.path.join(compendium_out, "metadata.json")
    )
