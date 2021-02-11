#!/bin/bash

counter=0
while [ $counter -eq "0" ]
do
	read -p "Would you like to build and run test container? [y/n]" build_container

	if [[ "$build_container" == 'y' ]]
	then 

		docker build -f Dockerfile-test -t plan_parser_test .
		docker run plan_parser_test 
		let counter++

	elif [[ "$build_container" == 'n' ]]
	then 

		let counter++

	else
		echo "Please enter valid option"

	fi
done

echo "Goodbye!"
