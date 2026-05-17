"""
Hades 游戏知识库 — 构建与检索
将所有祝福、武器、双人祝福数据组织为可检索的知识文档
"""

# ============================================================
# 神明基础信息
# ============================================================
GODS = {
    "zeus": {
        "name": "宙斯", "name_en": "Zeus", "icon": "⚡",
        "desc": "闪电之神，掌管天空与雷霆。祝福以链式闪电为核心，在敌人间弹射造成范围伤害。",
        "status": "Jolted（电击）— 敌人攻击时会对自己造成伤害",
        "keepsake": "雷霆信物 (Thunder Signet)",
        "playstyle": "适合高攻速武器，闪电链清场效率极高"
    },
    "poseidon": {
        "name": "波塞冬", "name_en": "Poseidon", "icon": "🌊",
        "desc": "海神，掌管海洋与地震。祝福以击退为核心，将敌人撞向墙壁造成额外伤害。",
        "status": "Rupture（割裂）— 敌人移动时受到持续伤害",
        "keepsake": "海螺壳 (Conch Shell)",
        "playstyle": "适合在狭窄地图作战，撞墙伤害极高"
    },
    "athena": {
        "name": "雅典娜", "name_en": "Athena", "icon": "🛡️",
        "desc": "智慧与战争女神。祝福以偏转（Deflect）为核心，可反弹敌方弹幕。",
        "status": "Exposed（暴露）— 敌人受到背刺伤害+50%",
        "keepsake": "猫头鹰吊坠 (Owl Pendant)",
        "playstyle": "防御型打法首选，偏转提供极高生存能力"
    },
    "ares": {
        "name": "阿瑞斯", "name_en": "Ares", "icon": "🗡️",
        "desc": "战神，掌管战争与毁灭。祝福以毁灭（Doom）为核心，延迟爆发高额伤害。",
        "status": "Doom（毁灭）— 延迟后造成一次性高额伤害",
        "keepsake": "血之瓶 (Blood-Filled Vial)",
        "playstyle": "适合打一波爆发的玩法，配合多次施加叠加毁灭"
    },
    "aphrodite": {
        "name": "阿佛洛狄忒", "name_en": "Aphrodite", "icon": "💕",
        "desc": "爱与美之神。祝福以虚弱（Weak）为核心，降低敌人造成伤害。",
        "status": "Weak（虚弱）— 敌人造成伤害-30%（最高可叠至-47%）",
        "keepsake": "永恒玫瑰 (Eternal Rose)",
        "playstyle": "提供最高增伤倍率和强力减伤，攻守兼备"
    },
    "artemis": {
        "name": "阿尔忒弥斯", "name_en": "Artemis", "icon": "🏹",
        "desc": "狩猎女神。祝福以暴击为核心，提供高额暴击几率和暴击伤害加成。",
        "status": "Marked（标记）— 被命中后有几率标记敌人，被标记者暴击率+30%",
        "keepsake": "翡翠箭头 (Adamant Arrowhead)",
        "playstyle": "追求高爆发暴击伤害的玩家首选"
    },
    "demeter": {
        "name": "德墨忒尔", "name_en": "Demeter", "icon": "❄️",
        "desc": "丰收与季节女神。祝福以冰冻（Chill）为核心，减速敌人并在10层后爆炸。",
        "status": "Chill（冰冻）— 逐层减速，叠满10层引发爆炸并清除效果",
        "keepsake": "冰霜花环 (Frostbitten Horn)",
        "playstyle": "控制型打法，冰冻让敌人几乎无法行动"
    },
    "dionysus": {
        "name": "狄俄尼索斯", "name_en": "Dionysus", "icon": "🍷",
        "desc": "酒神，掌管葡萄酒与狂欢。祝福以宿醉（Hangover）为核心，持续的DoT伤害。",
        "status": "Hangover（宿醉）— 每0.5秒造成伤害，最高叠加5层（低耐受力双人祝福可至8层）",
        "keepsake": "满溢之杯 (Overflowing Cup)",
        "playstyle": "持续伤害型，叠满宿醉后伤害可观"
    },
    "hermes": {
        "name": "赫尔墨斯", "name_en": "Hermes", "icon": "👟",
        "desc": "奥林匹斯信使。祝福以速度和闪避为核心，提升攻击速度、移动速度和闪避几率。",
        "status": "无专属状态异常",
        "keepsake": "羽翼之鞋 (Lambent Plume)",
        "playstyle": "提升整体机动性和操作手感，几乎任何流派都受益"
    },
    "chaos": {
        "name": "混沌", "name_en": "Chaos", "icon": "🌀",
        "desc": "原始混沌之神。祝福以「先诅咒后祝福」为核心，承受3~5次遭遇的负面效果后获得永久增益。",
        "status": "无专属状态异常",
        "keepsake": "宇宙之卵 (Cosmic Egg)",
        "playstyle": "有风险有回报，混沌祝福可以极大提升上限"
    }
}

