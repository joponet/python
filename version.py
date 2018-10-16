import pathlib

def get_version():
	version=0
	file_path = pathlib.Path("version.dat")
	if file_path.exists():
		file = file_path.open("r")
		version = int(file.readline())
		file.close()
	return version

def inc_version():
	version = get_version() + 1
	file_path = pathlib.Path("version.dat")
	file = file_path.open ("w")
	file.write (str(version))
	file.close()
	return version

version = inc_version()
print(str(version))
