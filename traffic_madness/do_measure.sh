#!/bin/bash
# Run the simulation and change a variable
change='passives'
from=0
to=1
step=0.1
for i in $(seq $from $step $to)
do
    number=$i
    echo "Changing $change i is now $i of $to with step $step"
    sed -i "s/self.$change = [[:digit:]]\+\.[[:digit:]]/self.$change = $i/g" config.py
    python main.py
    echo "Run done"
done
