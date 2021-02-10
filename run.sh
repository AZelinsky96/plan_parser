#!/bin/bash

build_and_run () {

	docker build -f Dockerfile -t flask_application .
	docker run --name flask_app -p 5001:5000 -d flask_application
    echo
    echo
    echo "Please navigate to localhost:5001 to view application!"
	read -p "Press any key to stop application: "
	docker rm $(sudo docker stop $(sudo docker ps -a -q --filter="name=flask_app"))
	echo "Container Stopped"
	echo "List of containers still running: "
	docker ps

}

counter=0
while [ $counter -eq "0" ]
do
	read -p "Would you like to build and run container? [y/n]" build_container

	if [[ "$build_container" == 'y' ]]
	then 

		build_and_run
		let counter++

	elif [[ "$build_container" == 'n' ]]
	then 

		let counter++

	else
		echo "Please enter valid option"

	fi
done

echo "Goodbye!"
