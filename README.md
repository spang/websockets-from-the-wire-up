# Supporting materials for "WebSockets from the Wire Up"

## To reproduce websocket_simple.dump

	# activate Python 3 venv
	source bin/activate
	# install dependencies (there aren't many)
	pip install -r requirements.txt
	# start up the server
	python ws_server.py
	# start packet capture
	sudo tcpdump -i lo -s0 tcp port 8765 -w output.dump
