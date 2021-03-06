"""
CloudLab profile for Cicada
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# CONSTANTS
IMAGE = "urn:publicid:IDN+wisc.cloudlab.us+image+cops-PG0:copycat-cicada-node-0"
HW_TYPE = "c220g5"

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Add a raw PC to the request.
node = request.RawPC("node")
node.disk_image = IMAGE
node.hardware_type = HW_TYPE

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/setup.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
