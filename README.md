# 多入口客流的重叠触达与覆盖推断

本项目提供文化展会场景的本地合成原始资料与物理检查，统计分析应用尚未实现。输入能读取不表示业务记录有效或某个结论成立；没有预生成权重、预测、估计、推荐或最优方案。

Python版本为3.11，requirements.txt固定分析依赖。可运行 python -m pip install -r requirements.txt 安装；python -m materials inputs 校验原件大小、SHA-256及Parquet物理行数，并实际经DuckDB读取。python -m unittest discover -s tests -v 检查两种输入载体的值、原件损坏拒绝与本项目资料引用关系。

容器用法：docker build -t culture-inputs .，再运行 docker run --rm culture-inputs；输入测试用 docker run --rm culture-inputs python -m unittest discover -s tests -v。资料检查不需要网络或外部业务账号。

inputs/seed.json与同名Parquet保存原始值，其他JSON保存已有设计、请求和资源背景，docs/input-contract.md解释语义。后续动作在inputs/actions.json，尚未处理。materials.build_inputs只重建原始Parquet与物理清单，通常无需再次运行；它不计算任何目标分析。统计与建模依赖已提供，方法与产品接口待实现选择。

原件保留供追查，产品结果另存独立目录。实现后再补充实际分析入口、适用假设、结果查询和业务验证说明；现有输入测试不能替代这些功能验收。
