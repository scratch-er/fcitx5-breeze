#!/usr/bin/env python3
import os
import json
import shutil

configfile = "build.json"

files = {}
variables = {}
tags = []
buildconfig =[]

# 从源文件中替换掉变量的值并写入目标文件
def replace_variables(srcfile, destfile):
    srcfile = open(srcfile, "rt")
    destfile = open(destfile, "wt")
    content = srcfile.read()
    for k, v in variables.items():
        content = content.replace("${}$".format(k), v)
    destfile.write(content)
    srcfile.close()
    destfile.close()


def write_file(dirname):
    for srcfile, destfile in files.items():
        destfile = os.path.join("build", dirname, destfile)
        if srcfile.endswith(".svg.in"):
            tmpfile = os.path.join("tmp", os.path.basename(srcfile) + ".svg")
            cmd = "inkscape -o " + destfile + tmpfile
            replace_variables(srcfile, tmpfile)
            os.system(cmd)
        elif srcfile.endswith(".in"):
            replace_variables(srcfile, destfile)
        else:
            shutil.copy(srcfile, destfile)

def build(level):
    if level == len(buildconfig):
        dirname = ""
        for tag in tags:
            dirname += tag + "-"
        dirname = dirname[:-1]
        write_file(dirname)
    else:
        conf = buildconfig[level]
        tags.append(conf["tag"])
        files.update(conf["files"])
        variables.update(conf["variables"])
        build(level+1)
        tags.pop()
        for k in conf["files"].keys():
            files.pop(k)
        for k in cong["variables"].keys():
            variables.pop(k)

configfile = open(configfile, "rt")
buildconfig = json.loads(configfile)
configfile.close()
build(0)
shutil.rmtree("tmp")
