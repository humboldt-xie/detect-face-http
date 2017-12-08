#!/bin/bash
#===============================================================================
#
#          FILE:  test.sh
# 
#         USAGE:  ./test.sh 
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
#       CREATED:  2017/12/08 19时48分59秒 CST
#      REVISION:  ---
#===============================================================================

curl -v  -F file=@data/Anthony_Hopkins_0001.jpg http://127.0.0.1:5000/upload
curl -v  -F file=@data/Anthony_Hopkins_0002.jpg http://127.0.0.1:5000/uploadStream
