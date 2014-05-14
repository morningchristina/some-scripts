#!/bin/bash
cat urlcity.txt |while read url city
do
    curl $url >>htmls.html
    echo "this is city"$city >>htmls.html
    echo "the website is"$url >>htmls.html    
done


