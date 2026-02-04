---
layout: home
title: Model Responses Dashboard
---

<div class="dashboard">
  <h1>Model Response Dashboard</h1>
  <p>This site displays generated responses from various AI models.</p>
  
  <div class="recent-responses">
    <h2>Recent Model Responses</h2>
    <ul>
      {% for post in site.posts limit: 10 %}
        <li>
          <a href="{{ post.url }}">{{ post.title }}</a>
          <span class="date">{{ post.date | date: "%Y-%m-%d %H:%M" }}</span>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>
