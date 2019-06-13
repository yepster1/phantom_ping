#!/bin/sh
python3 videoWriter.py &
python3 videoDeleter.py &
python3 videoDisplayer.py &
