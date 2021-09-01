#!/bin/bash

if [ -d /var/python3 ]; then

	chmod -R 0775 /var/python3

	#echo ""
	#echo "For dynamic inventory test:"
	#echo "  With python"
	#echo "  	/etc/ansible/inventory/all.py --list"
	#echo "  	/etc/ansible/inventory/all.py --host <hostname>"
	#echo ""
	#echo "  With ansible"
	#echo "  	ansible-inventory --list"
	#echo "  	ansible-inventory --host <hostname>"
	#echo "  	ansible all -m ping"
	#echo ""

fi