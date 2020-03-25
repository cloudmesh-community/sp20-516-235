from cloudmesh.common.util import readfile
import json
import yaml
from cloudmesh.common.debug import VERBOSE
google = readfile("/Users/yasirjasim/cm/cloudmesh-google/cloudmesh/google.json")
print(google)

d = json.loads(google)
print(d)

c = yaml.dump(d)
print("yaml")
print(c)
VERBOSE(c)
