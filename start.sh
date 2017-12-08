#!/bin/bash
#===============================================================================
#
#          FILE:  start.sh
# 
#         USAGE:  ./start.sh 
# 
#   DESCRIPTION:  
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  xiehongbao (), @.com
#       COMPANY:  
#       VERSION:  1.0
#       CREATED:  2017/12/08 19时46分19秒 CST
#      REVISION:  ---
#===============================================================================

export FLASK_APP=detect_face_http.py
python -m flask run 
