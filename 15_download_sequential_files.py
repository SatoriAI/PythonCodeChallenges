import os
import re
import requests


def generate_sequence(url_suffix):
    """Generates a sequence of consecutive strings based
    on the first one.
    For example a string "text1.txt" will yield "text1.txt",
    "text2.txt" etc.

    Args:
        url_suffix (str): string containing filename,
        it's sequence number or index and it's extension.

    Yields:
        str: a sequence of naturally consecutive strings.
    """
    groups = re.search(r'([A-Za-z]+)([0-9]+)\.([a-z]+)', url_suffix)
    filename = groups.group(1)
    number, length = int(groups.group(2)), len(groups.group(2))
    extension = groups.group(3)
    url_placeholder = filename + '{}' + '.' + extension
    i = 0
    while True:
        yield_number = format(number+i, '0'+str(length)+'d')
        i += 1
        yield url_placeholder.format(yield_number)


def download_files(first_url, output_path):
    """Downloads sequential files basing on the url to the
    first file. Then saves the files in the specified folder.
    The downloading process stops after failing 5 times in
    a row.

    Args:
        first_url (str): The url to the first file,
        output_path (str): The path to the directory in which to save
        the downloaded files. Creates the directory
        if it does not exist).
    """
    if '/' not in first_url:
        return 'Wrong URL.'
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    url_base, url_suffix = os.path.split(first_url)
    url_base = url_base + '/{}'
    failed_downloads, successful_downloads = 0, 0
    for seq in generate_sequence(url_suffix):
        url = url_base.format(seq)
        file = requests.get(url, allow_redirects=True)
        if not file:
            failed_downloads += 1
            print(f'failed to download:\t{seq}')
        else:
            successful_downloads += 1
            open(os.path.join(output_path, seq), 'wb').write(file.content)
            print(f'successfully downloaded:\t{seq}')
        if failed_downloads == 5:
            break
    print(f'Downloading finished. {successful_downloads} file(s) saved in {output_path}.')


if __name__ == "__main__":
    download_files(
        first_url='http://699340.youcanlearnit.net/image001.jpg',
        output_path='files/downloads'
    )
