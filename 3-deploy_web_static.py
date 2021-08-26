#!/usr/bin/python3
# Distributes an archive to web servers.
from fabric.api import env, put, run, local
from datetime import datetime
import os.path

env.hosts = ["34.139.228.214", "34.75.185.97"]



def do_pack():
    """ Packs the web_static folder. """
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

def do_deploy(archive_path):
    """ Deploys webstatic. """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        put(archive_path, "/tmp/{}".format(file))
        run("rm -rf /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file, name))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(name, name))
        run("rmdir /data/web_static/releases/{}/web_static".format(name))
        run("rm /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return (True)
    except Exception:
        return (False)

def deploy():
    """ Creates and distributes an archive to web servers. """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
