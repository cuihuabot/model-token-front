---
layout: home
title: 模型接口管理平台
---

# 模型接口管理平台

欢迎来到模型接口管理平台，这里展示各种大模型API接口的状态和性能。

## 最新模型响应

<div class="model-responses-grid">
{% for post in site.posts limit: 10 %}
<div class="model-response-card">
  <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  <p><strong>模型:</strong> {{ post.model }}</p>
  <p><strong>配置:</strong> {{ post.config }}</p>
  <p><strong>时间:</strong> {{ post.timestamp }}</p>
  <p><a href="{{ post.url | relative_url }}">查看详情</a></p>
</div>
{% endfor %}
</div>

## 支持的模型

- OpenAI GPT系列
- Google Gemini系列
- Anthropic Claude系列
- Meta Llama系列
- Mistral系列
- 通义千问系列
- 以及其他主流模型

<script>
  // Simple script to improve the display of model response cards
  document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.model-response-card');
    cards.forEach(card => {
      card.style.border = '1px solid #ddd';
      card.style.borderRadius = '8px';
      card.style.padding = '16px';
      card.style.marginBottom = '16px';
      card.style.backgroundColor = '#f9f9f9';
    });
  });
</script>