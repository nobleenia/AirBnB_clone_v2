#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive
from the contents of the web_static folder of the AirBnB Clone repo,
using the function do_pack
"""
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Archives all files in the folder web_static
    Stores archived files in the folder versions
    Return the archive path if the archive has been correctly generated
    Otherwise: return None
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    pack_time = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        pack_time.year,
        pack_time.month,
        pack_time.day,
        pack_time.hour,
        pack_time.minute,
        pack_time.second
    )
    try:
        print("Packing web_static to {}".format(archive))
        local("tar -cvzf {} web_static".format(archive))
        size = os.stat(archive).st_size
        print("web_static packed: {} -> {} Bytes".format(archive, size))
    except Exception:
        return None
    return archive
