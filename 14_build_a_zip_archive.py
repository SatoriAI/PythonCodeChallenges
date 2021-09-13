import os
import pathlib

from zipfile import ZipFile


def zip_all(search_dir, extensions, output_path):
    """Zips files from a given searching directory.
    This function considers only files with a specified
    extension. The folder structure is preserved.

    Args:
        search_dir (str): searching directory,
        extensions (list): extensions; files from
        the searching directory will be filtered by them,
        output_path (str): path to save the zipped folder.
    """
    with ZipFile(output_path, 'w') as zip_object:
        for folder, _, filenames in os.walk(search_dir):
            rel_path = os.path.relpath(folder, search_dir)
            for filename in filenames:
                if pathlib.Path(filename).suffix in extensions:
                    zip_object.write(
                        os.path.join(folder, filename),
                        os.path.join(rel_path, filename)
                    )


if __name__ == "__main__":
    zip_all(
        search_dir='files',
        extensions=['.txt'],
        output_path='files/files.zip'
    )
