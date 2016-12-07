# PCTDM
Python 中文文本挖掘

本人初哥，每样东西略懂一点皮毛中的皮毛，感谢网上丰富的资源。
欢迎有同样兴趣人士来交流。

暂拟技术路线如下。
1. 中文文本获取
  1）存量文本 （Done）
  2）Python爬虫获取Web文本。
  3）Python爬虫获取CNKI文献资源文本。（Done）
  4）其他文本

2. 中文数据清洗。
  1）编码转换 （Done）
  2）按需求进行一定格式化 （Done）
  
3. 中文处理。
  1）分词（结巴分词为主）、词频统计等（Done）
  2）向量化（VSM，Word2vec，LDA等）（Done）
  3）文本聚类（Hadoop的Mahout跑，现在似乎已经被归入Spark）（Done）
  4）相似度计算（Done）
  5）输出各种json文件。（Done）
  6）Django建个站点进行交互。（Done）
  
4.可视化展示
  1）送到Elastic Stack创建索引，用Kibana展示 （Done）
  2）D3.js展示 （不会js，感觉略复杂）（Done）
  3）Echart展示（不会js，感觉看demo比D3.js简单些）

 摸索中：
  新词发现
  实体归并
 
 
