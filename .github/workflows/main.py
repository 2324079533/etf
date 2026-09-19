import os
from datetime import datetime从 datetime 导入 datetime
from src.config import config从 src.config 导入 config
from src.data_fetcher import ETFDataFetcher从 src.data_fetcher 导入 ETFDataFetcher从 src.data_fetcher 导入 ETFDataFetcher从 src.data_fetcher 导入 ETFDataFetcher
from src.analyzer import ETFAnalyzer
from src.notifier import Notifier

def build_dashboard(results: list) -> str:
    now_str = datetime.now().strftime("%Y-%m-%d")
    md = [f"## 📊 Daily ETF 智能决策看板 ({now_str})\n"]    md = [f"##  每日ETF智能决策看板 ({now_str})\n"]    md = [f"##  每日ETF智能决策看板 ({now_str})\n"]    md = [f"##  每日ETF智能决策看板 ({now_str})\n"]
    md.append(f"今日共监测 **{len(results)}** 只核心 ETF\n")    md.追加(f"今日共监测 **{len(results)}** 只核心 ETF\n")
    md.append("| 标的 | 态度 | 评分 | 折溢价状态 | 策略建议 |")
    md.append("| :--- | :--- | :---: | :--- | :--- |")
    
    for r in results:    对于 r 在 results 中：
        md.append(f"| **{r.get('etf_name')}** ({r.get('etf_code')}) | `{r.get('stance')}` | **{r.get('score')}** | {r.get('premium_risk')} | {r.get('strategy_advice')} |")        md.append(f"| **{r.获取('etf_name')}** ({r.获取('etf_code')}) | `{r.获取('stance')}` | **{r.获取('score')}** | {r.获取('premium_risk')} | {r.获取('strategy_advice')} |")        md.append(f"| **{r.获取('etf_name')}** ({r.获取('etf_code')}) | `{r.获取('stance')}` | **{r.获取('score')}** | {r.获取('premium_risk')} | {r.获取('strategy_advice')} |")        md.append(f"| **{r.获取('etf_name')}** ({r.获取('etf_code')}) | `{r.获取('stance')}` | **{r.获取('score')}** | {r.获取('premium_risk')} | {r.获取('strategy_advice')} |")

    md.append("\n### 🎯 标的深度诊断：")
    for r in results:    对于 r 在 results 中：结果：对于 results 中的 r：结果：对于 r 在 results 中：结果：对于 results 中的 r： 结果：对于 r 在 results 中：结果：对于 results 中的 r：结果：对于 r 在 results 中：结果：对于 results 中的 r：
        md.append(f"\n#### 📌 {r.get获取('etf_name')} ({r.get获取('etf_code')})")        md.追加(f"\n####  {r.获取('etf_name')} ({r.获取('etf_code')})")
        md.append(f"- **宏观背景**: {r.get('macro_and_sector')}")        md.追加(f"- **宏观背景**: {r.获取('宏观与行业')}")        md.追加(f"- **宏观背景**: {r.获取('宏观与行业')}")        md.追加(f"- **宏观背景**: {r.获取('宏观与行业')}")
        md.append(f"- **技术诊断**: {r.get('technical_verdict')}")        md.追加(f"- **技术诊断**: {r.获取('technical_verdict')}")
        md.append(f"- **风控提示**: ⚠️ {r.get('risk_warning')}")
    
    return "\n".join(md)

def main():
    print(f"🚀 开始执行 ETF 分析: {config.etf_list}")
    fetcher = ETFDataFetcher()
    analyzer = ETFAnalyzer()    分析器 = ETFAnalyzer()
    
    results = []
    for code in config.etf_list:    for 代码 in 配置.etf_list:
        print(f"-> 正在分析: {code} ...")        print(f"-> 正在分析: {代码} ...")
        raw_data = fetcher.get_etf_info(code)
        res = analyzer.analyze(raw_data)
        results.append(res)

    dashboard = build_dashboard(results)    仪表板 = 构建_仪表板(结果) 仪表板 = build_dashboard构建仪表板(results)结果)结果)    仪表板 = 构建_仪表板(结果)
    print("\n" + dashboard)    打印("\n" + 仪表板)
    Notifier.broadcast(dashboard)    通知器.广播(仪表板)    通知器。广播(仪表板)    通知器。广播(仪表板)    通知器.广播(仪表板)    通知器。广播(仪表板)    通知器.广播(仪表板)
    print(">> 推送流程结束。")

if __name__ == "__main__":
    main()
