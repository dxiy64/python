# -*- coding: utf-8 -*-
# ============================================
# mybook/__init__.py · 包的"门面"
# 空着也能用；写内容是为了让外面少打几个字
# ============================================
from .book import ContactBook        # 让 from mybook import ContactBook 直接可用
from .storage import PATH            # 顺手把数据文件路径也出口出去

__all__ = ["ContactBook", "PATH"]    # 声明"本包的公开出口"，from mybook import * 时只给这些

__version__ = "1.0"