# ============================================================
# 武器知识
# ============================================================
WEAPONS_KNOWLEDGE = """
=== 哈迪斯6把冥界武器 ===

1. 冥界之刃 Stygian Blade (Stygius)
- 原使用者：扎格列欧斯
- 形态：
  * 扎格列欧斯：攻速和移速+3%~15%
  * 涅墨西斯：特殊攻击后3秒，攻击获得+15%~30%暴击
  * 波塞冬：特殊攻击可弹出血石，投射伤害+10%~50%
  * 亚瑟(隐藏)：圣剑Excalibur，特殊创建神圣领域（减伤20%~40%），生命+50

2. 永恒之枪 Eternal Spear (Varatha)
- 原使用者：哈迪斯
- 解锁：4冥界钥匙
- 形态：
  * 扎格列欧斯：特殊伤害/范围/速度+10%~25%
  * 阿喀琉斯：投枪后Raging Rush冲刺取回，之后4次攻击/投射伤害+50%~150%
  * 哈迪斯：旋转攻击变大范围Punishing Sweep，被命中敌人10秒内受伤+30%~150%
  * 关羽(隐藏)：霜寒偃月刀，旋转攻击为远程回复弹，生命与治疗-70%~-50%

3. 混沌之盾 Shield of Chaos (Aegis)
- 原使用者：宙斯与雅典娜
- 解锁：3冥界钥匙
- 形态：
  * 扎格列欧斯：攻击与冲刺攻击伤害+3~15
  * 混沌：盾冲后特殊额外投掷+1~5面盾牌
  * 宙斯：特殊变为Blitz Disc持续旋转攻击，可同时普攻
  * 贝奥武夫(隐藏)：盾冲载入血石造成Dragon Rush爆炸，伤害+10%

4. 追心之弓 Heart-Seeking Bow (Coronacht)
- 原使用者：赫拉
- 解锁：1冥界钥匙
- 形态：
  * 扎格列欧斯：攻击暴击+3%~15%
  * 喀戎：特殊自动追踪上次被攻击命中的敌人(4~8发)
  * 赫拉：血石载入攻击，命中时触发投射效果
  * 罗摩(隐藏)：Celestial Sharanga，蓄力攻击极强，特殊施加Shared Suffering

5. 玛尔丰双拳 Twin Fists of Malphon
- 原使用者：德墨忒尔
- 解锁：8冥界钥匙（需先解锁前4种武器）
- 形态：
  * 扎格列欧斯：闪避+5%~15%
  * 塔洛斯：特殊变Magnetic Cutter，磁力拉近敌人，4秒内增伤+8%~40%
  * 德墨忒尔：12连击后下次特殊额外击中1~5次
  * 吉尔伽美什(隐藏)：Claws of Enkidu，冲刺上勾拳施加Maim，冲刺次数+2

6. 坚冥轨 Adamant Rail (Exagryph)
- 原使用者：赫斯提亚
- 解锁：8冥界钥匙（需先解锁所有其他武器）
- 形态：
  * 扎格列欧斯：弹药容量+4~12
  * 厄里斯：吸收手雷爆炸后8秒内全局增伤+12%~60%
  * 赫斯提亚：手动装填后下一发为强化射击(50~150伤害)
  * 路西法(隐藏)：Igneus Eden，攻击变持续光束，特殊投放Hellfire能量球
"""

