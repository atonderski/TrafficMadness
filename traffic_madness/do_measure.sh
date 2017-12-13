#!/bin/bash
# Run the simulation and change a variable
change='aggressives'
from=0
to=1
step=0.1
for i in $(seq $from $step $to)
do
    number=$i
    echo "Changing $change i is now $i of $to with step $step"
    sed -i.bak "s/self.$change .*/self.$change = $i/g" config.py
    python main.py
    echo "Run done"
done

rm config.py.bak