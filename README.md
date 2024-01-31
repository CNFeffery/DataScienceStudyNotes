# :memo: DataScienceStudyNotes
:dart: 这个仓库保管从（数据科学学习手札69）开始的所有代码、数据等相关附件内容
<br>:email: 交流学习请联系邮箱：fefferypzy@gmail.com
<br>:rainbow: 博客地址：https://www.cnblogs.com/feffery/

> :inbox_tray: 国内镜像加速clone方式：
```bash
git clone https://gitee.com/cnfeffery/DataScienceStudyNotes.git
```

# :carousel_horse: 目录
- :books: [1 已更新博客列表](#first)
- :card_file_box: [2 专题系列](#second)
  - :earth_asia: [2.1 基于geopandas的空间数据分析  🏊 `<持续更新中>`](#second-geopandas)
  - :zap: [2.2 Python+Dash快速web应用开发  🚩 `<完结>` ](#second-dash)
- :man_astronaut: [3 pandas相关](#pandas)
- :ghost: [4 jupyter相关](#jupyter)
- :penguin: [5 kepler.gl相关](#keplergl)

***

<a name="first"></a>

## 1 :books: 已更新博客列表：
- [（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg](https://www.cnblogs.com/feffery/p/11468762.html) 　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg)
- [（数据科学学习手札70）面向数据科学的Python多进程简介及应用](https://www.cnblogs.com/feffery/p/11621076.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札70）面向数据科学的Python多进程简介及应用)
- [（数据科学学习手札71）利用Python绘制词云图](https://www.cnblogs.com/feffery/p/11842798.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札71）在Python中制作个性化词云图)
- [（数据科学学习手札72）用pdpipe搭建pandas数据分析流水线](https://www.cnblogs.com/feffery/p/12179647.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札72）用pdpipe搭建pandas数据分析流水线)
- [（数据科学学习手札73）盘点pandas 1.0.0中的新特性](https://www.cnblogs.com/feffery/p/12214635.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD73%EF%BC%89%E7%9B%98%E7%82%B9pandas%201.0.0%E4%B8%AD%E7%9A%84%E6%96%B0%E7%89%B9%E6%80%A7)
- [（数据科学学习手札74）基于geopandas的空间数据分析——数据结构篇](https://www.cnblogs.com/feffery/p/11898190.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札74）基于geopandas的空间数据分析——数据结构篇)
- [（数据科学学习手札75）基于geopandas的空间数据分析——坐标参考系篇](https://www.cnblogs.com/feffery/p/12285828.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札75）基于geopandas的空间数据分析——坐标参考系篇)
- [（数据科学学习手札76）基于Python的拐点检测——以新冠肺炎疫情数据为例](https://www.cnblogs.com/feffery/p/12325741.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札76）基于Python的拐点检测——以新冠肺炎疫情数据为例)
- [（数据科学学习手札77）基于geopandas的空间数据分析——文件IO](https://www.cnblogs.com/feffery/p/12301966.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札77）基于geopandas的空间数据分析——文件IO)
- [（数据科学学习手札78）基于geopandas的空间数据分析——基础可视化](https://www.cnblogs.com/feffery/p/12361421.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札78）基于geopandas的空间数据分析——基础可视化)
- [（数据科学学习手札79）基于geopandas的空间数据分析——深入浅出分层设色](https://www.cnblogs.com/feffery/p/12381322.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札79）基于geopandas的空间数据分析——深入浅出分层设色)
- [（数据科学学习手札80）用Python编写小工具下载OSM路网数据](https://www.cnblogs.com/feffery/p/12483967.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札80）用Python编写小工具下载OSM路网数据)
- [（数据科学学习手札81）conda+jupyter玩转数据科学环境搭建](https://www.cnblogs.com/feffery/p/12609118.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札81）conda+jupyter玩转数据科学环境搭建)
- [（数据科学学习手札82）基于geopandas的空间数据分析——geoplot篇(上)](https://www.cnblogs.com/feffery/p/12779150.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札82）基于geopandas的空间数据分析——geoplot篇(上))
- [（数据科学学习手札83）基于geopandas的空间数据分析——geoplot篇(下)](https://www.cnblogs.com/feffery/p/12901334.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札83）基于geopandas的空间数据分析——geoplot篇(下))
- [（数据科学学习手札84）基于geopandas的空间数据分析——空间计算篇（上）](https://www.cnblogs.com/feffery/p/12909284.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札84）基于geopandas的空间数据分析——空间计算篇（上）)
- [（数据科学学习手札85）Python+Kepler.gl轻松制作酷炫路径动画](https://www.cnblogs.com/feffery/p/12987968.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札85）Python+Kepler.gl轻松制作酷炫路径动画)
- [（数据科学学习手札86）全平台支持的pandas运算加速神器](https://www.cnblogs.com/feffery/p/13049547.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札86）全平台支持的pandas运算加速神器)
- [（数据科学学习手札87）利用adjustText解决matplotlib文字标签遮挡问题](https://www.cnblogs.com/feffery/p/13072364.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札87）利用adjustText解决matplotlib文字标签遮挡问题)
- [（数据科学学习手札88）基于geopandas的空间数据分析——空间计算篇（下）](https://www.cnblogs.com/feffery/p/13129271.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札88）基于geopandas的空间数据分析——空间计算篇（下）)
- [（数据科学学习手札89）geopandas&geoplot近期重要更新](https://www.cnblogs.com/feffery/p/13233271.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札89）geopandas&geoplot近期重要更新)
- [（数据科学学习手札90）Python+Kepler.gl轻松制作时间轮播地图](https://www.cnblogs.com/feffery/p/13322067.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札90）Python+Kepler.gl轻松制作时间轮播地图)
- [（数据科学学习手札91）在Python中妥善使用进度条](https://www.cnblogs.com/feffery/p/13392024.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札91）在Python中妥善使用进度条)
- [（数据科学学习手札92）利用query()与eval()优化pandas代码](https://www.cnblogs.com/feffery/p/13440148.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札92）利用query()与eval()优化pandas代码)
- [（数据科学学习手札93）利用geopandas与PostGIS进行交互](https://www.cnblogs.com/feffery/p/13468203.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札93）利用geopandas与PostGIS进行交互)
- [（数据科学学习手札94）QGIS+Conda+jupyter玩转Python GIS](https://www.cnblogs.com/feffery/p/13558608.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD94%EF%BC%89QGIS%2BConda%2Bjupyter%E7%8E%A9%E8%BD%ACPython%20GIS)
- [（数据科学学习手札95）elyra——jupyter lab平台最强插件集](https://www.cnblogs.com/feffery/p/13692800.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD95%EF%BC%89elyra%E2%80%94%E2%80%94jupyter%20lab%E5%B9%B3%E5%8F%B0%E6%9C%80%E5%BC%BA%E6%8F%92%E4%BB%B6%E9%9B%86)
- [（数据科学学习手札96）在geopandas中叠加在线地图](https://www.cnblogs.com/feffery/p/13763601.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札96）在geopandas中叠加在线地图)
- [（数据科学学习手札97）掌握pandas中的transform](https://www.cnblogs.com/feffery/p/13816362.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札97）掌握pandas中的transform)
- [（数据科学学习手札98）纯Python绘制满满艺术感的山脊地图](https://www.cnblogs.com/feffery/p/13977871.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札98）纯Python绘制满满艺术感的山脊地图)
- [（数据科学学习手札99）掌握pandas中的时序数据分组运算](https://www.cnblogs.com/feffery/p/14093478.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札99）掌握pandas中的时序数据分组运算)
- [（数据科学学习手札100）搞定matplotlib中的字体设置](https://www.cnblogs.com/feffery/p/14122415.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札100）搞定matplotlib中的字体设置)
- [（数据科学学习手札101）funcy：Python中的函数式编程百宝箱](https://www.cnblogs.com/feffery/p/14208030.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札101）funcy：Python中的函数式编程百宝箱)
- [（数据科学学习手札102）Python+Dash快速web应用开发——基础概念篇](https://www.cnblogs.com/feffery/p/14258438.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/01%20%E5%9F%BA%E7%A1%80%E6%A6%82%E5%BF%B5%E7%AF%87)
- [（数据科学学习手札103）Python+Dash快速web应用开发——页面布局篇](https://www.cnblogs.com/feffery/p/14276803.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/02%20%E9%A1%B5%E9%9D%A2%E5%B8%83%E5%B1%80%E7%AF%87)
- [（数据科学学习手札104）Python+Dash快速web应用开发——回调交互篇（上）](https://www.cnblogs.com/feffery/p/14313103.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/03%20%E5%9B%9E%E8%B0%83%E4%BA%A4%E4%BA%92%E7%AF%87%EF%BC%88%E4%B8%8A%EF%BC%89)
- [（数据科学学习手札105）Python+Dash快速web应用开发——回调交互篇（中）](https://www.cnblogs.com/feffery/p/14349206.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/04%20%E5%9B%9E%E8%B0%83%E4%BA%A4%E4%BA%92%E7%AF%87%EF%BC%88%E4%B8%AD%EF%BC%89)
- [（数据科学学习手札106）Python+Dash快速web应用开发——回调交互篇（下）](https://www.cnblogs.com/feffery/p/14386458.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/05%20%E5%9B%9E%E8%B0%83%E4%BA%A4%E4%BA%92%E7%AF%87%EF%BC%88%E4%B8%8B%EF%BC%89)
- [（数据科学学习手札107）在Python中利用funct实现链式风格编程](https://www.cnblogs.com/feffery/p/14400938.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札107）在Python中利用funct实现链式风格编程)
- [（数据科学学习手札108）Python+Dash快速web应用开发——静态部件篇（上）](https://www.cnblogs.com/feffery/p/14416390.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/06%20%E9%9D%99%E6%80%81%E9%83%A8%E4%BB%B6%E7%AF%87%EF%BC%88%E4%B8%8A%EF%BC%89)
- [（数据科学学习手札109）Python+Dash快速web应用开发——静态部件篇（中）](https://www.cnblogs.com/feffery/p/14457005.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/07%20%E9%9D%99%E6%80%81%E9%83%A8%E4%BB%B6%E7%AF%87%EF%BC%88%E4%B8%AD%EF%BC%89)
- [（数据科学学习手札110）Python+Dash快速web应用开发——静态部件篇（下）](https://www.cnblogs.com/feffery/p/14492085.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/08%20%E9%9D%99%E6%80%81%E9%83%A8%E4%BB%B6%E7%AF%87%EF%BC%88%E4%B8%8B%EF%BC%89)
- [（数据科学学习手札111）geopandas 0.9.0重要新特性一览](https://www.cnblogs.com/feffery/p/14519824.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD111%EF%BC%89geopandas%200.9.0%E9%87%8D%E8%A6%81%E6%96%B0%E7%89%B9%E6%80%A7%E4%B8%80%E8%A7%88)
- [（数据科学学习手札112）Python+Dash快速web应用开发——表单控件篇（上）](https://www.cnblogs.com/feffery/p/14532519.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/09%20%E8%A1%A8%E5%8D%95%E6%8E%A7%E4%BB%B6%E7%AF%87%EF%BC%88%E4%B8%8A%EF%BC%89)
- [（数据科学学习手札113）Python+Dash快速web应用开发——表单控件篇（下）](https://www.cnblogs.com/feffery/p/14561303.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/10%20%E8%A1%A8%E5%8D%95%E6%8E%A7%E4%BB%B6%E7%AF%87%EF%BC%88%E4%B8%8B%EF%BC%89)
- [（数据科学学习手札114）Python+Dash快速web应用开发——上传下载篇](https://www.cnblogs.com/feffery/p/14580950.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/11%20%E4%B8%8A%E4%BC%A0%E4%B8%8B%E8%BD%BD%E7%AF%87)
- [（数据科学学习手札115）Python+Dash快速web应用开发——交互表格篇（上）](https://www.cnblogs.com/feffery/p/14616652.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/12%20%E4%BA%A4%E4%BA%92%E8%A1%A8%E6%A0%BC%E7%AF%87%EF%BC%88%E4%B8%8A%EF%BC%89)
- [（数据科学学习手札116）Python+Dash快速web应用开发——交互表格篇（中）](https://www.cnblogs.com/feffery/p/14641943.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/13%20%E4%BA%A4%E4%BA%92%E8%A1%A8%E6%A0%BC%E7%AF%87%EF%BC%88%E4%B8%AD%EF%BC%89)
- [（数据科学学习手札117）Python+Dash快速web应用开发——交互表格篇（下）](https://www.cnblogs.com/feffery/p/14674642.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/14%20%E4%BA%A4%E4%BA%92%E8%A1%A8%E6%A0%BC%E7%AF%87%EF%BC%88%E4%B8%8B%EF%BC%89)
- [（数据科学学习手札118）Python+Dash快速web应用开发——特殊部件篇](https://www.cnblogs.com/feffery/p/14687893.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/15%20%E7%89%B9%E6%AE%8A%E9%83%A8%E4%BB%B6%E7%AF%87)
- [（数据科学学习手札119）Python+Dash快速web应用开发——多页面应用](https://www.cnblogs.com/feffery/p/14724140.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/16%20%E5%A4%9A%E9%A1%B5%E9%9D%A2%E5%BA%94%E7%94%A8)
- [（数据科学学习手札120）Python+Dash快速web应用开发——整合数据库](https://www.cnblogs.com/feffery/p/14748675.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/17%20%E6%95%B4%E5%90%88%E6%95%B0%E6%8D%AE%E5%BA%93)
- [（数据科学学习手札121）Python+Dash快速web应用开发——项目结构篇](https://www.cnblogs.com/feffery/p/14773887.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E3%80%90Python%2BDash%E5%BF%AB%E9%80%9Fweb%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E3%80%91%E7%B3%BB%E5%88%97%E6%96%87%E7%AB%A0/18%20%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84%E7%AF%87)
- [（数据科学学习手札122）Python+Dash快速web应用开发——内网穿透篇](https://www.cnblogs.com/feffery/p/14775704.html)
- [（数据科学学习手札123）Python+Dash快速web应用开发——部署发布篇](https://www.cnblogs.com/feffery/p/14826195.html)
- [（数据科学学习手札124）pandas 1.3版本主要更新内容一览](https://www.cnblogs.com/feffery/p/14993399.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD124%EF%BC%89pandas%201.3%E7%89%88%E6%9C%AC%E4%B8%BB%E8%A6%81%E6%9B%B4%E6%96%B0%E5%86%85%E5%AE%B9%E4%B8%80%E8%A7%88)
- [（数据科学学习手札125）在Python中操纵json数据的最佳方式](https://www.cnblogs.com/feffery/p/15087235.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札125）在Python中操纵json数据的最佳方式)
- [（数据科学学习手札126）Python中JSON结构数据的高效增删改操作](https://www.cnblogs.com/feffery/p/15115785.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札126）Python中JSON结构数据的高效增删改操作)
- [（数据科学学习手札127）在Python中使用icecream实现高效debug](https://www.cnblogs.com/feffery/p/15181212.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札127）在Python中使用icecream实现高效debug)
- [（数据科学学习手札128）在matplotlib中添加富文本的最佳方式](https://www.cnblogs.com/feffery/p/15331473.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札128）在matplotlib中添加富文本的最佳方式)
- [（数据科学学习手札129）geopandas 0.10版本重要新特性一览](https://www.cnblogs.com/feffery/p/15472342.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD129%EF%BC%89geopandas%200.10%E7%89%88%E6%9C%AC%E9%87%8D%E8%A6%81%E6%96%B0%E7%89%B9%E6%80%A7%E4%B8%80%E8%A7%88)
- [（数据科学学习手札130）利用geopandas快捷绘制在线地图](https://www.cnblogs.com/feffery/p/15530464.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札130）利用geopandas快捷绘制在线地图)
- [（数据科学学习手札131）pandas中的常用字符串处理方法总结](https://www.cnblogs.com/feffery/p/15584726.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札131）pandas中的常用字符串处理方法总结)
- [（数据科学学习手札132）Python+Fabric实现远程服务器连接](https://www.cnblogs.com/feffery/p/15646508.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札132）Python+Fabric实现远程服务器连接)
- [（数据科学学习手札133）利用geopandas绘制拓扑着色地图](https://www.cnblogs.com/feffery/p/15738273.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札133）利用geopandas绘制拓扑着色地图)
- [（数据科学学习手札134）pyjanitor：为pandas补充更多功能](https://www.cnblogs.com/feffery/p/15998079.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札134）pyjanitor：为pandas补充更多功能)
- [（数据科学学习手札135）tenacity：Python中最强大的错误重试库](https://www.cnblogs.com/feffery/p/16056079.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札135）tenacity：Python中最强大的错误重试库)
- [（数据科学学习手札136）Python中基于joblib实现极简并行计算加速](https://www.cnblogs.com/feffery/p/16271159.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札136）Python中基于joblib实现极简并行计算加速)
- [（数据科学学习手札137）orjson：Python中最好用的json库](https://www.cnblogs.com/feffery/p/16344712.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札137）orjson：Python中最好用的json库)
- [（数据科学学习手札138）使用sklearnex大幅加速scikit-learn运算](https://www.cnblogs.com/feffery/p/16387854.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札138）使用sklearnex大幅加速scikit-learn运算)
- [（数据科学学习手札139）geopandas 0.11版本重要新特性一览](https://www.cnblogs.com/feffery/p/16410796.html)　✈️[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%99%84%E4%BB%B6%E5%88%97%E8%A1%A8/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD139%EF%BC%89geopandas%200.11%E7%89%88%E6%9C%AC%E9%87%8D%E8%A6%81%E6%96%B0%E7%89%B9%E6%80%A7%E4%B8%80%E8%A7%88)
- [（数据科学学习手札140）详解geopandas中基于pyogrio的矢量读写引擎](https://www.cnblogs.com/feffery/p/16459024.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札140）详解geopandas中基于pyogrio的矢量读写引擎)
- [（数据科学学习手札141）利用Learn Git Branching轻松学习git常用操作](https://www.cnblogs.com/feffery/p/16689961.html)
- [（数据科学学习手札142）dill：Python中增强版的pickle](https://www.cnblogs.com/feffery/p/16703398.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札142）dill：Python中增强版的pickle)
- [（数据科学学习手札143）为geopandas添加gdb文件写出功能](https://www.cnblogs.com/feffery/p/16711477.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札143）为geopandas添加gdb文件写出功能)
- [（数据科学学习手札144）使用管道操作符高效书写Python代码](https://www.cnblogs.com/feffery/p/16794858.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札144）使用管道操作符高效书写Python代码)
- [（数据科学学习手札145）在Python中利用yarl轻松操作url](https://www.cnblogs.com/feffery/p/16817124.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札145）在Python中利用yarl轻松操作url)
- [（数据科学学习手札146）geopandas中拓扑非法问题的发现、诊断与修复](https://www.cnblogs.com/feffery/p/16841979.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札146）geopandas中拓扑非法问题的发现、诊断与修复)
- [（数据科学学习手札147）Python GIS利器shapely全新2.0版本一览](https://www.cnblogs.com/feffery/p/16989398.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札147）Python%20GIS利器shapely全新2.0版本一览)
- [（数据科学学习手札148）geopandas直接支持gdb文件写出与追加](https://www.cnblogs.com/feffery/p/17025278.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札148）geopandas直接支持gdb文件写出与追加)
- [（数据科学学习手札149）用matplotlib轻松绘制漂亮的表格](https://www.cnblogs.com/feffery/p/17086814.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札149）用matplotlib轻松绘制漂亮的表格)
- [（数据科学学习手札150）基于dask对geopandas进行并行加速](https://www.cnblogs.com/feffery/p/17231708.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札150）基于dask对geopandas进行并行加速)
- [（数据科学学习手札151）速通pandas2.0新版本干货内容](https://www.cnblogs.com/feffery/p/17290646.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札151）速通pandas2.0新版本干货内容)
- [（数据科学学习手札152）geopandas0.13版本更新内容一览](https://www.cnblogs.com/feffery/p/17379888.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札152）geopandas0.13版本更新内容一览)
- [（数据科学学习手札153）基于martin的高性能矢量切片地图服务构建](https://www.cnblogs.com/feffery/p/17581158.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札153）基于martin的高性能矢量切片地图服务构建)
- [（数据科学学习手札154）geopandas0.14版本新特性一览](https://www.cnblogs.com/feffery/p/17709443.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札154）geopandas0.14版本新特性一览)
- [（数据科学学习手札155）基于martin为在线地图构建字体切片服务](https://www.cnblogs.com/feffery/p/17846899.html)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札155）基于martin为在线地图构建字体切片服务)
- [（数据科学学习手札156）地图可视化神器kepler.gl 3.0版本发布](https://www.cnblogs.com/feffery/p/17932811.html)
- [（数据科学学习手札157）pandas新增case_when方法](https://www.cnblogs.com/feffery/p/17991230)　✈️[仓库路径](./历史文章附件列表/（数据科学学习手札157）pandas新增case_when方法)
***

<a name="second"></a>

## 2 :card_file_box: 专题系列：

<a name="second-geopandas"></a>
### 2.1 :earth_asia: 基于geopandas的空间数据分析　🏊 `<持续更新中>` 
- [课程附件百度云下载地址](https://pan.baidu.com/s/1czvOSQLoxnwbW-sACuASYQ)（提取码：6cjq）：

<p align="center">
  <img src="https://geopandas.readthedocs.io/en/latest/_static/geopandas_logo_web.svg" width="500"></img>
</p>

  - [（数据科学学习手札74）基于geopandas的空间数据分析——数据结构篇](https://www.cnblogs.com/feffery/p/11898190.html)<br>
  - [（数据科学学习手札75）基于geopandas的空间数据分析——坐标参考系篇](https://www.cnblogs.com/feffery/p/12285828.html)<br>
  - [（数据科学学习手札77）基于geopandas的空间数据分析——文件IO](https://www.cnblogs.com/feffery/p/12301966.html)<br>
  - [（数据科学学习手札78）基于geopandas的空间数据分析——基础可视化](https://www.cnblogs.com/feffery/p/12361421.html)<br>
  - [（数据科学学习手札79）基于geopandas的空间数据分析——深入浅出分层设色](https://www.cnblogs.com/feffery/p/12381322.html)<br>
  - [（数据科学学习手札82）基于geopandas的空间数据分析——geoplot篇(上)](https://www.cnblogs.com/feffery/p/12779150.html)<br>
  - [（数据科学学习手札83）基于geopandas的空间数据分析——geoplot篇(下)](https://www.cnblogs.com/feffery/p/12901334.html)<br>
  - [（数据科学学习手札84）基于geopandas的空间数据分析——空间计算篇（上）](https://www.cnblogs.com/feffery/p/12909284.html)<br>
  - [（数据科学学习手札88）基于geopandas的空间数据分析——空间计算篇（下）](https://www.cnblogs.com/feffery/p/13129271.html)<br>
  - :sparkles: **衍生文章**
    - [（数据科学学习手札89）geopandas&geoplot近期重要更新](https://www.cnblogs.com/feffery/p/13233271.html)
    - [（数据科学学习手札93）利用geopandas与PostGIS进行交互](https://www.cnblogs.com/feffery/p/13468203.html)
    - [（数据科学学习手札96）在geopandas中叠加在线地图](https://www.cnblogs.com/feffery/p/13763601.html)
    - [（数据科学学习手札111）geopandas 0.9.0重要新特性一览](https://www.cnblogs.com/feffery/p/14519824.html)
    - [（数据科学学习手札129）geopandas 0.10版本重要新特性一览](https://www.cnblogs.com/feffery/p/15472342.html)
    - [（数据科学学习手札130）利用geopandas快捷绘制在线地图](https://www.cnblogs.com/feffery/p/15530464.html)
    - [（数据科学学习手札133）利用geopandas绘制拓扑着色地图](https://www.cnblogs.com/feffery/p/15738273.html)
    - [（数据科学学习手札139）geopandas 0.11版本重要新特性一览](https://www.cnblogs.com/feffery/p/16410796.html)
    - [（数据科学学习手札140）详解geopandas中基于pyogrio的矢量读写引擎](https://www.cnblogs.com/feffery/p/16459024.html)
    - [（数据科学学习手札143）为geopandas添加gdb文件写出功能](https://www.cnblogs.com/feffery/p/16711477.html)
    - [（数据科学学习手札146）geopandas中拓扑非法问题的发现、诊断与修复](https://www.cnblogs.com/feffery/p/16841979.html)
    - [（数据科学学习手札147）Python GIS利器shapely全新2.0版本一览](https://www.cnblogs.com/feffery/p/16989398.html)
    - [（数据科学学习手札148）geopandas直接支持gdb文件写出与追加](https://www.cnblogs.com/feffery/p/17025278.html)
    - [（数据科学学习手札150）基于dask对geopandas进行并行加速](https://www.cnblogs.com/feffery/p/17231708.html)
    - [（数据科学学习手札152）geopandas0.13版本更新内容一览](https://www.cnblogs.com/feffery/p/17379888.html)
    - [（数据科学学习手札153）基于martin的高性能矢量切片地图服务构建](https://www.cnblogs.com/feffery/p/17581158.html)
    - [（数据科学学习手札154）geopandas0.14版本新特性一览](https://www.cnblogs.com/feffery/p/17709443.html)

​    

<a name="second-dash"></a>

### 2.2 :zap: Python+Dash快速web应用开发　🚩 `<完结>` 

<p align="center">
  <img src="./历史文章附件列表/Plotly_Dash_logo.png" width="450"></img>
</p>

  - [（数据科学学习手札102）Python+Dash快速web应用开发——基础概念篇](https://www.cnblogs.com/feffery/p/14258438.html)<br>
  - [（数据科学学习手札103）Python+Dash快速web应用开发——页面布局篇](https://www.cnblogs.com/feffery/p/14276803.html)<br>
  - [（数据科学学习手札104）Python+Dash快速web应用开发——回调交互篇（上）](https://www.cnblogs.com/feffery/p/14313103.html)<br>
  - [（数据科学学习手札105）Python+Dash快速web应用开发——回调交互篇（中）](https://www.cnblogs.com/feffery/p/14349206.html)<br>
  - [（数据科学学习手札106）Python+Dash快速web应用开发——回调交互篇（下）](https://www.cnblogs.com/feffery/p/14386458.html)<br>
  - [（数据科学学习手札108）Python+Dash快速web应用开发——静态部件篇（上）](https://www.cnblogs.com/feffery/p/14416390.html)<br>
  - [（数据科学学习手札109）Python+Dash快速web应用开发——静态部件篇（中）](https://www.cnblogs.com/feffery/p/14457005.html)<br>
  - [（数据科学学习手札110）Python+Dash快速web应用开发——静态部件篇（下）](https://www.cnblogs.com/feffery/p/14492085.html)<br>
  - [（数据科学学习手札112）Python+Dash快速web应用开发——表单控件篇（上）](https://www.cnblogs.com/feffery/p/14532519.html)<br>
  - [（数据科学学习手札113）Python+Dash快速web应用开发——表单控件篇（下）](https://www.cnblogs.com/feffery/p/14561303.html)<br>
  - [（数据科学学习手札114）Python+Dash快速web应用开发——上传下载篇](https://www.cnblogs.com/feffery/p/14580950.html)<br>
  - [（数据科学学习手札115）Python+Dash快速web应用开发——交互表格篇（上）](https://www.cnblogs.com/feffery/p/14616652.html)<br>
  - [（数据科学学习手札116）Python+Dash快速web应用开发——交互表格篇（中）](https://www.cnblogs.com/feffery/p/14641943.html)<br>
  - [（数据科学学习手札117）Python+Dash快速web应用开发——交互表格篇（下）](https://www.cnblogs.com/feffery/p/14674642.html)<br>
  - [（数据科学学习手札118）Python+Dash快速web应用开发——特殊部件篇](https://www.cnblogs.com/feffery/p/14687893.html)<br>
  - [（数据科学学习手札119）Python+Dash快速web应用开发——多页面应用](https://www.cnblogs.com/feffery/p/14724140.html)<br>
  - [（数据科学学习手札120）Python+Dash快速web应用开发——整合数据库](https://www.cnblogs.com/feffery/p/14748675.html)<br>
  - [（数据科学学习手札121）Python+Dash快速web应用开发——项目结构篇](https://www.cnblogs.com/feffery/p/14773887.html)<br>
  - [（数据科学学习手札122）Python+Dash快速web应用开发——内网穿透篇](https://www.cnblogs.com/feffery/p/14775704.html)<br>
  - [（数据科学学习手札123）Python+Dash快速web应用开发——部署发布篇](https://www.cnblogs.com/feffery/p/14826195.html)<br>

***

<a name="pandas"></a>

## 3 :man_astronaut: pandas相关

<p align="center">
  <img src="https://pandas.pydata.org/docs/_static/pandas.svg" width="350"></img>
</p>

- [（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg](https://www.cnblogs.com/feffery/p/11468762.html)<br>
- [（数据科学学习手札72）用pdpipe搭建pandas数据分析流水线](https://www.cnblogs.com/feffery/p/12179647.html)<br>
- [（数据科学学习手札73）盘点pandas 1.0.0中的新特性](https://www.cnblogs.com/feffery/p/12214635.html)<br>
- [（数据科学学习手札86）全平台支持的pandas运算加速神器](https://www.cnblogs.com/feffery/p/13049547.html)<br>
- [（数据科学学习手札92）利用query()与eval()优化pandas代码](https://www.cnblogs.com/feffery/p/13440148.html)<br>
- [（数据科学学习手札97）掌握pandas中的transform](https://www.cnblogs.com/feffery/p/13816362.html)<br>
- [（数据科学学习手札99）掌握pandas中的时序数据分组运算](https://www.cnblogs.com/feffery/p/14093478.html)<br>
- [（数据科学学习手札124）pandas 1.3版本主要更新内容一览](https://www.cnblogs.com/feffery/p/14993399.html)<br>
- [（数据科学学习手札131）pandas中的常用字符串处理方法总结](https://www.cnblogs.com/feffery/p/15584726.html)
- [（数据科学学习手札134）pyjanitor：为pandas补充更多功能](https://www.cnblogs.com/feffery/p/15998079.html)
- [（数据科学学习手札151）速通pandas2.0新版本干货内容](https://www.cnblogs.com/feffery/p/17290646.html)
- [（数据科学学习手札157）pandas新增case_when方法](https://www.cnblogs.com/feffery/p/17991230)

***

<a name="jupyter"></a>

## 4 :ghost: jupyter相关

<p align="center">
  <img src="https://jupyter.org/assets/homepage/main-logo.svg" width="220"></img>
</p>

- [（数据科学学习手札81）conda+jupyter玩转数据科学环境搭建](https://www.cnblogs.com/feffery/p/12609118.html)<br>
- [（数据科学学习手札94）QGIS+Conda+jupyter玩转Python GIS](https://www.cnblogs.com/feffery/p/13558608.html)<br>
- [（数据科学学习手札95）elyra——jupyter lab平台最强插件集](https://www.cnblogs.com/feffery/p/13692800.html)<br>

***

<a name="keplergl"></a>
## 5 :penguin: kepler.gl相关

<p align="center">
  <img src="https://d1a3f4spazzrp4.cloudfront.net/kepler.gl/website/icons/kepler.gl-logo.png" width="320"></img>
</p>

- [（数据科学学习手札85）Python+Kepler.gl轻松制作酷炫路径动画](https://www.cnblogs.com/feffery/p/12987968.html)<br>
- [（数据科学学习手札90）Python+Kepler.gl轻松制作时间轮播地图](https://www.cnblogs.com/feffery/p/13322067.html)<br>
- [（数据科学学习手札156）地图可视化神器kepler.gl 3.0版本发布](https://www.cnblogs.com/feffery/p/17932811.html)<br>

***



