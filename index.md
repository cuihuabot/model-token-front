---
layout: home
title: 模型接口管理平台
---

# 模型接口管理平台

欢迎来到模型接口管理平台，这里展示各种大模型API接口的状态和性能。

## 最新模型响应

<div class="model-responses-grid">
<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-claude-sonnet-api-test-config.html">claude-sonnet - api-test-config - 2026-02-04_20-30-23-281Z</a></h3>
  <p><strong>模型:</strong> claude-sonnet</p>
  <p><strong>配置:</strong> api-test-config</p>
  <p><strong>时间:</strong> 2026-02-04_20-30-23-281Z</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-claude-sonnet-api-test-config.html">查看详情</a></p>
</div>

<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-command-r-plus-config.html">command-r - plus-config - 2026-02-04_20-34-41-517Z</a></h3>
  <p><strong>模型:</strong> command-r</p>
  <p><strong>配置:</strong> plus-config</p>
  <p><strong>时间:</strong> 2026-02-04_20-34-41-517Z</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-command-r-plus-config.html">查看详情</a></p>
</div>

<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-gemini-pro-default-config.html">Gemini Pro Response - Default Config - 2026-02-05_04-01-22</a></h3>
  <p><strong>模型:</strong> gemini-pro</p>
  <p><strong>配置:</strong> default-config</p>
  <p><strong>时间:</strong> 2026-02-05_04-01-22</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-gemini-pro-default-config.html">查看详情</a></p>
</div>

<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-gpt-4-default-config.html">gpt-4 - default-config - 2026-02-04_20-26-04-903Z</a></h3>
  <p><strong>模型:</strong> gpt-4</p>
  <p><strong>配置:</strong> default-config</p>
  <p><strong>时间:</strong> 2026-02-04_20-26-04-903Z</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-gpt-4-default-config.html">查看详情</a></p>
</div>

<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-llama-3-api-prod-config.html">llama-3 - api-prod-config - 2026-02-04_20-31-06-250Z</a></h3>
  <p><strong>模型:</strong> llama-3</p>
  <p><strong>配置:</strong> api-prod-config</p>
  <p><strong>时间:</strong> 2026-02-04_20-31-06-250Z</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-llama-3-api-prod-config.html">查看详情</a></p>
</div>

<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-mistral-large-v1-config.html">mistral-large - v1-config - 2026-02-04_20-31-49-395Z</a></h3>
  <p><strong>模型:</strong> mistral-large</p>
  <p><strong>配置:</strong> v1-config</p>
  <p><strong>时间:</strong> 2026-02-04_20-31-49-395Z</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-mistral-large-v1-config.html">查看详情</a></p>
</div>

<div class="model-response-card">
  <h3><a href="{{ site.baseurl }}/_posts/2026-02-04-test-model-test-config.html">test-model - test-config - 2026-02-04_20-08-14-412Z</a></h3>
  <p><strong>模型:</strong> test-model</p>
  <p><strong>配置:</strong> test-config</p>
  <p><strong>时间:</strong> 2026-02-04_20-08-14-412Z</p>
  <p><a href="{{ site.baseurl }}/_posts/2026-02-04-test-model-test-config.html">查看详情</a></p>
</div>

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
