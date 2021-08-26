#!/usr/bin/python3
# Distributes an archive to web servers.
from fabric.api import env, put, run
from datetime import datetime
import os.path

env.hosts = ["34.139.228.214", "34.75.185.97"]


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
