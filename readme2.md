# LazyCraft

## 一、简介

LazyCraft 是一个基于 **LazyLLM** 构建的 AI Agent 应用开发与管理平台，旨在协助开发者以 **低门槛、低成本** 快速构建和发布大模型应用。

无论是非开发者还是技术团队，都可以通过平台快速构建如 **数据洞察师、文献综述生成器、代码理解助手**等多样化的 AI 应用，并发布到商店或通过 API 集成到业务系统中。

平台不仅支持 **低代码、组件化的应用编排**，提供从应用创建、调试、发布到监控的全链路体验，还集成了全流程的 **模型管理能力**，涵盖数据集管理、模型微调与推理服务。

LazyCraft 凭借灵活可插拔的组件设计，能够帮助团队快速验证想法、分析并优化效果，加速AI技术在业务场景中的落地与迭代。

### 平台特点

- **全流程闭环**：从应用创建、调试、发布到监控与 Bad Case 分析优化，完整覆盖研发链路，支持快速原型迭代直达生产部署。
- **灵活可插拔架构**：核心模块可替换，兼容多种向量库与 RAG 策略，支持按需调整检索结构与自定义知识库编排，满足不同场景需求。

📖 具体使用教程请参考：[用户文档](https://lazyllm.sensetime.com/console/api/doc/view)

---

## 二、主要功能

### 1. 应用搭建

- 提供丰富的 **可视化组件**，用户可在画布上快速构建、调试和发布 AI 应用，支持更新发布与版本管理。
- 内置多种应用模板，**开箱即用**，帮助用户快速上手体验。

### 2. 全面的模型服务

- 集成多家模型厂商的 **本地与在线模型服务**，涵盖大语言模型、图文理解、文生图、语音转文字、文字转语音、向量模型、重排模型、OCR 模型。
- 支持从 **模型推理、微调到评测** 的完整流程，轻松切换不同模型。

### 3. 资源创建

支持创建并管理 **Prompt、知识库、数据集、数据库、工具** 等资源：

- **Prompt 管理**：支持创建、编辑和管理提示词，内置模板与 AI 辅助编写能力。
- **知识库**：提供 Reader、Rewrite、Retriever、Rerank 等核心组件，覆盖从文档摄入到检索的完整链路。
  - 支持灵活配置 RAG 策略和多路召回
  - 兼容多种文件格式：PDF、Word、PPT、Excel、CSV、TXT、JSON、HTML、Markdown、LaTeX
- **工具与 MCP**：支持自定义工具或外部 API 接入，并可通过 MCP 服务扩展功能，可在画布中直接调用。
- **数据集**：支持 `json`、`csv`、`txt` 等多格式文件导入，便于训练、评测与应用场景使用。
  - 提供版本管理与模板下载
  - 支持数据清洗、增强与标注等处理操作

### 4. 多租户管理

- 支持 **多租户与多工作空间**，提供细粒度的 **权限控制与 API Key 管理**。
- 结合 **日志与审计功能**，满足企业级的安全与合规需求。

### 5. API 发布

- 提供 **标准化接口**，便于将应用无缝集成到各类企业系统与业务流程中。

---

## 三、快速开始

### 1. 克隆代码
```
git clone https://gitlab.bj.sensetime.com/lazyllm/lazycraft.git
cd lazycraft
# git submodule update --init
```

### 2. 启动服务
```
# 设置环境变量为平台的登录地址，例如本地部署 http://127.0.0.1:50382
export WEB_CONSOLE_ENDPOINT="http://your-console-url"

cd docker
docker compose up -d
```

### 3. 访问服务
```
和上面 WEB_CONSOLE_ENDPOINT 配置的一样
http://127.0.0.1:50382
默认账密 admin:Admin@123456
```

---
## 四. 自定义构建镜像

### 1. 如果你想要自己构建镜像而不是使用默认的：
```
git clone https://gitlab.bj.sensetime.com/lazyllm/lazycraft.git
cd lazycraft
# git submodule update --init
```

### 2. 构建后端服务镜像
```
cd back

# 使用在线模型
docker build --build-arg COMMIT_SHA=$(git rev-parse HEAD) -t lazycraft-back:latest .

# 使用本地模型
# 使用本地算力卡请更改 docker-compose.yml 中镜像名，并且取消 deploy 注释的部分
docker build -f gpu.Dockerfile --build-arg COMMIT_SHA=$(git rev-parse HEAD) -t lazycraft-back:latest .
```

### 3. 构建前端服务镜像
```
cd front
docker build --build-arg COMMIT_SHA=$(git rev-parse HEAD) -t lazycraft-front:latest .
```

### 4. 启动服务
```
# 设置环境变量为平台的登录地址，例如本地部署 http://127.0.0.1:50382
export WEB_CONSOLE_ENDPOINT="http://your-console-url"

export BACK_IMAGE="lazycraft-back:latest"
export FRONT_IMAGE="lazycraft-front:latest"
cd docker
docker compose up -d
```
