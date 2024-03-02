# A Puppet manifest that installs and configures an Nginx server to:
# 	listen on port 80.
# 	returns a page that contains the string "Hello World!",
#		when querying Nginx at its root /, using Curl,
#		with a Get request.
# 	The redirection must be a "301 Moved Permanently".
