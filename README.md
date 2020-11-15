# :memo: DataScienceStudyNotes
:dart:这个仓库保管从（数据科学学习手札69）开始的所有代码、数据等相关附件内容
<br>:email:交流学习请联系邮箱：fefferypzy@gmail.com
<br>:rainbow:博客地址：https://www.cnblogs.com/feffery/

# :carousel_horse: 目录
- :books: [1 已更新博客列表](#first)
- :card_file_box: [2 专题系列](#second)
  - :earth_asia: [2.1 基于geopandas的空间数据分析 🚩 `<完结>`](#second-geopandas)
- :man_astronaut: [3 pandas相关](#pandas)
- :ghost: [4 jupyter相关](#jupyter)
- :penguin: [5 kepler.gl相关](#keplergl)
- :wrench: [6 补充勘误内容记录](#third)
- :running: [7 To-do List](#fourth)

***

<a name="first"></a>
## 1 :books: 已更新博客列表：
- [（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg](https://www.cnblogs.com/feffery/p/11468762.html) 　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD69%EF%BC%89%E8%AF%A6%E8%A7%A3pandas%E4%B8%AD%E7%9A%84map%E3%80%81apply%E3%80%81applymap%E3%80%81groupby%E3%80%81agg)
- [（数据科学学习手札70）面向数据科学的Python多进程简介及应用](https://www.cnblogs.com/feffery/p/11621076.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD70%EF%BC%89%E9%9D%A2%E5%90%91%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E7%9A%84Python%E5%A4%9A%E8%BF%9B%E7%A8%8B%E7%AE%80%E4%BB%8B%E5%8F%8A%E5%BA%94%E7%94%A8)
- [（数据科学学习手札71）利用Python绘制词云图](https://www.cnblogs.com/feffery/p/11842798.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD71%EF%BC%89%E5%9C%A8Python%E4%B8%AD%E5%88%B6%E4%BD%9C%E4%B8%AA%E6%80%A7%E5%8C%96%E8%AF%8D%E4%BA%91%E5%9B%BE)
- [（数据科学学习手札72）用pdpipe搭建pandas数据分析流水线](https://www.cnblogs.com/feffery/p/12179647.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD72%EF%BC%89%E7%94%A8pdpipe%E6%90%AD%E5%BB%BApandas%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%B5%81%E6%B0%B4%E7%BA%BF)
- [（数据科学学习手札73）盘点pandas 1.0.0中的新特性](https://www.cnblogs.com/feffery/p/12214635.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD73%EF%BC%89%E7%9B%98%E7%82%B9pandas%201.0.0%E4%B8%AD%E7%9A%84%E6%96%B0%E7%89%B9%E6%80%A7)
- [（数据科学学习手札74）基于geopandas的空间数据分析——数据结构篇](https://www.cnblogs.com/feffery/p/11898190.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD74%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%AF%87)
- [（数据科学学习手札75）基于geopandas的空间数据分析——坐标参考系篇](https://www.cnblogs.com/feffery/p/12285828.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD75%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E5%9D%90%E6%A0%87%E5%8F%82%E8%80%83%E7%B3%BB%E7%AF%87)
- [（数据科学学习手札76）基于Python的拐点检测——以新冠肺炎疫情数据为例](https://www.cnblogs.com/feffery/p/12325741.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD76%EF%BC%89%E5%9F%BA%E4%BA%8EPython%E7%9A%84%E6%8B%90%E7%82%B9%E6%A3%80%E6%B5%8B%E2%80%94%E2%80%94%E4%BB%A5%E6%96%B0%E5%86%A0%E8%82%BA%E7%82%8E%E7%96%AB%E6%83%85%E6%95%B0%E6%8D%AE%E4%B8%BA%E4%BE%8B)
- [（数据科学学习手札77）基于geopandas的空间数据分析——文件IO](https://www.cnblogs.com/feffery/p/12301966.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD77%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E6%96%87%E4%BB%B6IO)
- [（数据科学学习手札78）基于geopandas的空间数据分析——基础可视化](https://www.cnblogs.com/feffery/p/12361421.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD78%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E5%9F%BA%E7%A1%80%E5%8F%AF%E8%A7%86%E5%8C%96)
- [（数据科学学习手札79）基于geopandas的空间数据分析——深入浅出分层设色](https://www.cnblogs.com/feffery/p/12381322.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD79%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BA%E5%88%86%E5%B1%82%E8%AE%BE%E8%89%B2)
- [（数据科学学习手札80）用Python编写小工具下载OSM路网数据](https://www.cnblogs.com/feffery/p/12483967.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD80%EF%BC%89%E7%94%A8Python%E7%BC%96%E5%86%99%E5%B0%8F%E5%B7%A5%E5%85%B7%E4%B8%8B%E8%BD%BDOSM%E8%B7%AF%E7%BD%91%E6%95%B0%E6%8D%AE)
- [（数据科学学习手札81）conda+jupyter玩转数据科学环境搭建](https://www.cnblogs.com/feffery/p/12609118.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD81%EF%BC%89conda%2Bjupyter%E7%8E%A9%E8%BD%AC%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)
- [（数据科学学习手札82）基于geopandas的空间数据分析——geoplot篇(上)](https://www.cnblogs.com/feffery/p/12779150.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD82%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94geoplot%E7%AF%87(%E4%B8%8A))
- [（数据科学学习手札83）基于geopandas的空间数据分析——geoplot篇(下)](https://www.cnblogs.com/feffery/p/12901334.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD83%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94geoplot%E7%AF%87(%E4%B8%8B))
- [（数据科学学习手札84）基于geopandas的空间数据分析——空间计算篇（上）](https://www.cnblogs.com/feffery/p/12909284.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD84%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E7%A9%BA%E9%97%B4%E8%AE%A1%E7%AE%97%E7%AF%87%EF%BC%88%E4%B8%8A%EF%BC%89)
- [（数据科学学习手札85）Python+Kepler.gl轻松制作酷炫路径动画](https://www.cnblogs.com/feffery/p/12987968.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD85%EF%BC%89Python%2BKepler.gl%E8%BD%BB%E6%9D%BE%E5%88%B6%E4%BD%9C%E9%85%B7%E7%82%AB%E8%B7%AF%E5%BE%84%E5%8A%A8%E7%94%BB)
- [（数据科学学习手札86）全平台支持的pandas运算加速神器](https://www.cnblogs.com/feffery/p/13049547.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD86%EF%BC%89%E5%85%A8%E5%B9%B3%E5%8F%B0%E6%94%AF%E6%8C%81%E7%9A%84pandas%E8%BF%90%E7%AE%97%E5%8A%A0%E9%80%9F%E7%A5%9E%E5%99%A8)
- [（数据科学学习手札87）利用adjustText解决matplotlib文字标签遮挡问题](https://www.cnblogs.com/feffery/p/13072364.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD87%EF%BC%89%E5%88%A9%E7%94%A8adjustText%E8%A7%A3%E5%86%B3matplotlib%E6%96%87%E5%AD%97%E6%A0%87%E7%AD%BE%E9%81%AE%E6%8C%A1%E9%97%AE%E9%A2%98)
- [（数据科学学习手札88）基于geopandas的空间数据分析——空间计算篇（下）](https://www.cnblogs.com/feffery/p/13129271.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD88%EF%BC%89%E5%9F%BA%E4%BA%8Egeopandas%E7%9A%84%E7%A9%BA%E9%97%B4%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E2%80%94%E2%80%94%E7%A9%BA%E9%97%B4%E8%AE%A1%E7%AE%97%E7%AF%87%EF%BC%88%E4%B8%8B%EF%BC%89)
- [（数据科学学习手札89）geopandas&geoplot近期重要更新](https://www.cnblogs.com/feffery/p/13233271.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD89%EF%BC%89geopandas%26geoplot%E8%BF%91%E6%9C%9F%E9%87%8D%E8%A6%81%E6%9B%B4%E6%96%B0)
- [（数据科学学习手札90）Python+Kepler.gl轻松制作时间轮播地图](https://www.cnblogs.com/feffery/p/13322067.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD90%EF%BC%89Python+Kepler.gl%E8%BD%BB%E6%9D%BE%E5%88%B6%E4%BD%9C%E6%97%B6%E9%97%B4%E8%BD%AE%E6%92%AD%E5%9C%B0%E5%9B%BE)
- [（数据科学学习手札91）在Python中妥善使用进度条](https://www.cnblogs.com/feffery/p/13392024.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD91%EF%BC%89%E5%9C%A8Python%E4%B8%AD%E5%A6%A5%E5%96%84%E4%BD%BF%E7%94%A8%E8%BF%9B%E5%BA%A6%E6%9D%A1)
- [（数据科学学习手札92）利用query()与eval()优化pandas代码](https://www.cnblogs.com/feffery/p/13440148.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD92%EF%BC%89%E5%88%A9%E7%94%A8query()%E4%B8%8Eeval()%E4%BC%98%E5%8C%96pandas%E4%BB%A3%E7%A0%81)
- [（数据科学学习手札93）利用geopandas与PostGIS进行交互](https://www.cnblogs.com/feffery/p/13468203.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD93%EF%BC%89%E5%88%A9%E7%94%A8geopandas%E4%B8%8EPostGIS%E8%BF%9B%E8%A1%8C%E4%BA%A4%E4%BA%92)
- [（数据科学学习手札94）QGIS+Conda+jupyter玩转Python GIS](https://www.cnblogs.com/feffery/p/13558608.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD94%EF%BC%89QGIS+Conda+jupyter%E7%8E%A9%E8%BD%ACPython%20GIS)
- [（数据科学学习手札95）elyra——jupyter lab平台最强插件集](https://www.cnblogs.com/feffery/p/13692800.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD95%EF%BC%89elyra%E2%80%94%E2%80%94jupyter%20lab%E5%B9%B3%E5%8F%B0%E6%9C%80%E5%BC%BA%E6%8F%92%E4%BB%B6%E9%9B%86)
- [（数据科学学习手札96）在geopandas中叠加在线地图](https://www.cnblogs.com/feffery/p/13763601.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD96%EF%BC%89%E5%9C%A8geopandas%E4%B8%AD%E5%8F%A0%E5%8A%A0%E5%9C%A8%E7%BA%BF%E5%9C%B0%E5%9B%BE)
- [（数据科学学习手札97）掌握pandas中的transform](https://www.cnblogs.com/feffery/p/13816362.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD97%EF%BC%89%E6%8E%8C%E6%8F%A1pandas%E4%B8%AD%E7%9A%84transform)
- [（数据科学学习手札98）纯Python绘制满满艺术感的山脊地图](https://www.cnblogs.com/feffery/p/13977871.html)　:airplane:[仓库路径](https://github.com/CNFeffery/DataScienceStudyNotes/tree/master/%EF%BC%88%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6%E5%AD%A6%E4%B9%A0%E6%89%8B%E6%9C%AD98%EF%BC%89%E7%BA%AFPython%E7%BB%98%E5%88%B6%E6%BB%A1%E6%BB%A1%E8%89%BA%E6%9C%AF%E6%84%9F%E7%9A%84%E5%B1%B1%E8%84%8A%E5%9C%B0%E5%9B%BE)

***

<a name="second"></a>
## 2 :card_file_box: 专题系列：

<a name="second-geopandas"></a>
### 2.1 :earth_asia: 基于geopandas的空间数据分析　🚩 `<完结>` 
- [课程附件百度云下载地址](https://pan.baidu.com/s/1ZzbxAm-0-udUaLlhM_KP7w)（提取码：1syu）：

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

***

<a name="jupyter"></a>
## 4 :ghost: jupyter相关

<p align="center">
  <img src="https://jupyter.org/assets/nav_logo.svg" width="320"></img>
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

***

<a name="third"></a>
## 6 :wrench: 补充&勘误内容记录：
- 2019.10.28 为[（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg](https://www.cnblogs.com/feffery/p/11468762.html)补充`apply()同时返回多列数据的方法`
- 2019.11.26 为[（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg](https://www.cnblogs.com/feffery/p/11468762.html)补充`tqdm_notebook()版apply()进度条的方法`
- 2020.01.15 为[（数据科学学习手札72）用pdpipe搭建pandas数据分析流水线](https://www.cnblogs.com/feffery/p/12179647.html)补充`用算术相加法拼接流水线的方法`
- 2020.08.27 为[（数据科学学习手札94）QGIS+Conda+jupyter玩转Python GIS](https://www.cnblogs.com/feffery/p/13558608.html)勘误：1.`PyQgis`中的**渔网创建工具**无`INPUT`参数；2.现阶段`geopandas`与`PyQgis`之间并无互相**兼容相通**的设定，因此无法将`GeoDataFrame`类型的变量作为`INPUT`参数传入`PyQgis`算法执行过程中
- 2020.09.28 为[（数据科学学习手札69）详解pandas中的map、apply、applymap、groupby、agg](https://www.cnblogs.com/feffery/p/11468762.html)更新：由于`numpy`的版本更新，故将**3.1**章节下`结合apply()`中的`df['name'][np.argmax(df['count'])]`更新为`df['name'][df['count'].idxmax()]`

***

<a name="fourth"></a>
## 7 :running: To-do List:
- [x] **adjustText的使用**
- [x] **基于geopandas的地理空间数据分析*****系列文章***　***已完结*** 🚩
- [x] **在Python中妥善使用进度条**
- [x] **最强jupyter lab插件elyra功能介绍**
- [ ] **介绍fastcore的常用功能**
- [ ] **详解pandas中的表格风格化**
- [ ] **plotly_express最佳实践*****系列文章***
- [ ] **folium最佳实践*****系列文章***
- [ ] **dplyr快速入门**
- [ ] **plotly完全指南*****系列文章***

