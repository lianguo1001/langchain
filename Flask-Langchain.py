import logging
import os
# 设置openai国内代理的官网和API
os.environ["OPENAI_API_BASE"] = "https://api.openai-proxy.org/v1"
os.environ["OPENAI_API_KEY"] = "sk-odj5uP5tFm0st1L2SCX72caSxWIypIYsuD8kpjH4qkshHPu9"
# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from langchain_openai import OpenAI  # 更新导入
from langchain_community.tools import Tool  # 更新导入
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory

# 定义工具函数
def custom_tool(input_text):
    # 这里可以定义工具的具体逻辑
    prompt = f"""
        要求使得文本更加流畅易读，保证原文含义不变，字数保持与原文相当的水平，符合正常的语言顺序和语法要求，更加专业化：
        {input_text}

         润色要求：
        1. 保持原意不变。
        2. 使用更高级的词汇和句式。
        3. 确保语法正确。
        4. 使文本更具吸引力。
        5. 与原文的字数相差不多，保证原文整体内容都有所呈现。
        """

    # 调用模型生成润色后的文本
    try:
        response = model(prompt)
        return response
    except Exception as e:
        logger.error(f"调用模型时出错: {e}")
        return f"调用模型时出错: {e}"

# 初始化LLM和工具
model = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
# 工具列表，包含了定义工具的名称、工具的功能、针对工具作用的描述
tools = [
    Tool(
        name="文本润色",
        func=custom_tool,
        description="可以针对文本进行润色和优化，使得文本更加专业和流畅。"
    )
]

# 初始化记忆
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True) # 将记忆存储到"chat_history"键值中

# 初始化Agent
agent = initialize_agent(tools, model, agent="zero-shot-react-description", verbose=True, memory=memory)

from flask import Flask, request, render_template_string
# 创建 Flask 应用
app = Flask(__name__)

# 定义首页路由
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    chat_history = []
    if request.method == "POST":
        # 获取用户输入
        user_input = request.form.get("user_input")
        # 输入验证
        if user_input.strip():
            try:
                # 执行 Agent 逻辑
                result = agent.run(user_input)
                # 获取对话历史
                chat_history = memory.load_memory_variables({})["chat_history"] # 加载对应键值所对应的字典中的变量信息
            except Exception as e:
                logger.error(f"执行 Agent 时出错: {e}")
                result = f"执行 Agent 时出错: {e}"
        else:
            result = "输入不能为空，请重新输入。"
    # 渲染 HTML 页面
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>LangChain Agent Web 服务</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                }
                form {
                    margin-top: 20px;
                }
                textarea {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                }
                select {
                    padding: 10px;
                    margin-bottom: 10px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                h2 {
                    margin-top: 20px;
                }
                #chat-history {
                    border: 1px solid #ccc;
                    padding: 10px;
                    margin-top: 20px;
                }
                .user-message {
                    color: blue;
                }
                .agent-message {
                    color: green;
                }
            </style>
        </head>
        <body>
            <h1>LangChain Agent Web 服务</h1>
            <form method="POST">
                <label for="user_input">请输入你的问题：</label><br>
                <textarea id="user_input" name="user_input" rows="4" cols="50"></textarea><br>
                <input type="submit" value="提交">
            </form>
            {% if result %}
                <h2>结果：</h2>
                <p>{{ result }}</p>
            {% endif %}
            <div id="chat-history">
                <h2>对话历史</h2>
                {% for message in chat_history %}
                    {% if message.type == "human" %}
                        <p class="user-message">{{ message.content }}</p>
                    {% else %}
                        <p class="agent-message">{{ message.content }}</p>
                    {% endif %}
                {% endfor %}
            </div>
        </body>
        </html>
        """,
        result=result,
        chat_history=chat_history
    )

# 启动 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)