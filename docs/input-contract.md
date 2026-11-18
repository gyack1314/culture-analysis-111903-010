# 合成分析资料契约

所有机构、企业、受访者、交易和事件均为本地合成，不来自新闻所涉真实主体，不声称新闻发生过这些分析问题。

seed.json与同名Parquet是相同原始值的两种载体；actions.json列尚未应用的后续输入动作。inventory.json只记录原件物理摘要和行数，不提供分析结论。时间均含时区或明确日期，金钱字段minor以CNY分计，空值保留未知含义。已有代码只做物理完整性检查，没有估计、预测、方案求解或产品发布功能。

linked_events只含获准的合成anon_id，consent_scope是可连接范围，不对未关联者分配新身份。marginals给set/count/value/period/universe/unit/source，set为渠道集合交集，不是并集；count_kind=period_unique或daily_unique不可直接混用。unknown交集未提供，不代表0。universe必须同地域/年龄/期间且unit=persons才允许同总体推断。audit_pairs的same/different/unresolved仅作用于明确样本，不能外推确定身份。model_assumptions是供敏感性比较的渠道依赖范围，不是已证实独立。plans给渠道组合、成本及相同目标总体；人数可行边界须同时满足所有采用的边际和交集。不会提供真实全体人群，只能用支持的证据与假设解释识别程度。

共七个渠道A至G，部分两方与三方交集已有审计值，其他交集未知。linked_events只覆盖部分已授权来源，不是其余渠道没人。组合比较应在同一联合可行人群中计算覆盖与边际增量，不把不同极值情景中各自最乐观数字拼成一份方案。初始边际具有共同可行解释，但没有提供真实原子人群、真实总体或独立性答案；后续动作的冲突需由实现核对定位。
