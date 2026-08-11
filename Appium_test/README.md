# Appium 自动化测试框架

## 📖 项目简介

本项目是一套基于 **Python + Appium + Pytest** 的移动端自动化测试框架，采用 **Page Object（页面对象）设计模式**，将页面元素定位、业务逻辑与测试用例解耦，提升代码的可维护性和复用性。

支持多设备配置管理、测试数据参数化、失败自动截图、日志追踪以及 HTML 测试报告生成。

---

## 📁 目录结构

```
testProject/
├── common/                 # 基础封装层
│   ├── __init__.py
│   ├── base_page.py        # 页面对象基类，封装 find / click / send_keys 等通用操作
│   ├── driver_factory.py   # 驱动工厂，负责 WebDriver 的初始化与销毁
│   └── build_data.py       # 测试数据构建工具
│
├── config/                 # 配置层
│   ├── __init__.py
│   └── caps.yml            # Appium Desired Capabilities 配置（设备/平台/包名等）
│
├── datas/                  # 测试数据层
│   └── test_login.json     # 登录模块测试数据（JSON 参数化）
│
├── images/                 # 资源层
│   └── screenshot/         # 运行截图存放目录（按时间戳命名）
│
├── logs/                   # 日志层
│   └── appium_test.log     # 测试运行日志，记录步骤与异常堆栈
│
├── pages/                  # 页面对象层（Page Object 模式）
│   ├── __init__.py
│   └── netease_pages/      # 网易模块页面对象封装
│
├── reports/                # 测试报告层（HTML 报告输出目录）
│
├── test_cases/             # 测试用例层
│   ├── __init__.py
│   └── test_login.py       # 登录业务流程测试用例
│
├── tools/                  # 工具脚本
│   └── main.py             # 测试执行入口
│
├── .venv/                  # Python 虚拟环境
├── pytest.ini              # Pytest 框架配置
├── requirements.txt        # 项目依赖清单
└── test.py                 # 备用执行脚本
```

---

## 🗂️ 一级目录说明

| 目录/文件 | 说明 |
|---|---|
| `common/` | 框架底层封装，包括页面基类、驱动管理、数据工具等公共组件 |
| `config/` | 集中管理 Appium 启动参数，支持多设备/多环境切换 |
| `datas/` | 存放 JSON / YAML 等格式的测试数据，实现数据与脚本分离 |
| `images/` | 存放测试过程中产生的截图，便于失败排查与报告展示 |
| `logs/` | 测试运行日志，记录每一步操作及异常信息 |
| `pages/` | 按模块划分的页面对象，每个页面封装自身的元素与操作 |
| `reports/` | 测试完成后生成的 HTML 报告输出位置 |
| `test_cases/` | 测试用例编写目录，调用 pages 层完成业务验证 |
| `tools/` | 辅助工具与执行入口脚本 |
| `pytest.ini` | Pytest 全局配置（默认参数、日志格式、用例发现规则等） |
| `requirements.txt` | Python 第三方依赖列表 |
| `main.py` | 一键启动测试的入口文件 |

---

## 🚀 快速启动

### 1. 环境准备

确保本机已安装：
- **Python 3.8+**
- **Appium Server**（本地或远程）
- **Android SDK / Xcode**（对应目标移动平台）

### 2. 安装依赖

建议在虚拟环境中安装：

```bash
# 进入项目根目录
cd testProject

# （可选）创建并激活虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 安装项目依赖
pip install -r requirements.txt
```

### 3. 配置设备参数

编辑 `config/caps.yml`，填入目标设备的 Desired Capabilities（platformName、deviceName、appPackage、appActivity 等）。

### 4. 启动 Appium Server

```bash
appium
```

确保 Server 默认监听 `http://127.0.0.1:4723`，或在 `caps.yml` 中指定自定义地址。

### 5. 运行测试

```bash
# 方式一：通过入口脚本运行
python main.py

# 方式二：直接使用 pytest
pytest

# 方式三：运行指定用例
pytest test_cases/ntest_login.py -v
```

### 6. 查看报告

测试完成后，HTML 报告将生成在 `reports/` 目录下，浏览器打开即可查看详细结果。

---

## 📌 注意事项

- 每次运行前请确认 **Appium Server 已启动** 且 **设备已连接**（`adb devices` 可见）。
- 截图与日志会在每次运行后追加，建议定期清理 `images/screenshot/` 和 `logs/` 目录。
- 新增页面对象请放在 `pages/` 对应模块目录下，保持 PO 模式结构清晰。
- 新增测试用例请放在 `test_cases/` 目录，文件名以 `test_` 开头以被 Pytest 自动发现。

---

## 📄 License

Internal Use Only.
