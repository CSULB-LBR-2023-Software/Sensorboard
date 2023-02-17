name=/home/pi/Documents/Sensorboard/data/Data
if [[ -e $name.csv || -L $name.csv ]] ; then
    i=1
    while [[ -e $name-$i.csv || -L $name-$i.csv ]] ; do
        let i++
    done
    name=$name-$i
fi
name=$name-$(date +'%m-%d-%Y-%H_%M_%S')

python3 /home/pi/Documents/Sensorboard/sensors.py | python3 /home/pi/Documents/Sensorboard/logger.py "-d" "$name".csv "0.5"
