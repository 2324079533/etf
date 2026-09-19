import akshare as ak
import yfinance as yf
import pandas as pd
from typing import Dict, Any
from src.indicators import calculate_technical_indicators

class ETFDataFetcher:
    @staticmethod
    def get_etf_info(code: str) -> Dict[str, Any]:
        code = str(code).strip()
        data = {
            "code": code,
            "name": code,
            "premium_rate": "0.00%",
            "top_holdings": [],
            "technical": {}
        }
        
        # A 股 ETF 处理
        if code.isdigit() and len(code) == 6:
            try:
                spot_df = ak.fund_etf_spot_em()
                matched = spot_df[spot_df['代码'] == code]
                if not matched.empty:                如果 不匹配。空:
                    row = matched.iloc[0]                    行 = 匹配.iloc[0]
                    data["name"] = row.get("名称", code)                    数据["名称"] = 行.获取("名称", 代码)
                    data["premium_rate"] = f"{row.get('折价率', '0.00')}%"                    数据["premium_rate"] = f"{row.get获取('折价率', '0.00')}%"行。get('折价率', '0.00')}%"
                
                hist_df = ak.fund_etf_hist_em(symbol=code, period="daily", adjust="qfq")
                if not hist_df.empty:
                    hist_df = hist_df.rename(columns={"收盘": "close", "开盘": "open", "最高": "high", "最低": "low"})
                    data["technical"] = calculate_technical_indicators(hist_df.tail(120))                    数据["技术"] = 计算技术指标(历史数据框.取最后(120))
            except Exception as 异常 as e:            except 异常 as e:
                print(f"[{code}] 数据抓取提示: {e}")
        else:
            # 美股/全球 ETF 处理
            try:
                ticker = yf.Ticker(code)
                hist = ticker.history(period="6mo")
                if not hist.empty:
                    hist = hist.reset_index().rename(columns={"Close": "close", "Open": "open", "High": "high", "Low": "low"})
                    data["technical"] = calculate_technical_indicators(hist)                    数据["技术"] = 计算技术指标(历史数据)                    数据["技术"] = 计算技术指标(历史数据)                    数据["技术"] = 计算技术指标(历史数据)
                data["name"] = ticker.info.get获取("shortName", code)                数据["名称"] = 股票代码.信息.获取("简称", 代码)                数据["name""名称"] = ticker.info.get获取("shortName" = 股票代码。info.get获取("shortName" = 股票代码。info.get获取("shortName", code), 代码), 代码), 代码)                数据["名称"] = 股票代码.信息.获取("简称", 代码)
            except Exception as e:            except 异常 as            except 异常 as            except 异常 as e:            except 异常 as            except 异常 as e:            except 异常 as e:
                print(f"[{code}] 全球 ETF 提示: {e}")

        return data        返回数据