# ============================================================
# 双人祝福详细知识
# ============================================================
DUO_BOONS_KNOWLEDGE = """
=== 哈迪斯28个双人祝福 (Duo Boons) ===
双人祝福需要至少1个来自每位相关神明的合格祝福才能触发。

【阿佛洛狄忒 + 阿瑞斯】渴望诅咒 (Curse of Longing)：毁灭效果持续打击虚弱敌人，每次50%递减。
【阿佛洛狄忒 + 阿尔忒弥斯】心碎撕裂 (Heart Rend)：暴击对虚弱敌人额外+150%伤害。最强增伤双人祝福之一。
【阿佛洛狄忒 + 雅典娜】离别射击 (Parting Shot)：投射获得背刺加成（+35%）。
【阿佛洛狄忒 + 德墨忒尔】冰冷拥抱 (Cold Embrace)：水晶光束朝你发射，持续+4秒，投射伤害+30%。
【阿佛洛狄忒 + 狄俄尼索斯】低耐受力 (Low Tolerance)：虚弱敌人宿醉可叠加至8层。
【阿佛洛狄忒 + 波塞冬】甜蜜琼浆 (Sweet Nectar)：力量石榴效果额外+1级。
【阿佛洛狄忒 + 宙斯】闷热空气 (Smoldering Air)：神圣计量表自动充能但上限25%。

【阿尔忒弥斯 + 阿瑞斯】狩猎刀刃 (Hunting Blades)：刀刃裂隙更快并自动追踪敌人。
【阿尔忒弥斯 + 雅典娜】致命反击 (Deadly Reversal)：偏转后短暂+20%暴击率(2秒)。
【阿尔忒弥斯 + 德墨忒尔】水晶清晰 (Crystal Clarity)：水晶光束伤害+10%，追踪更强。
【阿尔忒弥斯 + 狄俄尼索斯】分裂头痛 (Splitting Headache)：每层宿醉+1.5%暴击率。
【阿尔忒弥斯 + 波塞冬】幻影射击 (Mirage Shot)：投射额外发射第二发(30%伤害)。
【阿尔忒弥斯 + 宙斯】避雷针 (Lightning Rod)：地上的血石每秒闪电打击敌人(70伤害)。需要Infernal Soul。

【雅典娜 + 阿瑞斯】仁慈终结 (Merciful End)：偏转立即激活毁灭效果(40伤害)。非常强力的combo。
【雅典娜 + 德墨忒尔】顽固之根 (Stubborn Roots)：无死亡抗拒时缓慢恢复生命。
【雅典娜 + 宙斯】闪电方阵 (Lightning Phalanx)：方阵射击在敌人间弹射最多3次。
【雅典娜 + 狄俄尼索斯】计算风险 (Calculated Risk)：敌人远程弹幕速度减慢50%。
【雅典娜 + 波塞冬】不动如山 (Unshakeable Mettle)：免疫眩晕，Boss减伤+10%。

【阿瑞斯 + 德墨忒尔】冰冻漩涡 (Freezing Vortex)：刀刃裂隙施加冰冻但更小更慢。
【阿瑞斯 + 狄俄尼索斯】恶心诅咒 (Curse of Nausea)：宿醉伤害频率加快(0.5→0.35秒)。
【阿瑞斯 + 波塞冬】溺水诅咒 (Curse of Drowning)：洪水射击变为3次范围脉冲。
【阿瑞斯 + 宙斯】复仇情绪 (Vengeful Mood)：复仇效果自动每3秒触发。

【德墨忒尔 + 狄俄尼索斯】冰酒 (Ice Wine)：投射爆炸产生冰冻迷雾(+30%伤害)。
【德墨忒尔 + 宙斯】冷聚变 (Cold Fusion)：Jolted效果不消失(10秒)。
【德墨忒尔 + 波塞冬】暴风雪射击 (Blizzard Shot)：投射穿透敌人并发射碎片。

【狄俄尼索斯 + 宙斯】璀璨盛宴 (Scintillating Feast)：节日迷雾周期性闪电伤害(60)。
【狄俄尼索斯 + 波塞冬】专属通道 (Exclusive Access)：所有祝福最低史诗品质。最强辅助双人祝福之一。

【波塞冬 + 宙斯】海上风暴 (Sea Storm)：击退同时闪电打击(40伤害)。
"""

