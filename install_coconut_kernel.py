import sys
import subprocess
import os.path

from coconut.constants import icoconut_dir

cmd = [
    'jupyter', 'kernelspec', 'install',
    os.path.join(icoconut_dir, 'coconut3'),
    '--sys-prefix', sys.prefix,
    '--replace',
]

subprocess.call(cmd)
