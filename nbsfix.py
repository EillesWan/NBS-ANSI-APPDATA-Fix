COPYRIGNT = """
Copyright © 2026 金羿Eilles

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

print("本脚本依照以下开源协议发布，请阅读后按下回车键表示同意、同时按下 `Ctrl` 和 `C` 键表示不同意并退出本脚本。")
print("The Script is Licensed under the Following Open Source License. Press `Enter` to Agree, `Ctrl+C` to Cancel and Quit.")
input(COPYRIGNT)
print("\033[2J\033[H", end="", flush=True)

from os import environ, getlogin
from pathlib import Path


def main():
    ori_roaming_path = Path(
        environ.get("APPDATA", "C:\\Users\\{}\\AppData\\Roaming".format(getlogin()))
    ).absolute()


    print("已获取漫游目录于 | Having Get %APPDATA% Path at:", ori_roaming_path)

    ansi_roeaming_path = Path(
        str(ori_roaming_path)
        .encode(
            "utf-8",
        )
        .decode("ansi", "ignore")
    )

    print("计算得错误位置为 | Caculated Error ANSI Path at:", ansi_roeaming_path)

    if ori_roaming_path == ansi_roeaming_path:
        print("!!! 你无需进行此修复 | Your %APPDATA% Path is OK !!!")
        print('毕竟你的用户名很西方 | You Dont Need to "Fix" Your %APPDATA% Path')
        return 0
    if not (opth := (ori_roaming_path / "Minecraft_Note_Block_Studio").resolve()).exists():
        print("!!! 请先运行一遍 NBS | You Might Never Run NBS Before !!!")
        print("如果你没有运行过 NBS，那是怎么知道需要修复路径问题的？")
        print(
            "Please Run NBS at Least Once Before You Want to Fix Your %APPDATA% Path Problem."
        )
        return 0


    ansi_roeaming_path.mkdir(parents=True, exist_ok=True)

    print("已创建所需的上级目录 | Created Error ANSI Parent Path")

    (epth := ansi_roeaming_path / "Minecraft_Note_Block_Studio").symlink_to(
        opth, target_is_directory=True
    )

    if opth.exists() and epth.exists():
        print("已创建符号链接 | Created Symlink of `{}` to `{}`".format(opth, epth))
        return 1
    else:
        print("无法创建符号链接，请向作者反馈此问题，并期待无法取得解决方案")
        print("Failed to Create Symlink, Please Report This issue")
        return -1


if __name__ == "__main__":
    main()
    input("完成，按回车键退出 | All Done, Press `Enter` to Exit")

