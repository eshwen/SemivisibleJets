#!/bin/bash
echo "== path == "
pwd
echo "== starting == "
ls -alrth
tar -xzf mg_image.tar.gz
echo "== done untaring == "
bin/mg5 SAMPLE.input
ls -alrth
echo "== done == "
