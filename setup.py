#!/usr/bin/env python
# This is loosely adapted from ipykernel's setup.py

from glob import glob
import os
import shutil
import sys

from setuptools import setup


DISPLAY_NAME = "Python 3 Trio"
KERNEL_NAME = "python3-trio"


setup_args = dict(
    name="trio-jupyter",
    version="0.1.1",
    description="Trio mode for Jupyter Lab/Notebook",
    long_description="Installs a kernelspec for Jupyter Lab/Notebook based on ipykernel with Trio mode enabled",
    packages=["trio_jupyter"],
    package_data={
        "trio_jupyter": ["resources/*.*"],
    },
    author="Mark E. Haase",
    author_email="mehaase@gmail.com",
    url="https://github.com/mehaase/trio-jupyter",
    license="BSD",
    python_requires=">=3.7",
    install_requires=[
        "ipykernel>=5.5.0",
        "trio>=0.18.0",
    ],
    classifiers=[
        "Framework :: Trio",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)


if any(arg.startswith(("bdist", "install")) for arg in sys.argv):
    here = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, here)
    from ipykernel.kernelspec import write_kernel_spec, make_ipkernel_cmd
    extra_arguments = ["--IPKernelApp.trio_loop=True"]

    # When building a wheel, the executable specified in the kernelspec is simply "python".
    if any(arg.startswith("bdist") for arg in sys.argv):
        argv = make_ipkernel_cmd(executable="python", extra_arguments=extra_arguments)
    # When installing from source, the full `sys.executable` can be used.
    if any(arg.startswith("install") for arg in sys.argv):
        argv = make_ipkernel_cmd(extra_arguments=extra_arguments)
    dest = os.path.join(here, "data_kernelspec")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    write_kernel_spec(dest, overrides={"argv": argv, "display_name": DISPLAY_NAME})
    resource_path = os.path.join(os.path.dirname(__file__), "trio_jupyter", "resources")
    shutil.copytree(resource_path, dest, dirs_exist_ok=True)

    setup_args["data_files"] = [
        (
            os.path.join("share", "jupyter", "kernels", KERNEL_NAME),
            glob(os.path.join("data_kernelspec", "*")),
        )
    ]


if __name__ == "__main__":
    setup(**setup_args)
