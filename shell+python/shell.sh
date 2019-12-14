#!/bin/bash
while true
do
	input="pid.txt"
	while read -r line #le o arquivo
	do
		pid = $line
	done < "$input"  #arquivo input como fonte do texto lido
	A = `ps -p $pid` #escreve as informção sobre o processo com a pid lida em uma variavel
	if [ -z "$A" ]
		then
			echo "1: It is dead"
		else
			echo "1: It is alive"
	fi
	sleep 0.1
done