# WeFinance - 智能金融平台

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个功能完整的智能金融服务平台，集成P2P借贷、智能投顾、财富管理等多项金融科技功能

</div>

---

## 📖 项目介绍

WeFinance是一个基于Django开发的现代化金融科技平台，旨在为用户提供一站式的财富管理解决方案。平台整合了P2P借贷、智能投资、财富规划、投资社区等多个核心业务模块，通过AI算法为用户提供个性化的投资建议和理财方案。

### ✨ 核心功能

#### 📊 投资理财
- **P2P借贷投资**: 多样化的借贷产品，年化收益8%-15%
- **智能投顾**: 基于AI算法的个性化投资组合推荐
- **财富计划**: 目标导向的理财计划制定与执行
- **收益追踪**: 实时收益计算与历史数据分析

#### 💰 借款服务
- **信用贷款**: 无抵押快速审批，最高50万额度
- **车辆抵押**: 汽车抵押贷款，额度灵活
- **房产抵押**: 房产抵押大额贷款
- **智能评估**: 自动信用评分与额度核定

#### 👤 用户中心
- **个人仪表盘**: 资产概览、收益统计、投资分析
- **账单管理**: 完整的资金流水记录与统计
- **银行卡管理**: 安全的银行卡绑定与管理
- **实名认证**: 身份证OCR识别与人工审核

#### 💬 社区互动
- **投资社区**: 用户交流分享投资心得
- **新闻资讯**: 实时财经新闻与市场动态
- **专家问答**: 专业理财顾问在线解答

#### 🎯 客服系统
- **实时客服**: 基于WebSocket的在线客服聊天
- **会话管理**: 客服人员统一管理待处理会话
- **消息记录**: 完整的客服对话历史

---

## 🏗️ 技术架构

### 后端技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Python | 3.12 | 核心编程语言 |
| Django | 5.2.6 | Web框架 |
| SQLite3 | - | 默认数据库（开发/演示环境） |
| Daphne | 4.0 | ASGI服务器（支持WebSocket） |
| Channels | 4.0 | WebSocket实时通信 |
| Celery | 5.3 | 异步任务处理 |

### 前端技术栈

| 技术 | 版本 | 说明 |
|------|------|------|
| Bootstrap | 5.3 | UI框架 |
| jQuery | 3.6 | JavaScript库 |
| Chart.js | 4.4 | 数据可视化 |
| Font Awesome | 6.4 | 图标库 |
| CKEditor | 5.x | 富文本编辑器 |

### 核心功能模块

```
WeFinance/
├── accounts/          # 用户认证与账户管理
├── products/          # 金融产品管理
├── investments/       # 投资交易处理
├── borrow/           # 借款业务逻辑
├── roboadvisor/      # AI智能投顾引擎
├── wealth_plan/      # 财富计划管理
├── user_center/      # 用户中心（仪表盘、账单等）
├── community/        # 社区互动
├── news/             # 新闻资讯
├── admin_panel/      # 管理后台
└── pages/            # 静态页面
```

### 数据库设计

- **用户系统**: User, UserProfile, BankCard, LoginLog
- **产品系统**: LoanProduct, InvestmentStrategy
- **交易系统**: Investment, LoanApplication, RepaymentPlan
- **账单系统**: BillRecord, EarningsRecord, TransferOrder
- **社区系统**: Topic, Reply, UserMessage

### 安全特性

- ✅ HTTPS加密传输（生产环境）
- ✅ CSRF防护
- ✅ XSS过滤
- ✅ SQL注入防护
- ✅ 密码加密存储（PBKDF2）
- ✅ 实名认证系统
- ✅ 二次验证机制

