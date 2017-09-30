import sys

# Build the coconut source.
import coconut.main
sys.argv = ['coconut', '--quiet', 'src', 'build']
coconut.main.main()

from invoke import Collection
sys.path.append('build')
# Import Python modules built by Coconut compiler.
import main, docs, web


namespace = Collection.from_module(main)
for mod in (docs, web):
    namespace.add_collection(mod)
