@echo off
chcp 65001 > nul
if not exist "venv" (
    echo 未检测到虚拟环境，正在创建venv...
    python -m venv venv
    echo 虚拟环境创建完成，正在安装依赖包...
    call venv\Scripts\activate && pip install -r requirements.txt
    echo 依赖包安装完成！
)

call venv\Scripts\activate
echo.
echo 请选择运行模式：
echo 0: 返回一次消息
echo 1: 定时返回消息
set /p choice=请输入选项编号（0或1）并回车：

if "%choice%"=="0" (
    echo 运行单次消息模式...
    python main.py --once
    echo 消息已发送完毕！
) else if "%choice%"=="1" (
    echo 运行定时消息模式...
    python main.py
) else (
    echo 无效的选项，请重新运行脚本并选择0或1。
)

::保留窗口
pause