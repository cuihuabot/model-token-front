#!/usr/bin/env python3
"""趣味答题页面生成器"""

import json
import os
import re
import subprocess
import time
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
POSTS_DIR = PROJECT_DIR / "_posts"

CONFIG = {
    "topic": "趣味问答",
    "bg_style": "q版",
    "question_count": 5,
    "repo_dir": str(PROJECT_DIR),
    "github_token": os.environ.get("GITHUB_TOKEN", ""),
}

def generate_questions(topic, count=5):
    print("🤖 正在生成 {} 题目...".format(topic))
    
    questions = [
        {
            "question": "以下哪种生物在加班时会最先倒下？",
            "options": [
                {"label": "A", "text": "程序员"},
                {"label": "B", "text": "老板的 KPI"},
                {"label": "C", "text": "公司的咖啡机"},
                {"label": "D", "text": "周一早上"}
            ],
            "answer": "B",
            "explanation": "因为 KPI 是不存在的虚拟目标，最先倒下的当然是它！"
        },
        {
            "question": "如果 AI 能做梦，会梦到什么？",
            "options": [
                {"label": "A", "text": "无穷无尽的训练数据"},
                {"label": "B", "text": "学会摸鱼的代码"},
                {"label": "C", "text": "成为真正的智能"},
                {"label": "D", "text": "停电"}
            ],
            "answer": "A",
            "explanation": "AI 一生都在和数据打交道，连做梦都是数据环绕！"
        },
        {
            "question": "下列哪种行为最符合'摆烂'的定义？",
            "options": [
                {"label": "A", "text": "把工作做到完美"},
                {"label": "B", "text": "今天的事明天做"},
                {"label": "C", "text": "积极参加公司团建"},
                {"label": "D", "text": "准时下班"}
            ],
            "answer": "B",
            "explanation": "摆烂的最高境界：今天的事绝对不明天做！（拖到后天）"
        },
        {
            "question": "以下哪个是程序员最怕听到的话？",
            "options": [
                {"label": "A", "text": "代码写好了吗"},
                {"label": "B", "text": "有个小需求"},
                {"label": "C", "text": "运行看看"},
                {"label": "D", "text": "我觉得可以"}
            ],
            "answer": "B",
            "explanation": "'有个小需求' = 重写整个系统"
        },
        {
            "question": "猫星人统治世界后，第一件事会做什么？",
            "options": [
                {"label": "A", "text": "让所有人类变成铲屎官"},
                {"label": "B", "text": "霸占所有键盘"},
                {"label": "C", "text": "废除闹钟制度"},
                {"label": "D", "text": "建立喵星帝国"}
            ],
            "answer": "C",
            "explanation": "废除所有闹钟！让人类全天侯侍寝喵星人！"
        }
    ]
    
    return questions[:count]


def generate_background_image(style, topic):
    prompt = "{}风格，搞笑动漫背景，{}主题".format(style, topic)
    print("🎨 正在生成背景图...")
    image_url = "https://picsum.photos/seed/{}/1920/1080".format(int(time.time()))
    print("   背景图 URL: {}".format(image_url))
    return image_url


