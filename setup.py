import setuptools, pyRoomOSxAPI


with open('README.md', 'r') as file:
	long_description = file.read()

# with open('requirements.txt', 'r') as file:
# 	requirements = [c for c in file.read().split('\n') if c]

setuptools.setup(
    name='pyRoomOSxAPI',
    version=pyRoomOSxAPI.__version__,
    author='Fedor Batonogov',
    author_email='batonogov@icloud.com',
    description='Simple implementation RoomOS xAPI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/batonogov/pyRoomOSxAPI',
    packages=setuptools.find_packages(),
    # install_requires=requirements,
    classifiers=[
      "Programming Language :: Python :: 3.10",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
