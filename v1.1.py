# cfw
# 2022/4/28

import os


def get_root_dir():
    return r"Z:\Animation\BDRip\[VCB-Studio] 绯弹的亚里亚 [Ma10p_1080p]"
    # return os.path.dirname(os.path.realpath(__file__))


def get_filename_list(path: str, ext: str):
    filename_list = []
    for f in os.scandir(path):
        if f.is_file():
            if os.path.splitext(f.path)[1] == ext:
                filename_list.append(f.name)
    return filename_list


def rename_proc(video_list: list, ass_list: list):
    print("工作路径：", get_root_dir())
    print("开始检测...")
    rename_dict = {}
    s1 = sorted(video_list)
    s2 = sorted(ass_list)
    s1len = len(s1)
    s2len = len(s2)
    if s1len == s2len:
        for i in range(s1len):
            dst_name = os.path.splitext(s1[i])[0] + ".ass"
            src_path = os.path.join(get_root_dir(), s2[i])
            dst_path = os.path.join(get_root_dir(), dst_name)
            rename_dict[src_path] = dst_path
            print(s2[i] + "  →  " + dst_name)
    elif s1len * 2 == s2len:
        print("检测到字幕文件数量为视频文件数量的2倍，按照简繁字幕处理。")
        for i in range(s2len):
            ext_list = s2[i].split(".")
            if len(ext_list) >= 2:
                ext = ext_list[-2]
                dst_name = os.path.splitext(s1[i // 2])[0] + ext + ".ass"
                src_path = os.path.join(get_root_dir(), s2[i])
                dst_path = os.path.join(get_root_dir(), dst_name)
                rename_dict[src_path] = dst_path
                print(s2[i] + "  →  " + dst_name)
            else:
                print("简繁字幕识别错误，仍可重命名识别正确的字幕文件。")
    else:
        print("视频数量与字幕文件数量不一致！请重新检查！")
        return
    return rename_dict


def main():
    ext = input("请输入视频文件的后缀名(不包含“.”,例如:mkv):")
    s1 = get_filename_list(get_root_dir(), "." + ext)
    s2 = get_filename_list(get_root_dir(), ".ass")
    if len(s1) == 0:
        print("没有检测到视频文件！")
        return
    elif len(s2) == 0:
        print("没有检测到字幕文件！")
        return
    rename_dict = rename_proc(s1, s2)
    if not rename_dict:
        return
    input("按下任意键开始重命名字幕文件！退出请直接关闭。")
    input("注意：该操作不可撤销！")
    for src, dst in rename_dict.items():
        if src != dst:
            print("\n" + src)
            print("      ↓      ")
            print(dst + "\n")
            os.rename(src, dst)
        else:
            print(src + "  →  目标无需重命名")
    input("处理完成！")


if __name__ == "__main__":
    main()
