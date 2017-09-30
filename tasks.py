import subprocess
subprocess.call('coconut --quiet src build', shell=True)


from invoke import Collection
import sys
sys.path.append('build')
import main, docs, web


namespace = Collection.from_module(main)
for mod in (docs, web):
    namespace.add_collection(mod)
