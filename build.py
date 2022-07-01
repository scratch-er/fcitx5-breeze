#!/usr/bin/env python3
import os
import json
import shutil

configfile = "build.json"

files = {}
variables = {}
tags = []
buildconfig =[]

def mkne(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

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
    destdir = os.path.join("build", dirname)
    mkne(destdir)
    for destfile, srcfile in files.items():
        destfile = os.path.join(destdir, destfile)
        if srcfile.endswith(".svg.in"):
            # 生成svg文件并转换为png
            tmpfile = os.path.join("tmp", os.path.basename(srcfile) + ".svg")
            cmd = "inkscape -o " + destfile + " " + tmpfile
            replace_variables(srcfile, tmpfile)
            os.system(cmd)
        elif srcfile.endswith(".in"):
            # 生成配置文件
            replace_variables(srcfile, destfile)
        elif srcfile.endswith(".svg"):
            # 转换为png
            cmd = "inkscape -o " + destfile + " " + srcfile
            os.system(cmd)
        else:
            # 简单复制
            shutil.copy(srcfile, destfile)

def build(level):
    if level == len(buildconfig):
        dirname = ""
        for tag in tags:
            dirname += tag + "-"
        dirname = dirname[:-1]
        print("Building theme "+dirname)
        write_file(dirname)
    else:
        conflist = buildconfig[level]
        for conf in conflist:
            conf_tag = conf.get("tag", "none")
            conf_files = conf.get("files", {})
            conf_vars = conf.get("variables", {})
            tags.append(conf_tag)
            files.update(conf_files)
            variables.update(conf_vars)
            build(level+1)
            tags.pop()
            for k in conf_files.keys():
                files.pop(k)
            for k in conf_vars.keys():
                variables.pop(k)

configfile = open(configfile, "rt")
buildconfig = json.load(configfile)
configfile.close()

mkne("tmp")
mkne("build")

build(0)

shutil.rmtree("tmp")
