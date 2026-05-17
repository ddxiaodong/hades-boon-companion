"""
哈迪斯助手 — FastAPI 后端服务
提供 AI 问答 API，使用 RAG 检索 + LLM API（默认 LongCat）
"""

import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv

from knowledge import build_context, search_knowledge

load_dotenv()

app = FastAPI(title="哈迪斯助手 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.longcat.chat/openai/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "LongCat-Flash-Lite")

SYSTEM_PROMPT = """你是哈迪斯(Hades)游戏专家助手。你精通游戏中所有祝福(Boons)、双人祝福(Duo Boons)、传奇祝福(Legendary Boons)、武器形态(Weapon Aspects)和游戏机制。

回答规则：
1. 优先使用提供的「相关知识」来回答问题，确保信息准确
2. 如果知识库中没有相关信息，可以基于你的游戏知识回答，但要说明"此信息来自我的游戏知识，可能有版本差异"
3. 用中文回答，游戏专有名词首次出现时附带英文原名
4. 回答要简洁实用，重点突出游戏玩家关心的数值和前置条件
5. 如果用户问流派搭配(Build)，推荐具体的祝福组合和适用武器
6. 格式清晰，使用适当的分点和emoji增强可读性
7. 如果用户问题模糊，可以追问澄清"""


class ChatRequest(BaseModel):
    message: str
    history: list[dict] = []


class ChatResponse(BaseModel):
    reply: str
    sources: list[dict] = []


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "哈迪斯助手", "model": LLM_MODEL}


@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not LLM_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="未配置 LLM_API_KEY 环境变量。请复制 .env.example 为 .env 并填入您的 API Key。"
        )

    user_msg = req.message.strip()
    if not user_msg:
        raise HTTPException(status_code=400, detail="消息不能为空")

    # RAG 检索相关知识
    context = build_context(user_msg, top_k=3)
    sources = search_knowledge(user_msg, top_k=3)

    # 构建消息
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # 添加历史消息（最近20条）
    for h in req.history[-20:]:
        messages.append(h)

    # 构建用户消息（包含检索到的知识）
    if context:
        user_content = f"{context}\n\n用户问题：{user_msg}\n\n请基于以上知识回答问题。"
    else:
        user_content = user_msg

    messages.append({"role": "user", "content": user_content})

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(
                f"{LLM_BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {LLM_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": LLM_MODEL,
                    "messages": messages,
                    "temperature": 0.7,
                    "max_tokens": 1500,
                },
            )
            resp.raise_for_status()
            data = resp.json()

        message = data["choices"][0]["message"]
        # Thinking 模型 content 可能为空或缺失，尝试多种方式获取回复
        reply = message.get("content") or message.get("reasoning_content") or ""
        if not reply:
            raise HTTPException(
                status_code=502,
                detail=f"LLM 返回为空。raw message keys: {list(message.keys())}"
            )

        return ChatResponse(
            reply=reply,
            sources=[{"title": s["title"], "content": s["content"][:200]}
                     for s in sources]
        )

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"LLM API 错误 ({e.response.status_code}): {e.response.text[:300]}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"无法连接 LLM API: {str(e)}"
        )


@app.post("/api/search")
async def search(req: ChatRequest):
    """纯知识库搜索（不使用AI）"""
    results = search_knowledge(req.message, top_k=5)
    return {"query": req.message, "results": results}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
