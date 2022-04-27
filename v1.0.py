# cfw
# 2022/4/27
import os


def get_root_dir():
    return os.path.dirname(os.path.realpath(__file__))
    # return r"Z:\Animation\BDRip\[VCB-Studio] 绯弹的亚里亚 [Ma10p_1080p]"


def get_file_name(path: str, ext: str):
    ext = "." + ext
    filename_list = []
    for f in os.scandir(path):
        if f.is_file():
            _, file_ext = os.path.splitext(f.path)
            if file_ext == ext:
                filename_list.append(f.name)
    return filename_list


def find_name_prefix(filename_list: list):
    s1 = min(filename_list)
    s2 = max(filename_list)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1


def find_name_suffix(filename_list: list):
    s1 = min(filename_list)[::-1]
    s2 = max(filename_list)[::-1]
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i][::-1]
    return s1[::-1]


def rename_proc(prefix: str, suffix: str, filename_list: list):
    rename_dict = {}
    ext = os.path.splitext(filename_list[0])[1]
    ass_name_list = get_file_name(get_root_dir(), "ass")
    ass_prefix = find_name_prefix(ass_name_list)
    ass_suffix = find_name_suffix(ass_name_list)
    for f in filename_list:
        f = f.replace(prefix, "").replace(suffix, "")
        for i in ass_name_list:
            i2 = i.replace(ass_prefix, "").replace(ass_suffix, "")
            if f in i2:
                ass_rename = prefix + f + suffix + ".ass"
                ass_rename = ass_rename.replace(ext, "")
                ass_path = os.path.join(get_root_dir(), i)
                ass_rename_path = os.path.join(get_root_dir(), ass_rename)
                if ass_path == ass_rename_path:
                    continue
                print(i + "   →   " + ass_rename)
                rename_dict[ass_path] = ass_rename_path
    return rename_dict


if __name__ == "__main__":
    video_name_list = get_file_name(get_root_dir(), "mkv")
    video_prefix = find_name_prefix(video_name_list)
    video_suffix = find_name_suffix(video_name_list)
    rename_dict = rename_proc(video_prefix, video_suffix, video_name_list)
    input("确定重命名吗？确定请按任意键，否请直接退出！")
    input("该操作不可撤销！")
    for old_path, new_path in rename_dict.items():
        os.rename(old_path, new_path)
