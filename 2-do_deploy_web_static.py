#!/usr/bin/python3
""" Defines a function that deploys an archive file to web servers """
import os.path
from fabric.api import *


env.hosts = ["34.204.166.82", "44.200.178.195"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys an archive file to a remote host

    Args:
        archive_path: Path to the archive file to be deployed
    """
    if os.path.isfile(archive_path) is False:
        return False

    archive_file = archive_path.split("/")[-1]
    name = archive_file.split(".")[0]

    try:
        put(archive_path, "/tmp/{}".format(archive_file))
        run("mkdir -p /data/web_static/releases/{}/".
            format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_file, name))
        run("rm /tmp/{}".format(archive_file))
        run("mv /data/web_static/releases/{}/web_static/*"
            " /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name))

        return True

    except ValueError:
        return False
