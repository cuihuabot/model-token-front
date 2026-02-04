// Model Token Frontend - Main JavaScript

class ModelMonitor {
    constructor() {
        this.apiUrl = 'http://localhost:3000'; // 后端API地址
        this.refreshInterval = 30000; // 30秒刷新一次
        this.init();
    }

    async init() {
        console.log('Model Monitor initialized');
        await this.fetchModelData();
        this.startAutoRefresh();
        this.setupEventListeners();
    }

    async fetchModelData() {
        try {
            // 从后端API获取模型数据
            const response = await fetch(`${this.apiUrl}/api/models`);
            const models = await response.json();
            
            if (response.ok) {
                this.renderStatusCards(models);
                console.log('Model data fetched successfully', models);
            } else {
                console.error('Failed to fetch model data:', response.statusText);
            }
        } catch (error) {
            console.error('Error fetching model data:', error);
        }
    }

    renderStatusCards(models) {
        const container = document.getElementById('status-cards');
        if (!container) return;

        container.innerHTML = models.map(model => {
            const statusClass = this.getModelStatusClass(model);
            return `
                <div class="status-card ${statusClass}">
                    <h3>${model.name}</h3>
                    <div class="status-info"><strong>提供商:</strong> ${model.provider}</div>
                    <div class="status-info"><strong>状态:</strong> <span class="status-badge ${statusClass}">${this.getStatusText(statusClass)}</span></div>
                    <div class="status-info"><strong>活跃:</strong> ${model.is_active ? '是' : '否'}</div>
                    <div class="status-info"><strong>创建时间:</strong> ${new Date(model.created_at).toLocaleString()}</div>
                </div>
            `;
        }).join('');
    }

    getModelStatusClass(model) {
        // 简化的状态判断逻辑，实际应用中可以从API获取更详细的健康状态
        if (!model.is_active) return 'offline';
        // 这里可以加入更复杂的逻辑来判断在线/离线/缓慢状态
        return 'online';
    }

    getStatusText(statusClass) {
        switch(statusClass) {
            case 'online': return '在线';
            case 'offline': return '离线';
            case 'slow': return '缓慢';
            default: return '未知';
        }
    }

    startAutoRefresh() {
        setInterval(async () => {
            await this.fetchModelData();
        }, this.refreshInterval);
    }

    setupEventListeners() {
        // 设置页面导航事件监听器
        document.querySelectorAll('nav a').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = e.target.getAttribute('href').substring(1);
                this.navigateTo(targetId);
            });
        });
    }

    navigateTo(sectionId) {
        // 简单的导航功能
        document.getElementById(sectionId)?.scrollIntoView({ behavior: 'smooth' });
    }

    // 用于测试API连接的方法
    async testConnection() {
        try {
            const response = await fetch(`${this.apiUrl}/health`);
            return response.ok;
        } catch (error) {
            console.error('Connection test failed:', error);
            return false;
        }
    }
}

// 初始化应用
document.addEventListener('DOMContentLoaded', () => {
    new ModelMonitor();
});