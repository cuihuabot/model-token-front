# Model Token Frontend

前端项目，用于展示从模型接口后端定时调用的模型接口数据。

## 项目结构

```
model-token-front/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── js/
│   │   └── main.js
│   ├── css/
│   │   └── style.css
│   └── assets/
├── package.json
└── README.md
```

## 功能需求

1. 定时从后端API获取模型接口数据
2. 展示模型状态、响应时间、可用性等指标
3. 提供可视化图表展示历史趋势
4. 实现告警通知功能