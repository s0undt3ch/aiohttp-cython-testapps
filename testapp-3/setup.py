import os
import glob
import shutil
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from distutils.command.clean import clean
from distutils.command.build_py import build_py

SETUP_DIRNAME = os.path.dirname(__file__)
FULL_SETUP_DIRNAME = os.path.abspath(SETUP_DIRNAME)


class Clean(clean):
    def run(self):
        clean.run(self)
        # Let's clean compiled *.py[c,o] *.c *.so
        for subdir in ('testapp3',):
            root = os.path.join(os.path.dirname(__file__), subdir)
            for dirname, dirs, _ in os.walk(root):
                for to_remove_filename in glob.glob('{0}/*.py[ocx]'.format(dirname)):
                    os.remove(to_remove_filename)
                for to_remove_filename in glob.glob('{0}/*.c'.format(dirname)):
                    os.remove(to_remove_filename)
                for to_remove_filename in glob.glob('{0}/*.so'.format(dirname)):
                    os.remove(to_remove_filename)
                for dir_ in dirs:
                    if dir_ == '__pycache__':
                        shutil.rmtree(os.path.join(dirname, dir_))


class BuildPy(build_py):

    def find_package_modules(self, package, package_dir):
        modules = build_py.find_package_modules(self, package, package_dir)
        for package, module, filename in modules:
            if module not in ('__init__',):
                # We only want __init__ python files
                # All others will be built as extensions
                continue
            yield package, module, filename


def find_ext_packages():
    ret = []
    for root, _, files in os.walk(os.path.join(FULL_SETUP_DIRNAME, 'testapp3')):
        commonprefix = os.path.commonprefix([FULL_SETUP_DIRNAME, root])
        for filename in files:
            if not filename.endswith(('.py', '.c')):
                continue
            if filename in ('__init__.py',):
                continue
            full = os.path.join(root, filename)
            relpath = os.path.join(root, filename).split(commonprefix)[-1][1:]
            module = os.path.splitext(relpath)[0].replace(os.sep, '.')
            ret.append(Extension(module, [full]))
    return ret

setup(
    name='testapp3',
    version='0.0',
    ext_modules=cythonize(find_ext_packages()),
    packages=find_packages(),
    zip_safe=False,
    cmdclass={
        'clean': Clean,
        'build_py': BuildPy,
    }
)
