# Data-Science-Notes
数据科学的笔记以及资料搜集，目前尚在更新，部分内容来源于github搜集。

[0.math](0.math) （数学基础）

[1.python-basic](1.python-basic) （python基础）

[2.numpy](2.numpy)（numpy基础）

[3.pandas](3.pandas)（pandas基础）

[4.scipy](4.scipy)（scipy基础）

[5.data-visualization](5.data-visualization)（数据可视化基础，包含matplotlib和seaborn）

[6.scikit-learn](6.scikit-learn)（scikit-learn基础）

[7.machine-learning](7.machine-learning)（机器学习基础）

[8.deep-learning](8.deep-learning)（深度学习基础）

[9.feature-engineering](9.feature-engineering)（特征工程基础）

#####  2021-2022 Study PathWay ######

第一阶段 机器学习基础与凸优化
本阶段主要目的是讲解必要的算法理论以及凸优化技术，为后续的课程打下基础。凸优化的重要性不言而喻，如果想具备改造模型的能力，对于凸优化的理解是必不可少的！ 
【核心知识点】
- KNN，Weighted KNN、近似KNN
- KD树，近似KD树、哈希算法、LSH
- 岭回归、LASSO、ElasticNet
- 正则：L1, L2, L-inifity Norm
- LR、GD、SGD、小批量SGD
- 凸集，凸函数、判定凸函数
- LP、QP、ILP、SDP问题
- Duality，Strong Duality、KKT条件
- 带条件/无条件优化问题、Projected GD
- 平滑函数、Convergence Analysis
【部分案例讲解】
- 基于QP的股票投资组合策略设计
- 基于LP的短文本相似度计算
- 基于KNN的图像识别
<hr>
第二阶段 SVM与集成模型
本阶段主要目的是深入理解SVM以及核函数部分的知识点。为了理解清楚SVM的Dual转换，需要掌握第一部分里的Duality理论。另外，重点介绍Bagging和Boosting模型，以及所涉及到的几项有趣的理论。
【核心知识点】
- Max-Margin与线性SVM构建
- Slack Variable以及条件的松弛
- SVM的Dual、Kernelized SVM
- Kernel Functions, Mercer 定理
- Kernelized LR/KNN/K-Means/PCA
- Bagging, Boosting, Stacking
- 信息论与决策树
- 随机森林，完全随机森林
- 基于残差的提升树训练思想
- GBDT与XGBoost
- 集成不同类型的模型
- VC理论， PAC Learning
【部分案例讲解】
- 基于XGBoost的金融风控模型
- 基于PCA和Kernel SVM的人脸识别. 
- 基于Kernal PCA和Linear SVM的人脸识别
<hr>
第三阶段 无监督学习与序列模型
本阶段主要目的是学习无监督算法和经典的序列模型。重点讲解EM算法以及GMM，K-means的关系，同时花几次课程时间来仔细讲解CRF的细节：从无向图模型、Potential函数、Log-Linear Model、逻辑回归、HMM、MEMM、Label Bias、Linear CRF、Inference，最后到Non-Linear CRF。
【核心知识点】
- K-means、GMM以及EM
- 层次聚类，DCSCAN，Spectral聚类算法
- 隐变量与隐变量模型、Partition函数
- 条件独立、D-Separation、Markov性质
- HMM以及基于Viterbi的Decoding
- Forward/Backward算法
- 基于EM算法的参数估计
- 有向图与无向图模型区别
- Log-Linear Model，逻辑回归，特征函数
- MEMM与Label Bias问题
- Linear CRF以及参数估计
【部分案例讲解】
- 基于HMM和GMM的语音识别
- 基于聚类分析的用户群体分析
- 基于CRF的命名实体识别
<hr>
第四阶段 深度学习
本阶段主要讲解深度学习理论以及常见的模型。这里包括BP算法、卷积神经网络、RNN/LSTM、BERT、XLNet、ALBERT以及各类深度学习图模型。另外，也会涉及到深度相关的优化以及调参技术。 
【核心知识点】
- 神经网络与激活函数
- BP算法、卷积层、Pooling层、全连接层
- 卷积神经网络、常用的CNN结构
- Dropout与Batch Normalization
- SGD、Adam、Adagrad算法
- RNN与梯度消失、LSTM与GRU
- Seq2Seq模型与注意力机制
- Word2Vec, Elmo, Bert, XLNet
- 深度学习中的调参技术
- 深度学习与图嵌入（Graph Embedding）
- Translating Embedding (TransE)
- Node2Vec- Graph Convolutional Network
- Graph Neural Network
- Dynamic Graph Embedding
【部分案例讲解】
- 基于Seq2Seq和注意力机制的机器翻译
- 基于TransE和GCN的知识图谱推理
- 基于CNN的人脸关键点检测
第五阶段 推荐系统与在线学习
推荐系统一直是机器学习领域的核心，所以在本阶段重点来学习推荐系统领域主流的算法以及在线学习的技术、包括如何使用增强学习来做推荐系统。 在线学习算法很深具有很漂亮的理论基础，在本阶段你都会一一体会到！
【核心知识点】
- 基于内容和协同过滤的推荐算法
- 矩阵分解，带条件的矩阵分解
- 基于内容的Gradient Tree
- 基于深度学习的推荐算法
- 冷启动问题的处理
- Exploration vs Exploitation
- Multi-armed Bandit
- UCB1 algorithm，EXP3 algorithm
- Adversarial Bandit model
- Contexulalized Bandit、LinUCB
【部分案例讲解】
- 使用GB Tree做基于 interaction 与 content的广告推荐
- 使用深度神经网络做基于interaction 与 content的推荐
- LinUCB做新闻推荐, 最大化rewards
<hr>
第六阶段 贝叶斯模型
本阶段重点讲解贝叶斯模型。贝叶斯派区别于频率派，主要的任务是估计后验概率的方式来做预测。我们重点讲解主题模型以及不同的算法包括吉布采样、变分法、SGLD等，以及如何把贝叶斯的框架结合在深度学习模型里使用，这就会衍生出Bayesian LSTM的模型。贝叶斯部分的学习需要一定的门槛，但我们会让每个人听懂所有细节！ 
【核心知识点】
- 主题模型（LDA) 以及生成过程
- Dirichlet/Multinomial Distribution
- 蒙特卡洛与MCMC
- Metropolis Hasting与Gibbs Sampling
- 使用Collapsed Gibbs Sampler求解LDA
- Mean-field variational Inference
- 使用VI求解LDA
- Stochastic Optimization与贝叶斯估计
- 利用SLGD和SVI求解LDA
- 基于分布式计算的贝叶斯模型求解
- 随机过程与无参模型（non-parametric)
- Chinese Retarant Process
- Stick Breaking Process
- Stochastic Block Model与MMSB
- 基于SGLD与SVI的MMSB求解
- Bayesian Deep Learning模型
- Deep Generative Model
【部分案例讲解】
- 基于Bayesian LSTM的文本分析
- 使用无参主题模型做文本分类
- 基于贝叶斯模型实现小数量的图像识别
<hr>
第七阶段 增强学习与其他前沿主题
本阶段重点讲解增强学习以及前沿的内容，包括增强学习在文本领域的应用，GAN, VAE，图片和文本的Disentangling，深度学习领域可解释性问题、Adversial Learning, Fair Learning等最前沿的主题。 这一阶段的安排也会根据学员的兴趣点做局部的调整。
【核心知识点】
- Policy Learning、Deep RL
- Variational Autoencoder(VAE)与求解
- 隐变量的Disentangling
- 图像的生成以及Disentangling
- 文本的生成以及Disentangling
- Generative Adversial Network(GAN)
- CycleGan
- 深度学习的可解释性
- Deconvolution与图像特征的解释
- Layer-wise Propagation
- Adversial Machine Learning
- Purturbation Analysis
- Fair Learning
【部分案例讲解】
- 基于GAN的图像生成
- 基于VAE的文本Style Transfer
- 可视化机器翻译系统
