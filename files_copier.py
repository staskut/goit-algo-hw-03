import os
from pathlib import Path


def list_files(dir):
    items = []
    try:
        for it in (Path(dir).iterdir()):
            try:
                items.append(it)
            except PermissionError:
                print(f"Permission error when scanning src folder: {it}")
    except PermissionError:
        print(f"Permission error when scanning src folder: {dir}")
    if all(it.is_file() for it in items):
        return items
    else:
        subdirs = [it for it in items if it.is_dir()]
        items = [it for it in items if it not in subdirs]
        for subdir in subdirs:
            items.extend(list_files(subdir))
    return items


def copy_files(files, dst):
    if not Path(dst).exists():
        Path.mkdir(Path(dst))
    unique_extensions = set(f.suffix for f in files)
    for ext in unique_extensions:
        ext = ext[1:]
        if not Path(dst + "/" + ext).exists():
            Path.mkdir(Path(dst + "/" + ext))

    for file in files:
        ext = file.suffix[1:]
        status = os.system(f"cp {file} {dst}/{ext}/")
        if status != 0:
            print(f"Permission error when trying to copy file: {file}")


def scan_and_copy(src_dir, dst_dir="dist"):
    files = list_files(src_dir)
    copy_files(files, dst_dir)


if __name__ == "__main__":
    # testing
    test_src_folder = "./test_src"
    Path.mkdir(Path(test_src_folder))
    Path.mkdir(Path("./test_src/pics"))
    Path.mkdir(Path("./test_src/pics/photos"))
    Path.mkdir(Path("./test_src/pics/imgs"))
    Path.mkdir(Path("./test_src/audio"))
    Path.touch(Path("./test_src/pics/photos/photo.jpeg"))
    Path.touch(Path("./test_src/pics/imgs/img.gif"))
    Path.touch(Path("./test_src/pics/photo1.jpeg"))
    Path.touch(Path("./test_src/audio/file.wav"))

    Path.touch(Path("./test_src/audio/no_permissions.wav", ))
    Path("./test_src/audio/no_permissions.wav", ).chmod(0o000)
    Path.mkdir(Path("./test_src/no_permissions", ))
    Path.touch(Path("./test_src/no_permissions/no_permissions2.wav", ))

    Path("./test_src/no_permissions/no_permissions2.wav", ).chmod(0o000)
    Path("./test_src/no_permissions", ).chmod(0o000)

    test_dst_folder = "./test_dst"

    scan_and_copy(test_src_folder, test_dst_folder)
