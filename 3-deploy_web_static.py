#!/usr/bin/python3
""" Creates distributes and deloys an archive file """
import os.path
from fabric.api import *
from datetime import datetime


env.hosts = ["34.204.166.82", "44.200.178.195"]
env.user = "ubuntu"

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

def deploy():
    """ Creates and archive, and deploys it to remote hosts """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