# ============================================================
# 传奇祝福知识
# ============================================================
LEGENDARY_KNOWLEDGE = """
=== 12个传奇祝福 (Legendary Boons) ===

宙斯 - 分裂闪电 (Splitting Bolt)：所有闪电额外产生爆发(40伤害)。前置：风暴闪电/双重打击/高压电中选1个。
波塞冬 - 第二波 (Second Wave)：击退延迟后额外推一次。前置：核心祝福+台风之怒/碎浪中选1个。
波塞冬 - 大丰收 (Huge Catch)：钓鱼点出现率+20%。前置：沉没宝藏/海洋恩赐中选2个。
雅典娜 - 神圣保护 (Divine Protection)：屏障每20秒抵消一次伤害。前置：华丽反击。
阿佛洛狄忒 - 不健康迷恋 (Unhealthy Fixation)：虚弱15%几率魅惑4秒。前置：核心祝福+虚弱增强祝福。
阿尔忒弥斯 - 全副武装 (Fully Loaded)：血石+2。前置：支援火力/穴位攻击/出口创伤中选2个。
阿瑞斯 - 恶性循环 (Vicious Cycle)：刀刃裂隙连续命中递增伤害。前置：黑金属或吞噬漩涡。
狄俄尼索斯 - 断片 (Black Out)：宿醉敌人在迷雾中受伤+60%。前置：迷幻射击+宿醉核心。
德墨忒尔 - 冬季丰收 (Winter Harvest)：冰冻敌人在10%生命时碎裂。前置：致命冰冻/贪婪意志/极地爆发中选2个。
赫尔墨斯 - 伟大召回 (Greater Recall)：血石自动返回。前置：连射/快速装填 + Infernal Soul。
赫尔墨斯 - 坏消息 (Bad News)：无血石敌人投射伤害+50%。前置：自动装填 + Stygian Soul。
混沌 - 反抗 (Defiance)：+1死亡抗拒。前置：任意混沌祝福。
"""

# ============================================================
# 常见问题
# ============================================================
FAQ_KNOWLEDGE = """
=== 哈迪斯常见问题 ===

Q: 什么是祝福(Boon)？
A: 祝福是奥林匹斯众神在每次逃脱中给予的临时能力强化。分为攻击、特殊、投射、冲刺、召唤和被动6大类。死亡后所有祝福丢失。

Q: 祝福稀有度等级是什么？
A: 普通(白色)→稀有(蓝色)→史诗(紫色)→英雄(红色)。稀有度越高效果越强。英雄级只能通过特定方式获得(如交换祝福)。

Q: 什么是双人祝福(Duo Boon)？
A: 双人祝福是两位神明合作给予的特殊祝福。需要先拥有每位神明至少1个合格祝福，才有几率在后续房间遇到。共28个。

Q: 什么是传奇祝福(Legendary Boon)？
A: 传奇祝福是单一神明的最强祝福。需要满足特定前置条件才有极低几率出现。共12个。

Q: 如何提高双人祝福出现概率？
A: 1) 夜之镜升级「神之遗产」(Gods' Legacy)天赋；2) 使用特定神明的信物(Keepsake)强制首次遭遇该神明；3) 购买「阿里阿德涅的线球」(Yarn of Ariadne)；4) 欧律狄刻的「清爽甘露」(Refreshing Nectar)。

Q: 什么是状态诅咒(Status Curse)？
A: 每位神明有专属的负面状态效果，如宙斯的Jolted、阿瑞斯的Doom、阿佛洛狄忒的Weak等。镜之天赋「特权地位」(Privileged Status)在敌人受2种状态诅咒时增加你的伤害。

Q: 什么是血石(Bloodstone/Cast Ammo)？
A: 投射弹药用的小型宝石。初始为1颗（Stygian Soul）或3颗掉落型（Infernal Soul），嵌入敌人后需等待掉落或敌人死亡回收。

Q: 如何解锁隐藏武器形态？
A: 1) 购买命运清单；2) 至少投资5个泰坦之血到非扎格列欧斯形态；3) 与阿喀琉斯交谈解锁关羽形态(首个隐藏)；4) 投资5泰坦之血到目标武器；5) 与对应NPC交谈：剑→倪克斯、弓→阿尔忒弥斯、盾→混沌、拳→阿斯忒里俄斯、炮→宙斯。

Q: 雅典娜和阿瑞斯的「仁慈终结」怎么用？
A: 这是最强combo双人祝福之一。需要雅典娜的偏转能力（神圣打击或神圣绽放）+ 阿瑞斯的毁灭效果（痛苦诅咒或疼痛诅咒）。偏转攻击命中后立即触发毁灭的爆发伤害(40点)，不需要等毁灭的延迟。
"""

