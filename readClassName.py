#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def classNameReader(path):
    targetList = []
    f = open(path, "r")
    for line in f.readlines():
        line = line[:-1]
        targetList.append(line)
    f.close()

    return targetList
