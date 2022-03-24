#!/usr/bin/python3
""" Defines a function do_pack that generates a .tgz file """
import os.path
from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a '.tgz' archive from the contents of the web_static folder"""
    dt = datetime.now()
    date_time = "{}{}{}{}{}{}".format(dt.year, dt.month, dt.day,
                                      dt.hour, dt.minute, dt.second)
    path = "versions/web_static_{}.tgz".format(date_time)

    if os.path.isdir("versions") is False:
        local("mkdir -p versions")

    archive = 'tar -cvzf {} web_static'.format(path)
    if local(archive).failed is True:
        return None

    return path