# ============================================================
# 所有知识文档列表
# ============================================================
KNOWLEDGE_DOCS = [
    {"title": "游戏概述", "content": "哈迪斯(Hades)是Supergiant Games开发的Roguelike动作游戏。玩家扮演冥界王子扎格列欧斯，在奥林匹斯众神的帮助下尝试逃离冥界。祝福(Boons)是众神给予的临时能力强化，分为攻击、特殊、投射、冲刺、召唤和被动。死亡后祝福全部丢失。稀有度：普通<稀有<史诗<英雄。双人祝福需两个神明的祝福触发，传奇祝福需满足前置条件。"},
    {"title": "武器总览", "content": WEAPONS_KNOWLEDGE},
    {"title": "双人祝福", "content": DUO_BOONS_KNOWLEDGE},
    {"title": "传奇祝福", "content": LEGENDARY_KNOWLEDGE},
    {"title": "常见问题", "content": FAQ_KNOWLEDGE},
]

# 为每位神明创建独立文档
for god_id, god_data in GODS.items():
    KNOWLEDGE_DOCS.append({
        "title": f"{god_data['icon']} {god_data['name']} ({god_data['name_en']})",
        "content": f"""{god_data['desc']}
状态诅咒：{god_data['status']}
信物：{god_data['keepsake']}
打法风格：{god_data['playstyle']}
"""
    })


def search_knowledge(query: str, top_k: int = 3) -> list[dict]:
    """简单关键词匹配检索，返回最相关的知识文档"""
    query_lower = query.lower()
    scored = []

    # 提取中文 n-gram（2-4字词组）用于中文搜索
    cn_ngrams = set()
    for n in [2, 3, 4]:
        for i in range(len(query) - n + 1):
            chunk = query[i:i+n]
            # 只保留纯中文词组
            if all('\u4e00' <= c <= '\u9fff' for c in chunk):
                cn_ngrams.add(chunk)

    for doc in KNOWLEDGE_DOCS:
        content_lower = doc["content"].lower()
        title_lower = doc["title"].lower()
        score = 0

        # 英文空格分词
        keywords = query_lower.split()
        for kw in keywords:
            score += content_lower.count(kw) * 2
            score += title_lower.count(kw) * 5

        # 中文 n-gram 匹配
        for ng in cn_ngrams:
            count_in_content = content_lower.count(ng.lower())
            count_in_title = title_lower.count(ng.lower())
            if count_in_content > 0 or count_in_title > 0:
                # 词组越长权重越高
                weight = len(ng)
                score += count_in_content * weight * 3
                score += count_in_title * weight * 8

        # 中文特殊关键词映射（神明名、游戏术语等）
        cn_keywords = {
            "宙斯": "zeus", "波塞冬": "poseidon", "雅典娜": "athena",
            "阿瑞斯": "ares", "阿佛洛狄忒": "aphrodite", "阿尔忒弥斯": "artemis",
            "德墨忒尔": "demeter", "狄俄尼索斯": "dionysus", "赫尔墨斯": "hermes",
            "混沌": "chaos",
            "双人": "duo", "双重": "duo", "传奇": "legendary",
            "武器": "weapon", "形态": "aspect", "隐藏": "hidden",
            "暴击": "critical", "虚弱": "weak", "冰冻": "chill",
            "宿醉": "hangover", "毁灭": "doom", "闪电": "lightning",
            "击退": "knockback", "偏转": "deflect",
            "祝福": "boon", "血石": "bloodstone",
        }
        for cn, en in cn_keywords.items():
            if cn in query:
                score += content_lower.count(en) * 3
                score += title_lower.count(en) * 5

        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    for score, doc in scored[:top_k]:
        content = doc["content"]
        if len(content) > 1200:
            content = content[:1200] + "\n...（内容过长已截断）"
        results.append({
            "title": doc["title"],
            "content": content,
            "score": score
        })

    return results


def build_context(query: str, top_k: int = 3) -> str:
    """构建注入AI的上下文文本"""
    docs = search_knowledge(query, top_k)
    if not docs:
        return ""

    parts = ["以下是哈迪斯游戏中与用户问题相关的知识：\n"]
    for i, doc in enumerate(docs, 1):
        parts.append(f"【知识{i}】{doc['title']}\n{doc['content']}\n")
    return "\n".join(parts)


