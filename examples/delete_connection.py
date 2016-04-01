"""
Delete a connection by name
"""

import NetworkManager
import sys

# Find the connection
name = sys.argv[1]
connections = NetworkManager.Settings.ListConnections()
connections = dict([(x.GetSettings()['connection']['id'], x) for x in connections])
conn = connections[name]

# And delete
success = conn.Delete()
