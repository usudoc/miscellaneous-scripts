import os
import zipfile


def unzip(path_root):
    # subsフォルダー内のフォルダーの名前リストを取得
    folders = os.listdir(path_root)
    print(folders)

    # 各フォルダ内のファイル名を取得
    files = [os.listdir(os.path.join(path_root, f)) for f in folders]
    print(files)

    # zipファイルのpathリスト
    print('zipファイルのpathリスト')
    paths_zip = [os.path.join(path_root, folders[i], files[i][0]).replace('\\', '/') for i in range(len(folders))]
    print(len(paths_zip))
    print(paths_zip)

    # zipファイルの解凍先のpath('./subs/各フォルダ/')
    print('zipファイルの解凍先のpath')
    paths_unzip = [os.path.join(path_root, folders[i]) for i in range(len(folders))]
    print(len(paths_unzip))
    print(paths_unzip)

    # pathの末尾が'.zip'であるもののリストを取得
    print('pathの末尾が.zipであるもの')
    paths_zip_only = [_path for _, _path in enumerate(paths_zip) if _path.endswith('.zip')]
    print(len(paths_zip_only))
    print(paths_zip_only)

    # pathの末尾が'.zip'であるもののインデックスのリストを取得
    print('pathの末尾が.zipであるもののインデックス')
    paths_zip_only_idx = [idx for idx, _path in enumerate(paths_zip) if _path.endswith('.zip')]
    print(len(paths_zip_only_idx))
    print(paths_zip_only_idx)

    # pathの末尾が'.zip'でないもののリストを取得
    print('pathの末尾が.zipでないもの')
    paths_zip_not = [_path for _, _path in enumerate(paths_zip) if not(_path.endswith('.zip'))]
    print(len(paths_zip_not))
    print(paths_zip_not)

    # rootディレクトリに解凍
    for i, path_zip in enumerate(paths_zip_only):
        with zipfile.ZipFile(path_zip) as zf:
            zf.extractall(paths_unzip[paths_zip_only_idx[i]])


if __name__ == '__main__':
    path = './subs/'
    unzip(path_root=path)