> ⚠️ **安全测试演示**: 项目包含一个SQL注入漏洞演示接口 `/auth/api/vulnerable/search/`，仅用于安全测试教学，详见 [API文档](WeFinance完整API文档.md#16-安全测试演示api)。

---

## 🚀 快速启动

### 环境要求

- Python 3.12+
- Docker 20+ (可选，用于容器化部署)
- 2GB+ RAM
- Ubuntu 20.04+ / macOS 10.15+ / Windows 10+

### 安装步骤

#### 1. 克隆项目
```bash
cd /var/www/
# 假设项目已存在于 /var/www/wefinance
```

#### 2. 创建虚拟环境
```bash
cd /var/www/wefinance
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

#### 3. 安装依赖
```bash
pip install -r requirements.txt
```

#### 4. 配置数据库
```bash
# 编辑 wefinance/settings.py 配置数据库连接
# 运行迁移
python manage.py migrate
```

#### 5. 创建超级用户
```bash
python manage.py createsuperuser
```

#### 6. 收集静态文件
```bash
python manage.py collectstatic --noinput
```

#### 7. 启动服务器

```bash
# 使用Daphne启动（支持WebSocket，推荐）
daphne -b 0.0.0.0 -p 8000 wefinance.asgi:application

# 或使用Django开发服务器（不支持WebSocket）
python manage.py runserver 0.0.0.0:8000
```

#### 8. 创建测试数据（可选）

```bash
# 创建测试用户
python dev_tools/data_management/create_test_users.py

# 生成账单测试数据
python manage.py generate_bills --username=admin
```

---

## 🐳 Docker 部署

### 快速启动

```bash
# 构建并启动容器
cd /var/www/wefinance
docker compose build
docker compose up -d

# 查看状态
docker compose ps
docker logs wefinance_web
```

### 常用命令

```bash
docker compose up -d      # 启动
docker compose down       # 停止
docker compose restart    # 重启
docker compose logs -f    # 查看日志
```

### 开机自启

```bash
# 安装开机自启服务
sudo cp wefinance.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable wefinance
sudo systemctl start wefinance

# 管理命令
systemctl status wefinance    # 查看状态
systemctl restart wefinance   # 重启
systemctl stop wefinance      # 停止
```

---

## 🌐 访问地址

### 本地访问
```
http://127.0.0.1:8000/
http://localhost:8000/
```

### 局域网访问
```bash
# 查看本机IP地址
ifconfig          # Linux/Mac
ipconfig          # Windows
ip addr show      # Linux (新版)

# 然后使用查到的IP访问，例如：
# http://192.168.x.x:8000/
```

### 主要页面路径
- 首页: `/`
- 用户登录: `/auth/login/`
- 用户注册: `/auth/register/`
- 用户中心: `/user/dashboard/`
- 账单中心: `/user/bills/`
- 产品列表: `/products/`
- 借款中心: `/borrow/`
- 客服系统: `/customer-service/admin/` (客服人员)
- 管理后台: `/admin-panel/`
- Django Admin: `/admin/`

---

## 👥 测试账号

### 基础测试账号（运行 create_test_users.py 创建）

| 角色 | 用户名 | 密码 | 说明 |
|------|--------|------|------|
| 超级管理员 | admin | admin123456 | 拥有所有权限，可访问 /admin/ 和 /admin-panel/ |
| 测试用户 | testuser | test123456 | 普通个人用户 |
| VIP用户 | vipuser | vip123456 | VIP会员，已实名认证，账户余额¥100,000 |

### 扩展测试账号（运行 populate_data.py 创建）

| 角色 | 用户名 | 密码 | 说明 |
|------|--------|------|------|
| 投资者 | investor1 | password123 | 测试投资功能，已实名认证，余额¥50,000 |
| 借款人1 | borrower1 | password123 | 测试借款功能，已实名认证 |
| 借款人2 | borrower2 | password123 | 测试借款功能，已实名认证 |
| 借款人3 | borrower3 | password123 | 测试借款功能，已实名认证 |
| 借款人4 | borrower4 | password123 | 测试借款功能，已实名认证 |

### 社区测试账号（运行 populate_community_data.py 创建）

| 角色 | 用户名 | 密码 | 说明 |
|------|--------|------|------|
| 社区用户1 | investor1 | testpass123 | 社区活跃用户（如已存在则密码不变） |
| 社区用户2 | investor2 | testpass123 | 社区活跃用户 |
| 社区用户3 | investor3 | testpass123 | 社区活跃用户 |
| 专家1 | expert1 | testpass123 | 社区专家用户 |
| 专家2 | expert2 | testpass123 | 社区专家用户 |

**⚠️ 重要提示**: 
- 生产环境请立即修改默认密码！
- 如果多次运行不同的数据生成脚本，部分账号（如investor1）密码可能被覆盖
- 建议按顺序运行：`create_test_users.py` → `populate_data.py` → `populate_community_data.py`

---

## 📁 项目结构

```
wefinance/
├── accounts/              # 用户账户管理
│   ├── models.py         # 用户模型、银行卡、实名认证
│   ├── views.py          # 认证视图
│   ├── api_views.py      # RESTful API
│   └── forms.py          # 表单验证
│
├── products/             # 金融产品管理
│   ├── models.py         # 产品模型
│   └── views.py          # 产品展示
│
├── investments/          # 投资交易
│   ├── models.py         # 投资记录、收益记录
│   ├── views.py          # 投资操作
│   └── api_views.py      # 投资API
│
├── borrow/              # 借款业务
│   ├── models.py         # 借款申请、还款计划
│   ├── views.py          # 借款流程
│   └── api_views.py      # 借款API
│
├── roboadvisor/         # 智能投顾
│   ├── models.py         # 投资策略、风险评估
│   └── views.py          # 投顾推荐
│
├── wealth_plan/         # 财富计划
│   ├── models.py         # 理财计划
│   └── views.py          # 计划管理
│
├── user_center/         # 用户中心
│   ├── models.py         # 账单模型
│   ├── views.py          # 仪表盘、账单、设置
│   └── management/       # 管理命令
│       └── commands/
│           └── generate_bills.py  # 生成账单数据
│
├── community/           # 投资社区
│   ├── models.py         # 帖子、回复、消息
│   └── views.py          # 社区功能
│
├── news/                # 新闻资讯
│   ├── models.py         # 新闻文章
│   └── views.py          # 新闻展示
│
├── admin_panel/         # 管理后台
│   └── views.py          # 管理功能
│
├── pages/               # 静态页面
│   └── views.py          # 关于我们、帮助中心等
│
├── templates/           # HTML模板
│   ├── base/            # 基础模板
│   ├── accounts/        # 用户相关页面
│   ├── user_center/     # 用户中心页面
│   └── ...
│
├── static/              # 静态资源
│   ├── css/             # 样式文件
│   ├── js/              # JavaScript文件
│   ├── images/          # 图片资源
│   └── vendor/          # 第三方库
│
├── media/               # 用户上传文件
│   ├── avatars/         # 用户头像
│   ├── id_cards/        # 身份证照片
│   └── documents/       # 其他文档
│
├── wefinance/           # 项目配置
│   ├── settings.py      # Django配置
│   ├── urls.py          # 路由配置
│   ├── asgi.py          # ASGI配置（WebSocket）
│   └── wsgi.py          # WSGI配置
│
├── customer_service/    # 客服系统
│   ├── consumers.py     # WebSocket消费者
│   ├── routing.py       # WebSocket路由
│   └── views.py         # 客服视图
│
├── dev_tools/           # 开发工具集
│   ├── data_management/ # 数据管理脚本
│   └── README.md        # 工具使用说明
│
├── manage.py            # Django管理脚本
├── requirements.txt     # Python依赖
├── Dockerfile           # Docker构建文件
├── docker-compose.yml   # Docker Compose配置
├── wefinance.service    # systemd服务配置
├── README.md           # 项目说明（本文件）
└── WeFinance完整API文档.md  # API接口文档
```

---



---

## 📚 相关文档

- [Django官方文档](https://docs.djangoproject.com/)
- [Bootstrap文档](https://getbootstrap.com/docs/)
- [PostgreSQL文档](https://www.postgresql.org/docs/)
- [WeFinance API文档](WeFinance完整API文档.md)
- [开发工具说明](dev_tools/README.md)

---

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 📧 联系方式

- **项目地址**: GitHub Repository
- **问题反馈**: Issues
- **邮箱**: support@wefinance.com
- **技术支持**: 工作日 9:00-18:00

---

## 🙏 致谢

感谢以下开源项目：

- [Django](https://www.djangoproject.com/) - Web框架
- [Bootstrap](https://getbootstrap.com/) - UI框架
- [Chart.js](https://www.chartjs.org/) - 图表库
- [Font Awesome](https://fontawesome.com/) - 图标库
- [PostgreSQL](https://www.postgresql.org/) - 数据库

---

<div align="center">

**WeFinance** - 让财富管理更智能

Made with ❤️ by WeFinance Team

</div>