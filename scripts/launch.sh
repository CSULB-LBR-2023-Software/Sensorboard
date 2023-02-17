name=../data/rawData
if [[ -e $name.csv || -L $name.csv ]] ; then
    i=1
    while [[ -e $name-$i.csv || -L $name-$i.csv ]] ; do
        let i++
    done
    name=$name-$i
fi

python3 ../sensors.py | python3 ../logger.py "" "$name".csv "0.5"
