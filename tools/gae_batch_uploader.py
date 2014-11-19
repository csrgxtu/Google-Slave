#!/usr/bin/env python
# coding = utf8
# Author: Archer Reilly
# Date: 19/Nov/2014
# File: gae_batch_uploader.py
# Desc: batch upload my gae slave application to the Google
# App Engine. can handle multiple email accounts
#
# Produced By CSRGXTU
import os

# loadGaeApps
# load gae app list from data file
#
# @param inputFile
# @return lst 2d
def loadGaeApps(inputFile):
  apps = []
  with open(inputFile, 'r') as myFile:
    for line in myFile:
      apps.append(line.rstrip().split(','))

  return apps

# changeAppId
# change app id in app.yaml
#
# @param yaml file
# @param gaeId
# @return none
def changeAppId(inputFile, gaeId):
  cmd = "sed -i 's/application: .*/application: " + gaeId + "/g' " + inputFile
  os.system(cmd)
#changeAppId('/home/archer/Documents/Google-Slave/src/GAE-Slave/app.yaml', 'test')

# appCfg
# invoke app config to upload
#
# @param 

# main
def main():
  app_list_file = '/home/archer/Documents/Google-Slave/tools/gae_app_list.csv'
  app_yaml_file = '/home/archer/Documents/Google-Slave/src/GAE-Slave/app.yaml'
  application_dir = '/home/archer/Documents/Google-Slave/src/GAE-Slave/'

  app_lists = loadGaeApps(app_list_file)
  #print app_lists
  for lst in app_lists:
    for i in range(len(lst) - 1):
      changeAppId(app_yaml_file, lst[i + 1])
      if i == 0:
        cmd = "appcfg.py --email=" + lst[0] + " --no_cookies update " +\
        application_dir
        #print cmd
        os.system(cmd)
      else:
        cmd = "appcfg.py update " + application_dir
        #print cmd
        os.system(cmd)

if __name__ == '__main__':
  main()
