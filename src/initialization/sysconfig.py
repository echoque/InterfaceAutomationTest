#! /usr/bin/env python
#coding=utf-8

import configparser

def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    cfg.read(cfg_file)
    return cfg

sys_cfg = read_config(r'E:\光荣之路\测试开发\corweixindemo\corweixindemo\cfg\auto.cfg')


if __name__=="__main__":
    cfg=read_config("../../cfg/auto.cfg")
    print(cfg.get('contact_para','create_dep_url'))