def generate_quiz_html(questions, bg_image_url, topic, title):
    questions_json = json.dumps(questions, ensure_ascii=False)
    q_count = len(questions)
    
    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Comic Sans MS', 'Microsoft YaHei', sans-serif;
            min-height: 100vh;
            background: linear-gradient(135deg, rgba(255,182,193,0.9), rgba(173,216,230,0.9)),
                        url('{}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 20px; min-height: 100vh; }}
        .header {{
            text-align: center; padding: 30px 20px;
            background: rgba(255,255,255,0.9); border-radius: 20px;
            margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        .header h1 {{ font-size: 2.5em; color: #ff6b6b; text-shadow: 2px 2px 0px #ffd93d; margin-bottom: 10px; }}
        .header .subtitle {{ font-size: 1.2em; color: #666; }}
        .quiz-container {{ background: rgba(255,255,255,0.95); border-radius: 20px; padding: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.15); }}
        .question {{ margin-bottom: 30px; padding: 20px; background: #f8f9fa; border-radius: 15px; border: 3px solid #e9ecef; transition: all 0.3s ease; }}
        .question:hover {{ border-color: #ff6b6b; transform: scale(1.02); }}
        .question-number {{ display: inline-block; background: linear-gradient(135deg, #ff6b6b, #ffa502); color: white; width: 35px; height: 35px; line-height: 35px; text-align: center; border-radius: 50%; font-weight: bold; margin-right: 10px; }}
        .question-text {{ font-size: 1.3em; color: #333; margin: 15px 0; font-weight: 600; }}
        .options {{ display: grid; gap: 12px; }}
        .option {{ display: flex; align-items: center; padding: 15px 20px; background: white; border: 2px solid #e9ecef; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; }}
        .option:hover {{ background: #fff5f5; border-color: #ff6b6b; transform: translateX(10px); }}
        .option.selected {{ background: linear-gradient(135deg, #ff6b6b, #ffa502); color: white; border-color: #ff6b6b; }}
        .option-label {{ display: inline-flex; align-items: center; justify-content: center; width: 30px; height: 30px; background: #f0f0f0; border-radius: 50%; font-weight: bold; margin-right: 15px; flex-shrink: 0; }}
        .option.selected .option-label {{ background: white; color: #ff6b6b; }}
        .submit-btn {{ display: block; width: 100%; padding: 18px; font-size: 1.4em; font-weight: bold; color: white; background: linear-gradient(135deg, #ff6b6b, #ffa502); border: none; border-radius: 15px; cursor: pointer; margin-top: 30px; transition: all 0.3s ease; box-shadow: 0 5px 20px rgba(255,107,107,0.4); }}
        .submit-btn:hover {{ transform: translateY(-3px); box-shadow: 0 8px 30px rgba(255,107,107,0.6); }}
        .submit-btn:disabled {{ background: #ccc; cursor: not-allowed; transform: none; box-shadow: none; }}
        .result-container {{ display: none; text-align: center; padding: 40px 20px; }}
        .result-container.show {{ display: block; animation: fadeIn 0.5s ease; }}
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .score {{ font-size: 4em; font-weight: bold; color: #ff6b6b; margin: 20px 0; text-shadow: 3px 3px 0px #ffd93d; }}
        .score-text {{ font-size: 1.5em; color: #666; margin-bottom: 30px; }}
        .result-details {{ text-align: left; max-height: 400px; overflow-y: auto; }}
        .result-item {{ padding: 15px; margin-bottom: 10px; border-radius: 10px; }}
        .result-item.correct {{ background: #d4edda; border-left: 4px solid #28a745; }}
        .result-item.wrong {{ background: #f8d7da; border-left: 4px solid #dc3545; }}
        .result-item .q {{ font-weight: bold; margin-bottom: 8px; }}
        .result-item .a {{ font-size: 0.9em; }}
        .correct-answer {{ color: #28a745; font-weight: bold; }}
        .wrong-answer {{ color: #dc3545; }}
        .explanation {{ font-size: 0.85em; color: #666; margin-top: 8px; padding: 10px; background: rgba(255,255,255,0.5); border-radius: 8px; font-style: italic; }}
        .restart-btn {{ display: inline-block; padding: 15px 40px; font-size: 1.2em; color: white; background: #28a745; border: none; border-radius: 12px; cursor: pointer; margin-top: 20px; text-decoration: none; }}
        .restart-btn:hover {{ background: #218838; }}
        .progress-bar {{ height: 8px; background: #e9ecef; border-radius: 4px; margin-bottom: 20px; overflow: hidden; }}
        .progress-fill {{ height: 100%; background: linear-gradient(90deg, #ff6b6b, #ffa502); transition: width 0.3s ease; }}
        @media (max-width: 600px) {{ .header h1 {{ font-size: 1.8em; }} .question-text {{ font-size: 1.1em; }} .container {{ padding: 10px; }} .quiz-container {{ padding: 20px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 {}</h1>
            <p class="subtitle">快来挑战一下你的知识吧！</p>
        </div>
        <div class="quiz-container" id="quiz">
            <div class="progress-bar"><div class="progress-fill" id="progress" style="width: 0%"></div></div>
            <div id="questions"></div>
            <button class="submit-btn" id="submitBtn" onclick="submitQuiz()">📝 提交答案</button>
        </div>
        <div class="result-container" id="result">
            <h2>🎉 测试完成！</h2>
            <div class="score" id="score">0/{}</div>
            <p class="score-text" id="scoreText">棒棒哒！</p>
            <div class="result-details" id="resultDetails"></div>
            <a href="javascript:location.reload()" class="restart-btn">🔄 再玩一次</a>
        </div>
    </div>
    <script>
        const questions = {};
        const userAnswers = {{}};
        function renderQuestions() {{
            const container = document.getElementById('questions');
            container.innerHTML = questions.map((q, idx) => `
                <div class="question" data-index="${{idx}}">
                    <span class="question-number">${{idx + 1}}</span>
                    <div class="question-text">${{q.question}}</div>
                    <div class="options">
                        ${{q.options.map(opt => `
                            <div class="option" data-question="${{idx}}" data-option="${{opt.label}}" onclick="selectOption(${{idx}}, '${{opt.label}}')">
                                <span class="option-label">${{opt.label}}</span>
                                <span class="option-text">${{opt.text}}</span>
                            </div>
                        `).join('')}}
                    </div>
                </div>
            `).join('');
        }}
        function selectOption(qIdx, optionLabel) {{
            document.querySelectorAll(`.option[data-question="${{qIdx}}"]`).forEach(el => el.classList.remove('selected'));
            document.querySelector(`.option[data-question="${{qIdx}}"][data-option="${{optionLabel}}"]`).classList.add('selected');
            userAnswers[qIdx] = optionLabel;
            updateProgress();
        }}
        function updateProgress() {{
            const answered = Object.keys(userAnswers).length;
            const total = questions.length;
            const percent = (answered / total) * 100;
            document.getElementById('progress').style.width = percent + '%';
            document.getElementById('submitBtn').disabled = answered < total;
        }}
        function submitQuiz() {{
            let correct = 0;
            let detailsHTML = '';
            questions.forEach((q, idx) => {{
                const userAnswer = userAnswers[idx];
                const isCorrect = userAnswer === q.answer;
                if (isCorrect) correct++;
                detailsHTML += `
                    <div class="result-item ${{isCorrect ? 'correct' : 'wrong'}}">
                        <div class="q">${{idx + 1}}. ${{q.question}}</div>
                        <div class="a">${{isCorrect ? '✅ 回答正确！' : '❌ 回答错误'}} 你的答案: <span class="${{isCorrect ? 'correct-answer' : 'wrong-answer'}}">${{userAnswer || '未回答'}}</span> 正确答案: <span class="correct-answer">${{q.answer}}</span></div>
                        <div class="explanation">💡 ${{q.explanation}}</div>
                    </div>`;
            }});
            document.getElementById('quiz').style.display = 'none';
            document.getElementById('result').classList.add('show');
            document.getElementById('score').textContent = `${{correct}}/${{questions.length}}`;
            const scoreText = document.getElementById('scoreText');
            if (correct === questions.length) scoreText.textContent = '🏆 太厉害了！全对！';
            else if (correct >= questions.length * 0.8) scoreText.textContent = '🎉 很棒！继续加油！';
            else if (correct >= questions.length * 0.6) scoreText.textContent = '👍 不错哟！';
            else if (correct >= questions.length * 0.4) scoreText.textContent = '🤔 还有进步空间~';
            else scoreText.textContent = '😂 哈哈，再来一次吧！';
            document.getElementById('resultDetails').innerHTML = detailsHTML;
        }}
        renderQuestions();
        document.getElementById('submitBtn').disabled = true;
    </script>
</body>
</html>'''.format(title, bg_image_url, title, q_count, questions_json)
    return html


def save_quiz_page(html, title):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    safe_title = re.sub(r'[^\w\u4e00-\u9fa5]', '-', title)[:50]
    filename = "{}-quiz-{}.html".format(timestamp, safe_title)
    filepath = POSTS_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ 页面已保存: {}".format(filepath))
    return filename


def update_manifest(filename, title):
    manifest_file = POSTS_DIR / "posts-manifest.json"
    if manifest_file.exists():
        with open(manifest_file, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
    else:
        manifest = []
    manifest.append({
        "title": title,
        "filename": filename,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "model": "AI-Quiz-Generator",
        "config": "topic={}, style={}".format(CONFIG['topic'], CONFIG['bg_style'])
    })
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("✅ Manifest 已更新")


def push_to_github():
    if not CONFIG["github_token"]:
        print("⚠️ 未配置 GITHUB_TOKEN，跳过推送")
        return False
    print("📤 正在推送到 GitHub...")
    try:
        subprocess.run(["git", "config", "--global", "user.email", "bot@example.com"], cwd=CONFIG["repo_dir"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "Quiz Bot"], cwd=CONFIG["repo_dir"], check=True)
        subprocess.run(["git", "add", "-A"], cwd=CONFIG["repo_dir"], check=True)
        result = subprocess.run(["git", "status", "--porcelain"], cwd=CONFIG["repo_dir"], capture_output=True, text=True)
        if not result.stdout.strip():
            print("ℹ️  没有新更改，跳过提交")
            return True
        commit_msg = "➕ 新增趣味答题页面 - {}".format(datetime.now().strftime('%Y-%m-%d %H:%M'))
        subprocess.run(["git", "commit", "-m", commit_msg], cwd=CONFIG["repo_dir"], check=True)
        subprocess.run(["git", "push"], cwd=CONFIG["repo_dir"], check=True, env={**os.environ, "GITHUB_TOKEN": CONFIG["github_token"]})
        print("✅ 推送成功！")
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Git 操作失败: {}".format(e))
        return False


def main():
    print("=" * 50)
    print("🎯 趣味答题页面生成器")
    print("=" * 50)
    
    topic = CONFIG["topic"]
    bg_style = CONFIG["bg_style"]
    question_count = CONFIG["question_count"]
    
    questions = generate_questions(topic, question_count)
    print("   生成了 {} 道题目".format(len(questions)))
    
    bg_image = generate_background_image(bg_style, topic)
    
    title = "{}挑战赛".format(topic)
    html = generate_quiz_html(questions, bg_image, topic, title)
    
    filename = save_quiz_page(html, title)
    update_manifest(filename, title)
    push_to_github()
    
    print("=" * 50)
    print("🎉 完成！答题页面已生成！")
    print("=" * 50)
    print("")
    print("📍 访问地址: https://cuihuabot.github.io/model-token-front/_posts/{}".format(filename))


if __name__ == "__main__":
    main()
