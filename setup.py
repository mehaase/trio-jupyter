#!/usr/bin/env python

import sys
from glob import glob
import os
import shutil

from setuptools import setup


setup_args = dict(
    name="trio-jupyter",
    version="0.1.0",
    description="Trio mode for Jupyter Lab/Notebook",
    long_description="Installs a kernelspec for Jupyter Lab/Notebook based on ipykernel with Trio mode enabled",
    packages=["trio_jupyter"],
    package_data={
        'ipykernel': ['resources/*.*'],
    },
    author='Mark E. Haase',
    author_email='mehaase@gmail.com',
    url='https://github.com/mehaase/trio-jupyter',
    license='BSD',
    python_requires='>=3.7',
    install_requires=[
        'ipykernel>=5.5.3',
    ],
    classifiers=[
        'Framework :: Trio',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)


if any(a.startswith(('bdist', 'install')) for a in sys.argv):
    sys.path.insert(0, here)
    from ipykernel.kernelspec import write_kernel_spec, make_ipkernel_cmd, KERNEL_NAME

    # When building a wheel, the executable specified in the kernelspec is simply 'python'.
    if any(a.startswith('bdist') for a in sys.argv):
        argv = make_ipkernel_cmd(executable='python')
    # When installing from source, the full `sys.executable` can be used.
    if any(a.startswith('install') for a in sys.argv):
        argv = make_ipkernel_cmd()
    dest = os.path.join(here, 'data_kernelspec')
    if os.path.exists(dest):
        shutil.rmtree(dest)
    write_kernel_spec(dest, overrides={'argv': argv})

    setup_args['data_files'] = [
        (
            pjoin('share', 'jupyter', 'kernels', KERNEL_NAME),
            glob(pjoin('data_kernelspec', '*')),
        )
    ]


if __name__ == '__main__':
    setup(**setup_args)
