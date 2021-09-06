#/usr/bin/env sh

# check every file
python maze.py
python reinforce.py

echo -e "Running Game maybe give incompatible indexer error because of same value of actions []"
python update.py 