# 预设所有神明祝福的快速参考数据（从JS数据移植）
BOONS_REFERENCE = {
    "zeus": [
        ("闪电打击", "Lightning Strike", "攻击", "攻击释放链式闪电在敌人间弹射(最多4次弹跳)"),
        ("雷霆绽放", "Thunder Flourish", "特殊", "特殊攻击使闪电打击附近敌人"),
        ("电击射击", "Electric Shot", "投射", "投射变为链式闪电弹射"),
        ("雷霆冲刺", "Thunder Dash", "冲刺", "冲刺使闪电打击附近敌人"),
        ("宙斯之助", "Zeus' Aid", "召唤", "闪电快速打击附近敌人1.5秒"),
        ("天罚", "Heaven's Vengeance", "被动", "受伤后敌人被闪电打击"),
        ("闪电反射", "Lightning Reflexes", "被动", "在被击中前冲刺触发闪电"),
        ("风暴闪电", "Storm Lightning", "被动", "链式闪电弹射次数增加"),
        ("高压电", "High Voltage", "被动", "闪电效果范围更大"),
        ("双重打击", "Double Strike", "被动", "闪电有25%几率打击两次"),
        ("静电释放", "Static Discharge", "被动", "闪电效果使敌人Jolted(攻击时自伤)"),
        ("汹涌之力", "Billowing Strength", "被动", "使用Call后15秒内伤害增加"),
        ("云遮审判", "Clouded Judgment", "被动", "造成或受伤害时神圣计量表充能更快"),
        ("分裂闪电", "Splitting Bolt", "传奇", "所有闪电效果额外产生伤害爆发(40)"),
    ],
    "poseidon": [
        ("风暴打击", "Tempest Strike", "攻击", "攻击伤害+30%并击退敌人"),
        ("风暴绽放", "Tempest Flourish", "特殊", "特殊伤害+70%并击退敌人"),
        ("洪水射击", "Flood Shot", "投射", "投射造成范围伤害并击退敌人"),
        ("潮汐冲刺", "Tidal Dash", "冲刺", "冲刺造成范围伤害并击退敌人"),
        ("波塞冬之助", "Poseidon's Aid", "召唤", "无敌冲撞敌人1.2秒(冲击伤害250)"),
        ("液压之力", "Hydraulic Might", "被动", "每次遭遇前5秒攻击和特殊更强(+50%)"),
        ("台风之怒", "Typhoon's Fury", "被动", "撞墙伤害+200%"),
        ("碎浪", "Breaking Wave", "被动", "撞墙产生水波爆炸(100伤害)"),
        ("巨浪拍打", "Wave Pounding", "被动", "击退对Boss伤害+20%"),
        ("锋利浅滩", "Razor Shoals", "被动", "击退同时使敌人Rupture(移动时持续受伤)"),
        ("沉没宝藏", "Sunken Treasure", "被动", "获得随机资源和生命"),
        ("海洋恩赐", "Ocean's Bounty", "被动", "黑暗/宝石/金币奖励+50%"),
        ("第二波", "Second Wave", "传奇", "击退效果延迟后额外推一次"),
        ("大丰收", "Huge Catch", "传奇", "钓鱼点出现率+20%"),
    ],
    "athena": [
        ("神圣打击", "Divine Strike", "攻击", "攻击伤害+40%并可偏转弹幕"),
        ("神圣绽放", "Divine Flourish", "特殊", "特殊伤害+60%并可偏转弹幕"),
        ("方阵射击", "Phalanx Shot", "投射", "投射造成范围伤害并可偏转"),
        ("神圣冲刺", "Divine Dash", "冲刺", "冲刺造成伤害并可偏转"),
        ("雅典娜之助", "Athena's Aid", "召唤", "短暂无敌并偏转所有攻击(1.5秒)"),
        ("神圣护盾", "Holy Shield", "被动", "受伤后伤害周围敌人并短暂偏转"),
        ("铜皮铁骨", "Bronze Skin", "被动", "减少来自敌人的伤害(-5%)"),
        ("致盲闪光", "Blinding Flash", "被动", "偏转能力同时使敌人Exposed(背刺+50%)"),
        ("华丽反击", "Brilliant Riposte", "被动", "偏转攻击时造成更多伤害(+80%)"),
        ("不死之身", "Deathless Stand", "被动", "死亡抗拒使你无敌更久"),
        ("最后抵抗", "Last Stand", "被动", "死亡抗拒恢复更多生命"),
        ("神圣保护", "Divine Protection", "传奇", "屏障每20秒抵消一次伤害"),
    ],
    "ares": [
        ("痛苦诅咒", "Curse of Agony", "攻击", "攻击施加毁灭效果(50伤害)"),
        ("疼痛诅咒", "Curse of Pain", "特殊", "特殊施加毁灭效果(60伤害)"),
        ("切割射击", "Slicing Shot", "投射", "投射变为向前飞行的刀刃裂隙"),
        ("刀刃冲刺", "Blade Dash", "冲刺", "冲刺起点创建刀刃裂隙"),
        ("阿瑞斯之助", "Ares' Aid", "召唤", "变为无敌刀刃裂隙1.2秒"),
        ("复仇诅咒", "Curse of Vengeance", "被动", "受伤后对周围敌人施加毁灭"),
        ("杀戮冲动", "Urge to Kill", "被动", "攻击/特殊/投射伤害+10%"),
        ("战斗狂怒", "Battle Rage", "被动", "击杀后下次攻击/特殊伤害+100%~250%"),
        ("黑金属", "Black Metal", "被动", "刀刃裂隙范围+20%"),
        ("吞噬漩涡", "Engulfing Vortex", "被动", "刀刃裂隙持续更久并吸引敌人"),
        ("厄运临头", "Dire Misfortune", "被动", "毁灭多次施加时伤害更高"),
        ("末日将至", "Impending Doom", "被动", "毁灭伤害+60%但延迟+0.5秒"),
        ("恶性循环", "Vicious Cycle", "传奇", "刀刃裂隙连续命中伤害递增+2/次"),
    ],
    "aphrodite": [
        ("心碎打击", "Heartbreak Strike", "攻击", "攻击伤害+50%并施加虚弱"),
        ("心碎绽放", "Heartbreak Flourish", "特殊", "特殊伤害+80%并施加虚弱"),
        ("粉碎射击", "Crush Shot", "投射", "短距离大范围爆炸投射并施加虚弱"),
        ("热情冲刺", "Passion Dash", "冲刺", "冲刺终点伤害并施加虚弱"),
        ("阿佛洛狄忒之助", "Aphrodite's Aid", "召唤", "发射追踪弹施加魅惑(5秒，Boss 2.5秒)"),
        ("临终哀叹", "Dying Lament", "被动", "敌人死亡时伤害附近敌人并施加虚弱"),
        ("绝望之波", "Wave of Despair", "被动", "受伤后伤害周围敌人并施加虚弱"),
        ("内心空虚", "Empty Inside", "被动", "虚弱持续+5秒"),
        ("甜蜜屈服", "Sweet Surrender", "被动", "虚弱状态的敌人受到更多伤害(+10%)"),
        ("破碎决心", "Broken Resolve", "被动", "虚弱效果更强(可叠至-47%伤害)"),
        ("生命肯定", "Life Affirmation", "被动", "生命房间奖励+30%"),
        ("不同凡响", "Different League", "被动", "附近敌人伤害-10%"),
        ("不健康迷恋", "Unhealthy Fixation", "传奇", "虚弱15%几率魅惑敌人4秒"),
    ],
    "artemis": [
        ("致命打击", "Deadly Strike", "攻击", "攻击伤害+20%/+15%暴击"),
        ("致命绽放", "Deadly Flourish", "特殊", "特殊伤害+40%/+20%暴击"),
        ("真实射击", "True Shot", "投射", "投射追踪敌人/+10%暴击"),
        ("猎人冲刺", "Hunter Dash", "冲刺", "冲刺攻击伤害+50%~125%"),
        ("阿尔忒弥斯之助", "Artemis' Aid", "召唤", "发射追踪箭/+35%暴击"),
        ("穴位攻击", "Pressure Points", "被动", "所有伤害+3%~6%暴击几率"),
        ("出口创伤", "Exit Wounds", "被动", "血石被弹出时造成100伤害"),
        ("干净击杀", "Clean Kill", "被动", "暴击伤害+15%~37.5%"),
        ("支援火力", "Support Fire", "被动", "攻击/特殊/投射后发射追踪箭(10~16伤害)"),
        ("破甲者", "Hide Breaker", "被动", "暴击对护甲伤害+200%"),
        ("猎人本能", "Hunter Instinct", "被动", "暴击时神圣计量表充能"),
        ("猎人标记", "Hunter's Mark", "被动", "暴击后标记附近敌人(被标记者+30%暴击率)"),
        ("全副武装", "Fully Loaded", "传奇", "血石+2"),
    ],
    "demeter": [
        ("冰霜打击", "Frost Strike", "攻击", "攻击伤害+40%并施加冰冻"),
        ("冰霜绽放", "Frost Flourish", "特殊", "特殊伤害+60%并施加冰冻"),
        ("水晶光束", "Crystal Beam", "投射", "投射为水晶向敌人发射光束5秒"),
        ("寒风冲刺", "Mistral Dash", "冲刺", "冲刺前方释放寒风并施加冰冻"),
        ("德墨忒尔之助", "Demeter's Aid", "召唤", "创建冬季漩涡冰冻敌人5秒"),
        ("雪花爆发", "Snow Burst", "被动", "每次投射伤害周围敌人并冰冻"),
        ("冰霜触碰", "Frozen Touch", "被动", "受伤后完全冰冻周围敌人"),
        ("稀有作物", "Rare Crop", "被动", "祝福降为普通品质，每3次遭遇提升品质"),
        ("冰川凝视", "Glacial Glare", "被动", "水晶光束持续更久并施加冰冻"),
        ("极地爆发", "Arctic Blast", "被动", "10层冰冻引发爆炸(80伤害)"),
        ("致命冰冻", "Killing Freeze", "被动", "所有敌人被冰冻时减速并Decay持续掉血"),
        ("贪婪意志", "Ravenous Will", "被动", "无血石时减伤+10%并增伤+10%"),
        ("冬季丰收", "Winter Harvest", "传奇", "冰冻敌人在10%生命时碎裂(50伤害)"),
    ],
    "dionysus": [
        ("醉意打击", "Drunken Strike", "攻击", "攻击施加宿醉(4伤害/0.5秒)"),
        ("醉意绽放", "Drunken Flourish", "特殊", "特殊施加宿醉(5伤害/0.5秒)"),
        ("迷幻射击", "Trippy Shot", "投射", "投射为大型爆炸产生节日迷雾(Stun敌人)"),
        ("醉意冲刺", "Drunken Dash", "冲刺", "冲刺起点多次施加宿醉"),
        ("狄俄尼索斯之助", "Dionysus' Aid", "召唤", "对周围敌人施加宿醉1.5秒(15伤害/0.5秒)"),
        ("上等佳酿", "Premium Vintage", "被动", "拾取甘露时+20最大生命"),
        ("余兴派对", "After Party", "被动", "遭遇后生命低于30%时恢复到阈值"),
        ("烈酒", "Strong Drink", "被动", "泉水满恢复+每泉+3%伤害"),
        ("高耐受力", "High Tolerance", "被动", "站在迷雾中减伤+14%"),
        ("坏影响", "Bad Influence", "被动", "3+敌人宿醉时伤害+50%"),
        ("麻木感", "Numbing Sensation", "被动", "宿醉同时使敌人减速15%"),
        ("同侪压力", "Peer Pressure", "被动", "宿醉敌人每4秒传染附近敌人"),
        ("断片", "Black Out", "传奇", "宿醉敌人在迷雾中受伤+60%"),
    ],
    "hermes": [
        ("迅捷打击", "Swift Strike", "被动", "攻击速度+10%~30%"),
        ("迅捷绽放", "Swift Flourish", "被动", "特殊攻击速度+10%~30%"),
        ("极速", "Greater Haste", "被动", "移动速度+20%~40%"),
        ("最强反射", "Greatest Reflex", "被动", "额外+1~4次冲刺次数"),
        ("闪避大师", "Greater Evasion", "被动", "被击中时10%~20%几率自动闪避"),
        ("快速装填", "Quick Reload", "被动", "血石掉落更快(需Infernal Soul)"),
        ("自动装填", "Auto Reload", "被动", "血石自动再生(需Stygian Soul)"),
        ("连射", "Flurry Cast", "被动", "按住投射连续发射(需Infernal Soul)"),
        ("超级冲刺", "Hyper Sprint", "被动", "冲刺后短暂坚毅+100%移速(0.5秒)"),
        ("快速投递", "Rush Delivery", "被动", "额外移速50%转化为伤害"),
        ("快速恢复", "Quick Recovery", "被动", "受伤后冲刺恢复30%损失生命"),
        ("副业", "Side Hustle", "被动", "每进入房间+100金币"),
        ("第二口气", "Second Wind", "被动", "Call后10秒闪避+30%移速+30%"),
        ("伟大召回", "Greater Recall", "传奇", "血石自动返回"),
        ("坏消息", "Bad News", "传奇", "无血石敌人投射伤害+50%"),
    ],
}
