"""报告格式化辅助模块。"""
from datetime import datetime
from typing import Dict, Any


def format_datetime(dt_str: str) -> str:
    """格式化 ISO 时间为易读格式。"""
    
    if not dt_str:
        return "未知时间"
    
    try:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return dt_str


def format_duration(start: str, end: str) -> str:
    """计算并格式化持续时间。"""
    
    if not start or not end:
        return "未知"
    
    try:
        start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
        
        delta = end_dt - start_dt
        
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        
        if hours > 0:
            return f"{hours}小时{minutes}分钟"
        
        return f"{minutes}分钟"
    except Exception:
        return "未知"


def escape_markdown(text: str) -> str:
    """转义 Markdown 特殊字符。"""
    
    special_chars = ['`', '*', '_', '#', '[', ']', '<', '>', '|']
    
    for char in special_chars:
        text = text.replace(char, f'\\{char}')
    
    return text


def truncate_text(text: str, max_length: int = 500) -> str:
    """截断文本并添加省略号。"""
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length] + "...(已截断)"


def format_runner_info(runner_name: str, runner_group: str) -> str:
    """格式化 Runner 信息。"""
    
    chip_type = detect_chip_type(runner_name)
    card_count = detect_card_count(runner_name)
    
    parts = [chip_type]
    
    if card_count:
        parts.append(f"{card_count}卡")
    
    if runner_group:
        parts.append(f"({runner_group})")
    
    return " ".join(parts)


def detect_chip_type(runner_name: str) -> str:
    """根据 Runner 名称检测芯片类型。"""
    
    if "a2b3" in runner_name.lower():
        return "Ascend 910B"
    if "a3" in runner_name.lower():
        return "Ascend 910C"
    if "310p" in runner_name.lower():
        return "Ascend 310P"
    
    return "未知芯片"


def detect_card_count(runner_name: str) -> int | None:
    """根据 Runner 名称检测卡数。"""
    
    import re
    
    patterns = [
        (r"-2$", 2),
        (r"-4$", 4),
        (r"-1$", 1),
        (r"single", 1)
    ]
    
    for pattern, count in patterns:
        if re.search(pattern, runner_name):
            return count
    
    return None