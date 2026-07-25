# 同济高数第七版第五章双语习题册

[English README](README.md)

这是一套面向 Goodnotes 的双语学习资料，范围与同济大学《高等数学》第七版
上册第五章“定积分”对齐。项目独立编写，不是同济大学或高等教育出版社的官方
出版物。

## 成品下载

- [中文版习题册](dist/同济高数第七版_第五章_习题册_中文.pdf)
- [中文版超详细解析](dist/同济高数第七版_第五章_超详细解析_中文.pdf)
- [English Exercise Workbook](dist/Tongji_Calculus_7e_Chapter_5_Exercises_EN.pdf)
- [English Detailed Solutions](dist/Tongji_Calculus_7e_Chapter_5_Detailed_Solutions_EN.pdf)
- [SHA-256 校验值](SHA256SUMS)
- [发布与公式审计](reports/release_audit.md)

## 内容与结构

- 恰好 100 道题，按基础、标准、进阶、困难、挑战逐级递进。
- 覆盖 Riemann 和、定积分性质与平均值、微积分基本定理、Newton–Leibniz
  公式、定积分换元与分部积分、反常积分、审敛法以及 Gamma 函数选学内容。
- 含单选、多选、判断、填空、计算、证明、综合和错解诊断八种题型。
- 每题解析都含知识点、审题分析、至少四步推导、易错点、验算、方法总结和
  变式提示。
- 四份 PDF 使用完全一致的 Q001–Q100 编号。
- 习题册采用 4:3 横版并为每题保留独立书写页；解析册采用 4:3 竖版，留白
  宽松。

## 公式质量

题目、选项、答案与解析中的数学内容都以显式标准 LaTeX 源码保存。构建门禁
会：

1. 拒绝裸露 Unicode 数学快捷符号、斜杠除法、未闭合公式和高风险歧义写法；
2. 用固定版本 KaTeX 0.17.0 严格解析每一个公式片段；
3. 用 Tectonic 0.16.9 的 XeTeX 引擎和 STIX Two Math 编译矢量公式；
4. 检查中英文结构、100 个题目书签、字体、页面尺寸、校验值、可复现性和
   PDF 危险动作；
5. 用 PDFium 渲染并检查每一页是否裁切或异常稀疏，再人工复核代表性的公式
   密集页。

这里的“KaTeX 兼容”是源码审计标准；PDF 中呈现的是由 XeTeX 排版的矢量数学
公式，不是把 `$...$` 字符原样印在页面上。所有含奇点的反常积分都按定义
分段；Cauchy 主值绝不冒充普通收敛。

## 题目来源与原创边界

本套题保留逐题可审计的 `source_lineage`：

- 20 道开放教材方法改写；
- 50 道独立重写的经典方法变式；
- 30 道原创综合、比较、证明或诊断题。

开放来源包括 OpenStax Calculus 和 MIT OpenCourseWare。仓库不复制商业教材
的题干或解析；同济大学与高等教育出版社页面只用于核对版本和章节范围。具体
登记表与版权边界见 [SOURCES.md](SOURCES.md)。

## 推荐训练方法

1. 先按 Q001–Q100 顺序完成，首次作答不要打开解析册。
2. 订正时把错误归为：概念、端点方向、代数变形、方法选择、参数定义域、
   奇点拆分或敛散判断。
3. 对有限区间积分，用求导、对称性、估值或另一种换元独立验算。
4. 对反常积分，先写定义极限，再计算；每个问题端点必须单独检查。
5. 48 小时后重做错题；一周后按知识点交叉抽题。

## 优点与局限

优点是把公式熟练度与定义推理、证明、参数分类、错解诊断和独立验算结合起来。
题组会明确区分带符号面积与几何面积、普通反常积分与主值、充分估计与精确值；
中英文编号和结构完全对应。

局限是 100 题无法穷尽所有换元结构与审敛比较；难度会受个人代数和三角基础
影响。Gamma 函数内容明确标为选学。静态 PDF 不能依据个人错题自动调整顺序。
“经典方法变式”表示方法传统，不等于某本商业教材中的逐字原题。

## 本地生成与验证

经过验证的构建环境使用 Python 3.12+、Node.js 20+、KaTeX 0.17.0、Tectonic
0.16.9 和固定的 `default_bundle_v33`。中文、拉丁正文和数学分别使用 Fandol、
TeX Gyre Heros 与 STIX Two Math 开源字体。

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
npm ci
python scripts/generate_checkpoint_q001_q050.py
python scripts/generate_q051_q100.py
python scripts/merge_corpus.py
python scripts/migrate_latex.py
python scripts/validate_content.py
pytest -q
npm run validate:katex
python scripts/build_pdfs.py
python scripts/verify_reproducible.py
python scripts/update_checksums.py
python scripts/validate_pdfs.py
python scripts/render_validate.py
```

可编辑题目位于 [`content/parts`](content/parts)，合并后的规范语料是
[`content/questions.json`](content/questions.json)。排版工具与字体许可见
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

原创项目内容的许可见 [LICENSE](LICENSE)。CC BY-NC-SA 4.0 允许非商业分享与
改编；由于含有“非商业”限制，本仓库准确地说是公开源文件（source-available），
而不是 OSI 定义下的开源软件。
