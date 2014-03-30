#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import local, task, env, hosts

env.use_ssh_config = True


def test():
    local("make test")


def push():
    local("git push origin master")
    local("git push pro master")


@hosts(['kd'])
@task
def deploy():
    test()
    push()
