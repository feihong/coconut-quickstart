import sys

# Build the coconut source.
import coconut.main
sys.argv = ['coconut', '--quiet', 'src', 'build']
coconut.main.main()

from invoke import Collection

# Import Python modules built by Coconut compiler.
sys.path.append('build')
import main, docs, web


namespace = Collection.from_module(main)
for mod in (docs, web):
    namespace.add_collection(mod)
