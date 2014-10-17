# Supporting materials for "WebSockets from the Wire Up"

Unfortunately, my two different example apps require two entirely different
stacks---one which has few dependencies and is easy to run on the command line,
and one which is easy to deploy behind nginx. The Python library support
for websockets continues to evolve very quickly.

## To reproduce websocket_simple.dump

	# activate Python 3 venv
	source bin/activate
	# install dependencies (there aren't many)
	pip install -r requirements.txt
	# start up the server
	python ws_server.py
	# start packet capture
	sudo tcpdump -i lo -s0 tcp port 8765 -w output.dump
	# start up the client and interact
	python ws_client.py
	# kill your tcpdump and server when you're done :)

## To set up SocketIO chat application

	# cd socketio
	source bin/activate
	# la la la wait for gevent to compile...
	pip install -r requirements.txt
	# start the server
	python chat_server.py
	# proxy behind nginx for production-like environment
